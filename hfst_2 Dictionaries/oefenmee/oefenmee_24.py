# Maak voor deze oefen mee gebruik van onderstaande lijst van dictionaries.
film_reviews = [
    {'Matrix': 9.2, 'Avatar': 8.8, 'Fury': 9.0, 'Skyfall': 8.1},
    {'Matrix': 3.5, 'Avatar': 1, 'Fury': 8, 'Skyfall': 4},
    {'Matrix': 10, 'Avatar': 3, 'Fury': 7, 'Skyfall': 5}
]

for index_hoofd, subdict in enumerate(film_reviews):
    for index_subdict, Element in enumerate(subdict):
        if index_hoofd == 0 or index_hoofd == 2:
            print(f"{Element} een {subdict[Element]}")