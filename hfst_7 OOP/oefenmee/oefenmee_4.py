# Werk verder met de klasse Hond van oefen mee 2.

class Hond():
    naam= "death"
    massa= 50
    def blaf(self):
        print(f"{Hond.naam} blaft")

    def weegschaal(zichzelf):
        print(f"{Hond.naam} weegt {Hond.massa}kg")
        
    def benoem(self, naam:str)-> None:
        Hond.naam = naam
    
    def wegen(self, massa:int)->None:
        Hond.massa = massa

" Via onderstaande code kan je niveau 1 testen. "
hond = Hond()
hond.benoem("Fleur")
print( hond.naam )
hond.blaf()

" Via onderstaande code kan je niveau 2 testen. "
dier = Hond()
dier.benoem("Fifi")
dier.wegen(3)
print( dier.massa )
dier.weegschaal()