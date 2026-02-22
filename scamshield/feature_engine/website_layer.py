import requests

def check_ssl_certificate(url):
    try:
        response = requests.get(url, timeout=10)

        # If URL starts with https and request succeeds → SSL exists
        if url.startswith("https://"):
            return 0.0  # safe
        else:
            return 0.2  # slightly risky

    except:
        return 0.3  # cannot connect → suspicious