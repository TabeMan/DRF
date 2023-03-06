import requests


endpoint = "http://127.0.0.1:8000/api/products/3/"

response = requests.get(
    endpoint, json={"title": "Hello World!"})
print(response.json())
