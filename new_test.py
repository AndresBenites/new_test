import sys
import requests

r = requests.get("https://www.google.com")

test = "this is a test"

print(sys.version)
print(sys.executable)
print(r.url, r.status_code)
