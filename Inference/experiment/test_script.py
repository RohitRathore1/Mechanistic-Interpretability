import requests

url = "http://127.0.0.1:5000/predict"
data = {"text": "What is the capital of India?"}
response = requests.post(url, json=data)

print(response.json())