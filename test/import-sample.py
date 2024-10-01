# Simple Python script to demo importing 

import requests

# URL of the API endpoint
url = "https://api.github.com"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the response content
    print("Response from GitHub API:")
    print(response.json())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
