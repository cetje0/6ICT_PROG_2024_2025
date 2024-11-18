lijst_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Rij,Kolom: Element")
# for index_hoofd, sublijst in enumerate(lijst_2D):
    # for index_sub, Element in enumerate(sublijst):
    #     if index_hoofd == 0 or index_hoofd == 2:
    #         print(f"{index_hoofd}, {index_sub}: {Element}")

for index_hoofd, sublijst in enumerate(lijst_2D):
    for index_sub, Element in enumerate(sublijst):
        if index_hoofd == index_sub:
            print(f"{index_hoofd}, {index_sub}: {Element}")