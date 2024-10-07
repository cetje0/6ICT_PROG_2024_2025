# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}
print(f"Recept voor worst met wortelen en erwten.")
personen = int(input(f"Met hoeveel eten jullie: "))
for ingredient, hoeveelheid in recept.items():
    recept[ingredient] = (recept[ingredient]//4)*personen
    print(f"-{ingredient}: {recept[ingredient]} gr.")
    
    