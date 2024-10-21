dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']]

gebruiker_rij = int(input(f"hoe veelste rij: "))
gebruiker_kolom = int(input(f"hoe veelste kolom: "))
hoeveelheid_rijen = len(dambord_2D)
print(hoeveelheid_rijen)
if gebruiker_rij > hoeveelheid_rijen-1:
    gebruiker_rij_goed = gebruiker_rij - hoeveelheid_rijen
    print(f"{dambord_2D[gebruiker_rij_goed][gebruiker_kolom]}")
