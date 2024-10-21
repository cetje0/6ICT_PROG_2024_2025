# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
grootste_steden = {
    'Frankrijk': {
        'Parijs': 2140526,
        'Marseille': 869815,
    },
    'Belgie': {
        'Brussel': 1209000,
        'Antwerpen': 523248,
    },
    'Duitsland': {
        'Berlijn': 3769495,
        'Hamburg': 1841179,
    }
}
print(f"Overzicht van grootste steden in Europese landen...")
for land, stad in grootste_steden.items():
    print(f"De grootste steden in {land} zijn: \n")
    for stad, inwonerss in stad.items():
        print(f"-{stad} met {inwonerss} inwoners\n")