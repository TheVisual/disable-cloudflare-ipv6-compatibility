import requests

# Replace these with your actual API token and Zone ID
api_token = 'YOUR_API_TOKEN_HERE' # API Key (NOT GLOBAL)
zone_id = 'YOUR_ZONE_ID_HERE' # Site Zone ID

# Headers for authentication
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

# Endpoint to modify IPv6 setting
url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/ipv6'

# Data payload to disable IPv6 compatibility
data = {
    'value': 'off'  # Assuming 'off' disables IPv6 compatibility; check documentation
}

# Make the PATCH request to update the setting
response = requests.patch(url, headers=headers, json=data)

if response.status_code == 200:
    print("Successfully disabled IPv6 compatibility.")
else:
    print("Failed to update setting. Status code:", response.status_code)
    print("Response:", response.text)
