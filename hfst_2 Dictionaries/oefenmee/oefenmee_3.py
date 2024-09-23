persoonsinfo = { # info over een persoon
    "naam": "jan",
    "leeftijd": 16,
    "massa": 80
}
# oogkleur = persoonsinfo["oogkleur"]
# print(f"Deze persoon heeft {oogkleur} ogen.")
naam = "Jan"
print(persoonsinfo[naam])

print(f"{persoonsinfo['naam']} is {persoonsinfo['leeftijd']} jaar jong en weegt {persoonsinfo['massa']} kg.")
print(len(persoonsinfo))