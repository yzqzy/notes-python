import requests

url = "http://localhost:3000/api"
response = requests.get(url)

print(response.text)
