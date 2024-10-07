# Start de oefen mee met onderstaande dictionary.
planner = {
    "Slaap": 9,
    "Werk":  3,
    "Ontspanning": 8
}
uur_teller = 0
print(f"Planning van morgen")
for activiteit, duur in planner.items():
    print(f"-{activiteit}: {duur} u.")
    uur_teller += duur
    uur_over = 24 - uur_teller
print(f"je hebt {uur_over} u over.")