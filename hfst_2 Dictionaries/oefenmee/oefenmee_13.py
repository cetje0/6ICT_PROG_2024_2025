# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appels": 2,
    "bananen": 3,
    "kersen": 10,
    "mango's": 1
}
while True:
    status_while_loop = input("wil je bijkopen: ")
    if status_while_loop.lower() == "nee":
        break
    for fruit, hoeveelheid in fruitmand.items():
        gebruiker_fruit = int(input(f" hoeveel {fruit} wil je bijkopen (huidig aantal: {hoeveelheid}): "))
        fruitmand[fruit] += gebruiker_fruit

    print(f"In de fruitmand zit momenteel.")

    for fruit, hoeveelheid in fruitmand.items():
        print(f"-{fruitmand[fruit]} {fruit}")
print(fruitmand)