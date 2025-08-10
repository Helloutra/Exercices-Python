# Interface PyQt5 pour le solveur de Sudoku, nécessite PyQt5
# Assurez-vous d'avoir installé PyQt5 avec `pip install PyQt5`
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox

class SudokuSolverInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Solveur de Sudoku")
        self.setGeometry(100, 100, 600, 600)
        self.initUI()
        
    def initUI(self):
        layout = QGridLayout()
        self.sudoku_inputs = [[QLineEdit(self) for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.sudoku_inputs[i][j].setFixedSize(40, 40)
                self.sudoku_inputs[i][j].setMaxLength(1)
                self.sudoku_inputs[i][j].textChanged.connect(
                    lambda text, x=i, y=j: (self.focus_cellule_suivante(x, y), self.verifier_grille_complete())
                )
                layout.addWidget(self.sudoku_inputs[i][j], i, j)
        self.solve_button = QPushButton("Résoudre", self)
        self.solve_button.setEnabled(False)
        self.solve_button.clicked.connect(self.solve_sudoku)
        layout.addWidget(self.solve_button, 9, 0, 1, 9)
        self.setLayout(layout)


    def focus_cellule_suivante(self, i, j):
        if self.sudoku_inputs[i][j].text():
            if j < 8:
                self.sudoku_inputs[i][j+1].setFocus()
            elif i < 8:
                self.sudoku_inputs[i+1][0].setFocus()

    def solve_sudoku(self):
        sudoku = []
        positions_vides = set()
        for i in range(9):
            row = []
            for j in range(9):
                text = self.sudoku_inputs[i][j].text()
                if text.isdigit() and 0 <= int(text) <= 9:
                    val = int(text)
                    row.append(val)
                    if val == 0:
                        positions_vides.add((i, j))
                else:
                    QMessageBox.warning(self, "Erreur", f"Case ({i+1},{j+1}) invalide : entrez un chiffre de 0 à 9.")
                    return
            sudoku.append(row)
        if all(all(cell != 0 for cell in row) for row in sudoku):
            QMessageBox.information(self, "Info", "La grille est déjà complète.")
            return
        if self.resoudre_sudoku(sudoku):
            for i in range(9):
                for j in range(9):
                    self.sudoku_inputs[i][j].setText(str(sudoku[i][j]))
                    if (i, j) in positions_vides:
                        self.sudoku_inputs[i][j].setStyleSheet("font-weight: bold; color: MediumVioletRed;")
                    else:
                        self.sudoku_inputs[i][j].setStyleSheet("")
        else:
            QMessageBox.warning(self, "Erreur", "Aucune solution trouvée.")

    def peut_etre_place(self, sudoku, ligne, col, nombre):
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
    
    def resoudre_sudoku(self, sudoku):
        for ligne in range(9):
            for col in range(9):
                if sudoku[ligne][col] == 0:
                    for nombre in range(1, 10):
                        if self.peut_etre_place(sudoku, ligne, col, nombre):
                            sudoku[ligne][col] = nombre
                            if self.resoudre_sudoku(sudoku):
                                return True
                            sudoku[ligne][col] = 0
                    return False
        return True
    
    def verifier_grille_complete(self):
        for i in range(9):
            for j in range(9):
                text = self.sudoku_inputs[i][j].text()
                if not (text.isdigit() and 0 <= int(text) <= 9):
                    self.solve_button.setEnabled(False)
                    return
        self.solve_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    solver = SudokuSolverInterface()
    solver.show()
    sys.exit(app.exec_())