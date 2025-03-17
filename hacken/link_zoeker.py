import requests

# TODO 1: vervang URL door te doorzoeken webpagina.
URL = "http://172.16.112.19:8000/login" 
html_code = requests.get(URL).text
# html link voorbeeld: <a href="https://www.w3schools.com/">Visit W3Schools.com!</a>

# Overloop iedere regel HTML-code apart.
for regel in html_code.split("\n"):
    if "href" in regel:
        print("##############")
        print(regel)
        print("##############")