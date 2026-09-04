import requests

url = "https://api.open-meteo.com/v1/forecast"

response = requests.get(url,
                        params = {"latitude": 37.55,
                        "longitude": -77.46,
                        "current": "temperature_2m"})
data = response.json()
# print(data.keys())
# print(data["current"]["temperature_2m"])

url_aq = "https://air-quality-api.open-meteo.com/v1/air-quality"

aq_response = requests.get(url_aq,
                        params = {"latitude": 37.55,
                        "longitude": -77.46,
                        "current": "pm2_5"})

air_quality = aq_response.json()
# print(air_quality.keys())
print(air_quality["current"]["pm2_5"])