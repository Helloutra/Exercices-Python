# Interface PyQt5 pour le jeu Tic Tac Toe avec le joueur "0" qui représente un ordinateur, nécessite PyQt5
# Assurez-vous d'avoir installé PyQt5 avec `pip install PyQt5`

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from random import choice

class TicTacToeInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 400)
        self.initUI()
        self.reset_game()

    def initUI(self):
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        self.board_labels = [QLabel(str(i + 1), self) for i in range(9)]
        for i, label in enumerate(self.board_labels):
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 24px; border: 1px solid black;")
            label.mousePressEvent = lambda event, index=i: self.make_move(index)
            grid_layout.addWidget(label, i // 3, i % 3)
        main_layout.addLayout(grid_layout)
        self.status_label = QLabel("Bienvenue dans le jeu Tic Tac Toe !", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)
        self.reset_button = QPushButton("Réinitialiser le jeu", self)
        self.reset_button.clicked.connect(self.reset_game)
        main_layout.addWidget(self.reset_button)
        self.setLayout(main_layout)
        self.current_player = "X"
        self.player2 = "O"

    def reset_game(self):
        for label in self.board_labels:
            label.setText(str(self.board_labels.index(label) + 1))
            label.setStyleSheet("font-size: 24px; border: 1px solid black;")
        self.status_label.setText("Bienvenue dans le jeu Tic Tac Toe !")
        self.current_player = "X"
        self.player2 = "O"
        self.game_over = False

    def make_move(self, index):
        if self.game_over:
            self.status_label.setText("Le jeu est terminé. Veuillez réinitialiser pour jouer à nouveau.")
            return
        label = self.board_labels[index]
        if label.text() in ["X", "O"]:
            self.status_label.setText("Case déjà prise. Veuillez choisir une autre case.")
            return
        label.setText(self.current_player)
        label.setStyleSheet("font-size: 24px; border: 1px solid black; color: blue;" if self.current_player == "X" else "font-size: 24px; border: 1px solid black; color: red;")
        if self.check_winner():
            self.status_label.setText(f"Félicitations, Joueur {self.current_player} a gagné !")
            self.game_over = True
        elif all(label.text() in ["X", "O"] for label in self.board_labels):
            self.status_label.setText("Match nul ! Le jeu est terminé.")
            self.game_over = True
        else:
            self.current_player = self.player2 if self.current_player == "X" else "X"
            if self.current_player == "O":
                self.computer_move()

    def computer_move(self):
        available_moves = [i for i, label in enumerate(self.board_labels) if label.text() not in ["X", "O"]]
        if available_moves:
            move = choice(available_moves)
            self.make_move(move)
        else:
            self.status_label.setText("Aucun coup possible pour l'ordinateur.")

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        for combo in winning_combinations:
            if (self.board_labels[combo[0]].text() == self.current_player and
                self.board_labels[combo[1]].text() == self.current_player and
                self.board_labels[combo[2]].text() == self.current_player):
                return True
        return False
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToeInterface()
    window.show()
    sys.exit(app.exec_())