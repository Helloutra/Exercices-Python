sudoku = []
positions_vides = set()
print("Entrez le sudoku ligne par ligne, avec des zéros pour les cases vides :")
for i in range(9):
    ligne = input(f"Ligne {i + 1} : ")
    while len(ligne) != 9 or not all(c.isdigit() for c in ligne):
        print("Erreur : chaque ligne doit contenir exactement 9 chiffres.")
        ligne = input(f"Ligne {i + 1} : ")
    sudoku.append([int(c) for c in ligne])
    for j, c in enumerate(ligne):
        if c == '0':
            positions_vides.add((i, j))

def peut_etre_place(sudoku, ligne, col, nombre):
    if nombre in sudoku[ligne]:
        return False
    for i in range(9):
        if sudoku[i][col] == nombre:
            return False
    start_ligne = (ligne // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_ligne, start_ligne + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == nombre:
                return False
    return True

def resoudre_sudoku(sudoku):
    for ligne in range(9):
        for col in range(9):
            if sudoku[ligne][col] == 0:
                for nombre in range(1, 10):
                    if peut_etre_place(sudoku, ligne, col, nombre):
                        sudoku[ligne][col] = nombre
                        if resoudre_sudoku(sudoku):
                            return True
                        sudoku[ligne][col] = 0
                return False
    return True
if resoudre_sudoku(sudoku):
    print("Le sudoku résolu est :")
    for i, ligne in enumerate(sudoku):
        ligne_affichee = ""
        for j, val in enumerate(ligne):
            if (i, j) in positions_vides:
                ligne_affichee += f"\033[4m{val}\033[0m "
            else:
                ligne_affichee += f"{val} "
        print(ligne_affichee)
else:
    print("Aucune solution trouvée.")