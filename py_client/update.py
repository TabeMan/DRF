import requests


endpoint = "http://127.0.0.1:8000/api/products/2/delete/"

response = requests.delete(
    endpoint, json={"title": "Milk",
                    'price': 40.00})
print(response.json())
