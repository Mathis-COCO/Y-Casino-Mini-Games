from os import system

game = [0, 0, 0, 0, 0, 0, 0, 0, 0]
char_lookup = {0: "-", 1: "X", 2: "O"}
turn = 1

# Permet de tout supprimer dans la console
def cls():
    system("cls")

# Fonction qui crée le tableau
def drawBoard():
    game_board = list(map(lambda x: char_lookup[x], game))
    print("[{0[0]}] [{0[1]}] [{0[2]}]          0 1 2".format(game_board))
    print("[{0[3]}] [{0[4]}] [{0[5]}]          3 4 5".format(game_board))
    print("[{0[6]}] [{0[7]}] [{0[8]}]          6 7 8".format(game_board))

# Fonction qui check si un joueur a win
def win_detection():
    to_check = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for lst in to_check:
        check = list(map(lambda x: game[x], lst))
        if (check[0] != 0) & (check[0] == check[1] == check[2]):
            return check[0]
    return 0

# Détection égalité
def prod(iterable):
    out = 1
    for product in iterable:
        out *= product
    return out

def draw_detection():
    return prod(game) != 0

# Gestion des tours
def turn_swap():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1

class TicTacToeIndexError(Exception):
    pass

cls()
while True:
    print("C'est au tour du {}".format(char_lookup[turn]))
    drawBoard()

    try:
        move = int(input())
        if move not in range(9):
            raise ValueError
        if game[move] != 0:
            raise TicTacToeIndexError
        game[move] = turn

        won = win_detection()
        if won != 0:
            print("Le {} a gagné la partie!".format(char_lookup[won]))
            input("Appuyez sur entrer pour quitter")
            exit()

        if draw_detection():
            print("Egalité")
            input("Appuyez sur entrer pour quitter")
            exit()

        turn_swap()
        cls()
        
# Gestion d'erreur
    except ValueError:
        cls()
        print("Vous devez entrez un chiffre entre 0 et 8.")
    except TicTacToeIndexError:
        cls()
        print("Cette case est déja occupée.")
