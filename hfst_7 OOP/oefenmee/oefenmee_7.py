# Werk verder met de klasse Hond van oefen mee 6.
class Hond:
    def __init__(self, naam:str, massa:int)->None:
            self.massa = massa  
            self.naam = naam

    def blaf(self):
        print(f"{self.naam} blaft")

    def weegschaal(zichzelf):
        print(f"{zichzelf.naam} weegt {zichzelf.massa}kg")

    def wijzig_naam(self, nieuwe_naam:str)->None:
        print(f"{self.naam} heet nu {nieuwe_naam}")

    def eten(self,hoeveelheid:int)->None:
        self.massa = self.massa + 0.3*hoeveelheid
        print(f"{self.naam} weegt nu {round(self.massa, 2)}kg")


" Via onderstaande code kan je niveau 1 testen. "
# hond = Hond("Lucky", 5)
# hond.wijzig_naam("Bolly")
hond_2 = Hond("niggarot", 1025)
hond_2.eten(0.5)
hond_2.eten(0.5)
hond_2.eten(0.5)
" Via onderstaande code kan je niveau 2 testen. "
hond = Hond("Lucky", 5)
hond.eten(0.5)
hond.eten(0.5)
hond.eten(0.5)

" Stel de test voor niveau 3 zelf op. "