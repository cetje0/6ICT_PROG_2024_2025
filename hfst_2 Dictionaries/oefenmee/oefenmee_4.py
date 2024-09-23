dino_klassementen = {
    "carnivoor": "giganotosaurus",
    "omnivoor": "meawing",
    "herbivoor": "therizinosaurus"
}
klasse = input(f"welk klassement wil je van je dino: ")
if klasse not in dino_klassementen:
    print(f"kon {klasse} niet vinden in dino klassement")
else:
    print(dino_klassementen[klasse])