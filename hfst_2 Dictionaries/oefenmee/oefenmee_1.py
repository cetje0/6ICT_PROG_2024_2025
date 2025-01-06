import test_module

dino_klassementen = {
    "carnivoor": "giganotosaurus",
    "omnivoor": "meawing",
    "herbivoor": "therizinosaurus"
}
klasse = input(f"welk klassement wil je van je dino: ")
print(dino_klassementen[klasse])