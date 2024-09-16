// Function to parse URL parameters
function getQueryParams() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const payload = urlParams.get('payload');
    return payload;
}

// Function to process the JSON payload
function processPayload() {
    const jsonDisplay = document.getElementById('json-payload');
    const machineDisplay = document.getElementById('machine-id');
    const payload = getQueryParams();
    
    if (payload) {
        try {
            const jsonObj = JSON.parse(payload); // Parse the JSON string
            machineDisplay.textContent = jsonObj["id"];
            jsonDisplay.textContent = JSON.stringify(jsonObj, null, 4); // Pretty-print JSON
        } catch (e) {
            jsonDisplay.textContent = "Invalid JSON data.";
        }
        // TODO: Add custom logic here that uploads the data to the correct backend, server, etc. 
    } else {
        jsonDisplay.textContent = "No payload parameter found in the URL.";
    }
}

// Call the function to display the payload
processPayload();
