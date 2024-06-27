import requests

# API endpoint


# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Process the retrieved data
    print(data)
else:

    raise ValueError(f"Error: {response.status_code} - {response.text} from the 'index.py'")