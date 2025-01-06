import requests, json

url = "https://api.adviceslip.com/advice/search/api"
response_json = requests.get(url).json()

with open(r"6ICT_PROG_2024_2025\hfst_4 API\oefenmee\adviceslip_data.json", "w") as fp:
    json.dump(response_json, fp)
    print("data gedumpt")
print("Hier is wat wijsheid over API's...")
print(response_json["slips"][0]["advice"])