import requests


endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    'title': 'New Product',
}

response = requests.post(endpoint, json=data)
print(response.json())
