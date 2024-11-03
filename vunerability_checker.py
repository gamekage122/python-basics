import requests

def check_vulnerabilities(url):
    # Check for open directories
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Open Directory Found: {url}")
    
    # Check for insecure HTTP headers
    insecure_headers = ['X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy']
    for header in insecure_headers:
        if header not in response.headers:
            print(f"Insecure Header Missing: {header}")

# Example usage
target_url = input("Enter the url")
check_vulnerabilities(target_url)