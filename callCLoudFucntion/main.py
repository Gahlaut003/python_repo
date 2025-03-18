import requests
from google.oauth2 import service_account

# Replace these values with your actual service account key file path and Cloud Function details
key_file_path = 'key2.json'
project_id = 'linear-pursuit-411707'
location = 'us-central1'  # e.g., us-central1
function_name = 'gcloudtestfunction'

# Load service account credentials
credentials = service_account.Credentials.from_service_account_file(
    key_file_path,
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# Get an access token
access_token = credentials.token
print(credentials)

# Build Cloud Function URL
function_url = f'https://{location}-{project_id}.cloudfunctions.net/{function_name}'

# Set up headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

# Make an HTTP request to trigger the Cloud Function
response = requests.post(function_url, headers=headers)

if response.status_code == 200:
    result = response.text
    print(result)
else:
    print(f"Error: {response.status_code}, {response.reason}")
