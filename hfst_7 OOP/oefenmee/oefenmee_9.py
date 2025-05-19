# Maak de klasse Hond aan zoals omschreven in oefen mee 9.
import random
class Hond:
    locaties:list = ["living", "tuin", "buren", "keuken"]
    def __init__(self, naam:str)->None:
        self.naam = naam
        self.locatie = random.choice(self.locaties)
        print(f"{self.naam} {self.locatie}")
    def ziet_hond(self, andere_hond:'Hond')-> None:
        if self.locatie == andere_hond.locatie:
            print(f"{self.naam} ziet {andere_hond.naam} in de {self.locatie}.")
            self.locatie = random.choice(self.locaties)
            gekozen_hond = random.choice([self, andere_hond])
            print(f"{gekozen_hond.naam} is bang en rent naar de {self.locatie}.")
        else:
             print(f"{self.naam} ziet {andere_hond.naam} niet in de {self.locatie}.")

" Via onderstaande code kan je niveau 1 testen. "

# hond_1 = Hond("Lulu", "keuken")
# hond_2 = Hond("Floris", "keuken")
# hond_3 = Hond("Ranger", "tuin")

# hond_1.ziet_hond(hond_2)
# hond_1.ziet_hond(hond_3)


" Via onderstaande code kan je niveau 2 & 3 testen. Opgelet! Resultaat is random. "
" Best print je in __init__ ook de locatie waar iedere hond start, zo kan je de werking makkelijker nagaan. "

hond_1 = Hond("Lulu")
hond_2 = Hond("Floris")
hond_3 = Hond("Ranger")

hond_1.ziet_hond(hond_2)                  
hond_1.ziet_hond(hond_3)   
          
print(hond_1.locatie)   
