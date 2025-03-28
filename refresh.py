import requests
import random

# Replace with your blog or webpage URL
url = "https://viralcontenttt.blogspot.com/2025/03/viral-content.html"

# Free public proxies (these change often)
proxies = [
    "http://44.215.100.135",
    "http://85.215.64.49",
    "http://43.153.78.185",
    "http://35.180.85.81",
]

def refresh_page():
    proxy = random.choice(proxies)
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=10)
        print(f"Success with {proxy}: {response.status_code}")
    except Exception as e:
        print(f"Error with {proxy}: {e}")

if __name__ == "__main__":
    refresh_page()
