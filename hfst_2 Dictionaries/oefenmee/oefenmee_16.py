# Maak voor deze oefen mee gebruik van onderstaande dictionary-structuur.
landen_feiten = {
    'Frankrijk': {
        'hoofdstad': 'Parijs',
        'bevolking': 67348000,
        'taal': 'Frans',
    },
    'Belgie': {
        'hoofdstad': 'Brussel',
        'bevolking': 11563000,
        'taal': ['Nederlands', 'Frans', 'Duits'],
    },
    'Duitsland': {
        'bevolking': 83190556,
        'taal': 'Duits',
    }
}
print(f"Hoofdsteden van Europese landen...")
for land, stad in landen_feiten.items():
    if landen_feiten[land][stad] == 'hoofdstad':
        for stad, waarde in stad.items():
            print(f"{land}, {waarde}")