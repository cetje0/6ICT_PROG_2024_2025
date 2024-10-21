# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
spelinfo = {
    'speler1': {
        'naam': 'Alice',
        'hacker': False,
        'positie': {
            'x': 10,
            'y': 5
        },
        'inventaris': {
            'wapen': 'zwaard',
            'bepantsering': 'schild',
            'goud': 50
        }
    },
    'speler2': {
        'naam': 'Bob',
        'hacker': True,
        'positie': {
            'x': 2,
            'y': 8
        },
        'inventaris': {
            'wapen': 'boog',
            'goud': 0
        }
    }
}
print(spelinfo['speler2']['naam'])
print(spelinfo['speler1']['positie'])
print(spelinfo['speler2']['inventaris']['wapen'])
print(spelinfo)