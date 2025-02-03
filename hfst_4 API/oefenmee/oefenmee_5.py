import requests
import json


url = "https://v2.jokeapi.dev/joke/Christmas?amount=3"
response_json = requests.get(url).json() # Haal JSON uit response.

with open (r"6ICT_PROG_2024_2025\hfst_4 API\oefenmee\programeer_grap.json", "w") as fp:
    json.dump(response_json, fp)
    print("gedumpt")
for joke in response_json["jokes"]:
    # Bepaal of de grap uit 1 of 2 delen bestaat.
    if ("joke" in response_json):
        print(response_json["joke"]) 
            # De grap
    else:
        print(response_json["setup"])    # De setup
        print(response_json["delivery"]) # De punchline

