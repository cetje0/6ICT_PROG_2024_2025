# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}
print(f"Recept voor worst met wortelen en erwten.")
for ingredient, hoeveelheid in recept.items():
    print(f"-{ingredient}: {hoeveelheid} gr.")
    