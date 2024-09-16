import json
import urllib.parse
import qrcode
from asyncua.sync import Client, ua

def read_node(client, node_name):
    node = client.get_node(node_name)
    return node.read_value()

def retrieve_plc_data():
    ip = "localhost"
    port = 4840
    username = "Admin"
    password = "password"
    url = f"opc.tcp://{username}:{password}@{ip}:{port}/"
    client = Client(url=url)
    client.connect()
    id = read_node(client, "ns=6;s=::Logic:id")
    cycle_counter = read_node(client, "ns=6;s=::Logic:cycleCounter")
    good_products = read_node(client, "ns=6;s=::Logic:goodProducts")
    bad_products = read_node(client, "ns=6;s=::Logic:badProducts")
    packml_state = read_node(client, "ns=6;s=::Logic:packMLState")
    client.disconnect()
    return id, cycle_counter, packml_state, good_products, bad_products

def create_url():
    id, cycle_counter, packml_state, good_products, bad_products = retrieve_plc_data()
    payload = {
        "id": id, 
        "cycle_counter": cycle_counter,
        "packml_state": packml_state,
        "good_products": good_products,
        "bad_products": bad_products
    }
    # Convert the dictionary to a JSON string
    payload_json = json.dumps(payload)

    # URL encode the JSON string to safely include it as a query parameter
    encoded_payload = urllib.parse.quote_plus(payload_json)

    # Construct the final URL with the "payload" query parameter
    # base_url = "file:///C:/Projects/MusserAutomation/air-gapped-iiot/web/index.html"
    base_url = "https://air-gapped-iiot.s3.us-east-1.amazonaws.com/index.html"
    final_url = f"{base_url}?payload={encoded_payload}"

    return final_url

def generate_qr_code(url, output_file):
    # Create a QR code for the given URL
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    img.save(output_file)
    print(f"QR code saved as {output_file}")
    
url = create_url()
generate_qr_code(url, 'qr_code.png')
