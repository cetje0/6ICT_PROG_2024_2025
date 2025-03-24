# Werk verder met de klasse Hond van oefen mee 4.
class Hond:
    def __init__(self, naam:str, massa:int)->None:
            self.massa = massa  
            self.naam = naam

    def blaf(self):
        print(f"{self.naam} blaft")

    def weegschaal(zichzelf):
        print(f"{zichzelf.naam} weegt {zichzelf.massa}kg")

hond_1 = Hond(f"Floris", 8)
hond_2 = Hond("Fido", 3)
" Via onderstaande code kan je niveau 2 testen. "
hond_1.weegschaal()
hond_2.weegschaal()
