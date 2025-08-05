import random
board="1|2|3\n4|5|6\n7|8|9"
print("Bienvenue dans le jeu du Tic-Tac-Toe !"
      "\nVoici le plateau de jeu :"
      "\n" + board)
player1 = "X"
player2 = "O"
current_player = player1

while True:
    if current_player == player2:
        move = str(random.randint(1, 9))
    else:
        move = input(f"Joueur {current_player}, choisissez une case (1-9) ou 'q' pour quitter : ")
    if move not in "123456789" and move != 'q':
        print("Entrée invalide. Veuillez choisir un nombre entre 1 et 9.")
        continue
    if move == 'q':
        print("Merci d'avoir joué ! À bientôt.")
        break
    if move not in board :
        print("Cette case est déjà prise. Veuillez en choisir une autre.")
        continue
    board = board.replace(move, current_player)
    print("Nouveau plateau de jeu :")
    print(board)
    if (board[0] == board[2] == board[4] == current_player or 
        board[6] == board[8] == board[10] == current_player or 
        board[12] == board[14] == board[16] == current_player or 
        board[0] == board[6] == board[12] == current_player or 
        board[2] == board[8] == board[14] == current_player or 
        board[4] == board[10] == board[16] == current_player or 
        board[0] == board[8] == board[16] == current_player or 
        board[4] == board[8] == board[12] == current_player):
        print(f"Félicitations, Joueur {current_player} a gagné !")
        break
    if all(cell not in "123456789" for cell in board):
        print("Match nul ! Le jeu est terminé.")
        break
    current_player = player2 if current_player == player1 else player1
    