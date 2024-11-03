import requests



def check_vulnerabilities(url):
    try:
        # Check if URL uses HTTPS
        if not url.startswith("https://"):
            print("Warning: URL does not use HTTPS")

        # Check for open directories
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Open Directory Found: {url}")
        
        # Check for insecure HTTP headers
        insecure_headers = [
            'X-Frame-Options', 
            'X-XSS-Protection', 
            'Content-Security-Policy',
            'Strict-Transport-Security',
            'X-Content-Type-Options',
            'Referrer-Policy'
        ]
        for header in insecure_headers:
            if header not in response.headers:
                print(f"Insecure Header Missing: {header}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
target_url = input("Enter the URL: ")
check_vulnerabilities(target_url)