# Maak de klasse Persoon & Hond aan zoals omschreven in oefen mee 10.
# Je start reeds met de __init__ van beide klassen.
class Hond:
    geen_eigenaar = True
    def __init__(self, naam):
        self.naam = naam
        self.eigenaar = ""

class Persoon:
    def __init__(self, naam):
        self.naam = naam
        self.honden = []
    def koop_hond(self, hond:'Hond')->None:
        if hond.eigenaar != "":
            print(f"{hond.naam} heeft reeds {self.naam} als eigenaar.")
        else:
            print(f"hond is alleen")
            self.honden.append(hond)
            hond.eigenaar = self.naam

    def is_eigenaar(self,hond:'Hond')->bool:
        if hond in self.honden :
            return True
        else:
            return False
" Via onderstaande code kan je niveau 1 testen. "

# hond_1 = Hond("Lulu")
# hond_2 = Hond("Floris")
# persoon_1 = Persoon("Jos")
# persoon_2 = Persoon("Jef")

# persoon_1.koop_hond(hond_1)
# persoon_2.koop_hond(hond_2)

# print(persoon_1.is_eigenaar(hond_1)) # True
# print(persoon_2.is_eigenaar(hond_1)) # False


" Via onderstaande code kan je niveau 2 testen. "
hond_1 = Hond("Lulu")
hond_2 = Hond("Floris")
persoon_1 = Persoon("Jos")
persoon_2 = Persoon("Jef")

persoon_1.koop_hond(hond_1)
persoon_2.koop_hond(hond_2)
persoon_2.koop_hond(hond_1) # Lulu heeft reeds Jos als eigenaar.

print(persoon_1.is_eigenaar(hond_1)) # True
print(persoon_2.is_eigenaar(hond_1)) # False

