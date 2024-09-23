fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
nieuw_fruit  = "mango"
nieuw_aantal_mango = 1
nieuw_aantal_kers = 43
fruitmand[nieuw_fruit] = nieuw_aantal_mango

vorig_aantal_kers = fruitmand["kers"]
houddig_aantal_kers = vorig_aantal_kers - nieuw_aantal_kers
fruitmand["kers"] = houddig_aantal_kers

fruitmand.pop("kers")

print( fruitmand )
