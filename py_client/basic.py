import requests

# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"
get_response = requests.get(
    endpoint, params={"abc": 123}, json={"query": "Hello World"})  # HTTP Request


# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dictionary

print(get_response.json())
# print(get_response.status_code)
