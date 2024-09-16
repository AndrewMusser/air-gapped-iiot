# AIR GAPPED IIOT
This repository presents a concept for retrieving IIoT data from an air-gapped PLC - that is, a PLC that has no network connection to the outside world. The idea is to read PLC data with an OPC UA client, package this data into a JSON string, and embed that JSON string into a URL that points to a public website. Then generate a QR code based on this full URL, and display it on the machine's HMI. An operator with a smartphone can take a picture of the QR code onscreen, and this has the effect of pushing the recorded machine data up to the cloud. 

# WHY?
This can be interesting if you need to access your PLC's data, but don't want to risk connecting it to the internet. Effectively this sets up a full proof one-way data transfer from the PLC to the cloud. You don't have to worry about misconfiguring a firewall and accidentally opening up your PLC to attacks. 

# USAGE
This repository contains all the pieces required to reproduce the demo scenario. Here's a breakdown of each. 

### WEBSITE
The `web` folder contains a simple static website that is being hosted on a public S3 bucket: `https://air-gapped-iiot.s3.us-east-1.amazonaws.com/index.html`. This website simply parses out the URL query parameters, finds the JSON payload, extracts the machine ID, and displays a thank you message to the operator with the machine ID and the payload. Note that the JS script in this folder would be expanded for a real-world application so that it forwards the data to the correct location. There are also plenty of auth/security considerations that would need to get added to the website, but you get the general idea. 

### PLC PROJECT
The `plcProject` folder contains the source code for a sample PLC project that is responsible for generating the desired data. For the demo this includes machine ID, some product counters, and the machine's overall PackML state. This is a B&R project that can be run in simulation using Automation Studio and ARsim. 

### CLIENT
The `client` folder contains the Python source responsible for retrieving the data from the PLC and generating a QR code. 
