# import-sample.py
# Simple Python script to demonstrate importing modules
#------------------------------------------------------------------
import requests


# URL of the API endpoint
# The URL is stored in the variable 'url' as a string
url = "https://api.github.com"


#------------------------------------------------------------------


# Send a GET request to the API
# Use the requests module to make a GET request to the API 
# Passes the URL variable into the GET call, makes the call, and gets a value returned
# The response is stored in the 'response' variable
response = requests.get(url)

#------------------------------------------------------------------


# Check if the request was successful
# Verify if the status code of the response is 200 (HTTP OK)
if response.status_code == 200:
    # Print the response content
    print("Response from GitHub API:")
    # Output the response content as JSON
    print(response.json())
else:
    # If the status code is not 200, print an error message with the status code
    print(f"Failed to retrieve data. Status code: {response.status_code}")
