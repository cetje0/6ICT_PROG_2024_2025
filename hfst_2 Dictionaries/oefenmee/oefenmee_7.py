# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
while True:
    input_gebruiker = input(f"welke naam wil je verwijderen:")
    if input_gebruiker.lower() == "stop":
        break
    elif input_gebruiker in gasten:
        print(f"Welkom {gasten[input_gebruiker]} {input_gebruiker}. kom binnen")
        gasten.pop(input_gebruiker)
        
    else:
        print(f"De naam {input_gebruiker} staat niet op de lijst")