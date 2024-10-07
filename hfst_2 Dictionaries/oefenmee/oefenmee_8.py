# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
stad_gebruiker = input(f"Naar welke stad ga je naar toe: ")
stad = steden_temp.get(f"{stad_gebruiker}", "???")
print(f"Het is hier {stad} °C ")
