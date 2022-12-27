import requests

# Hacer una solicitud GET
#response = requests.get("http://127.0.0.1:5000")

# # Hacer una solicitud POST
url = "http://localhost:5000/"

payload = {'name': 'Julito'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 201:
    print(response.text)
else:
    print(f"Error {response.status_code}: {response.text}")

# # Hacer una solicitud PUT
# response = requests.put("http://127.0.0.1:5000", json="PUT")

# # Hacer una solicitud DELETE
# response = requests.delete("http://127.0.0.1:5000", params="DELETE")
