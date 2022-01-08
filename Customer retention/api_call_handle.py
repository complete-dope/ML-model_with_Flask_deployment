import requests
# we can check this on postman by inserting our content in body field in the json format. 
url="https://localhost:5000/apicall"

concat = requests.post(url , json())
print(concat.json())