import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = f"q={atraducir}&target=es&source=en"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "208c24c1eemsh70c0307617fcb35p1e3a7djsneddb7e91a187",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)