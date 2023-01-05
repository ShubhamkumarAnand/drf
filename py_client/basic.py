import requests

# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/"
get_response = requests.get(endpoint, data={"query": "Hello World"}) #HTTP Request


# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dictionary

# print(get_response.text)
# print(get_response.json())
print(get_response.status_code)
