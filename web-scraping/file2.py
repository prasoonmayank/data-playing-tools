import requests

google = requests.get('https://google.com/')

print google.status_code
print google.content[:200]
print google.headers
print google.cookies.items()
print type(google.content)


