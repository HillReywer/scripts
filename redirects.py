import requests
from requests.auth import HTTPBasicAuth

languages = ['en', 'fr', 'fr-ch', 'de', 'de-at', 'de-ch']
base_url = 'https://www.rockstargames.com'

# List of URLs to check
url_patterns = [
    '/landingpages/commercial-operator',
    
]
    
username = 'your_username'
password = 'your_password'

def check_links():
    for lang in languages:
        print(f"Checking links for language: {lang}")
        for pattern in url_patterns:
            url = f"{base_url}/{lang}{pattern}"
            response = requests.get(url, auth=HTTPBasicAuth(username, password), allow_redirects=False)

            if response.status_code == 200:
                print(f"URL {url} is OK")
            elif response.status_code == 301:
                redirected_url = response.headers['location']
                print(f"URL {url} is redirected permanently to {redirected_url}")
            else:
                print(f"URL {url} returned a {response.status_code} status code")

if __name__ == "__main__":
    check_links()
