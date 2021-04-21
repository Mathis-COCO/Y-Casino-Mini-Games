from random import randint
import random
import os
import time
import sys
from colorama import Fore

cash = 500

def Clear(chosen_game):
    os.system('cls')
    print(f'_________________ JEU CHOISI : {chosen_game} _________________\n\n')

def ChooseGame():
    chosen_game = "Casino"
    Clear(chosen_game)
    print("Bienvenue au Ycasino, le casino de Ynov, le casino gratuit d'entrée \n")
    time.sleep(3.5)
    Clear(chosen_game)
    print("Voici la liste de nos jeux : \n\n 1 - Roulette \n 2 - Blackjack \n 3 - Bataille navale\n 4 - Pendu\n 5 - Juste Prix\n 6 - Pierre Papier Ciseaux\n 7 - TicTacToe\n")
    user_choice = int(input("A quel jeu souhaitez-vous jouer ?\n"))
    if user_choice <= 7 and user_choice >= 1 :
        PlayGameNumber(user_choice)

def PlayGameNumber(game_number):
    game_number = game_number-1
    game_list = [Chosen_Roulette,Blackjack,BatailleNavale,Pendu,JustePrix,RockPS,TicTacToe]
    game = game_list[game_number]
    game()

def BatailleNavale():
    cmd = 'python ./casino_games/bataille_navale.py'
    os.system(cmd)

def PlayAgain(chosen_game,game_number):
    Clear(chosen_game)
    print("jeu actuel : ", chosen_game)
    play_choice = input("\nsouhaitez-vous rejouer au jeu précédent ( oui/non ) ? ")
    if play_choice == "oui" or play_choice == "o" :
        print("starting game...")
        PlayGameNumber(game_number)
    else:
        chosen_game = ""
        ChooseGame()

def Chosen_Roulette():
    chosen_game = "Roulette"
    while True :
        Clear(chosen_game)
        print(f'Votre solde actuel : {cash}€\n')
        want_to_play = input("Souhaitez-vous jouer à la roulette ( oui/non ) ? ")
        if want_to_play == "o" or want_to_play == "oui" :
            Roulette(cash)
            Clear(chosen_game)
            break
        else :
            print("D'accord, merci d'être passé.")
            time.sleep(2)
            want_to_play = input("Souhaitez-vous jouer à un autre jeu ( oui/non ) ? ")
            if want_to_play == "o" or want_to_play == "oui" :
                Clear(chosen_game)
                ChooseGame()
                break
            else :
                if want_to_play == "n" or want_to_play == "non" or want_to_play == "no":
                    return None

def Roulette(cash):
    keep_playing = True
    show_numbers = 0
    chosen_game = "Roulette"

    while keep_playing == True:
        Clear(chosen_game)
        print(f'Votre solde actuel : {cash}€\n')

        try :
            chosen_number = int(input("Choisissez le numéro sur lequel miser : \n"))
        except ValueError :
            print("Veuillez choisir un nombre")
        else :
            while chosen_number > 49 or chosen_number < 0 :
                Clear(chosen_game)
                print("Veuillez choisir un nombre compris entre 0 et 49 inclus")
                chosen_number = int(input("Choisissez le numéro sur lequel miser : \n"))

        color = chosen_number%2
        if color == 0 :
            print("Couleur associée à votre numéro: Noir")
        else:
            print("Couleur associée à votre numéro: Rouge")

        Clear(chosen_game)
        try :
            bet = int(input("Combien d'argent souhaitez-vous miser ? \n"))
        except ValueError:
            print("Veuillez miser de l'argent pour pouvoir jouer.")
        except NameError:
            print("Veuillez miser de l'argent pour jouer au jeu.")
        else :
            while bet > cash or bet == 0 or bet <= 0 :
                print ("Vous possédez ", cash ,". Veuillez choisir un nommbre choisi entre 1 et ", cash)
                bet = int(input("Veuillez saisir une somme entre 1 et ", cash))
                cash -= bet
                print("Votre solde actuel : ", cash ,"\n")

        while show_numbers < 100 :
            Clear(chosen_game)
            random_number = randint(0,49)
            color2 = random_number%2
            if color2 == 0 :
                print("Couleur de la case: Noir")
            else:
                print("Couleur de la case: Rouge")
            if random_number < 10:
                print(" ____________" "\n" "|            |" "\n" "|    ",random_number,"     |" "\n" "|____________|")
            else:
                print(" ____________" "\n" "|            |" "\n" "|    ",random_number,"    |" "\n" "|____________|")
            if show_numbers <= 75 :
                time.sleep(0.1)
            elif show_numbers > 75 and show_numbers < 90 :
                    time.sleep(0.25)
            else :
                if show_numbers > 90 :
                    time.sleep(0.35)
            show_numbers += 1
        show_numbers = 0

        if chosen_number%2 == random_number%2 :
            earned_cash = bet/2
            print("Dommage, vous avez perdu 50%' de votre mise.")
            cash += earned_cash
            print("Désormais votre solde s'estime à", cash)
        else:
            print("Dommage, vous avez perdu votre mise.\n Peut-être une autre fois.")
        time.sleep(6)
        Clear(chosen_game)
        PlayAgain(chosen_game,1)

def Blackjack():
    chosen_game = "BlackJack"
    i = 0
    Clear(chosen_game)
    total = 0
    total_opponent = 0
    player_cards = []
    player_suits = []
    while True:
        values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        suits = ['♥','♦','♣','♠']
        card_A = 0
        want_to_play = ""
        while i < 2:
            time.sleep(2)
            value = random.choice(values)
            suit = random.choice(suits)
            Blackjack_Card(value, suit)
            player_cards.append(value)
            player_suits.append(suit)
            if value == 'A':
                try :
                    card_A = int(input("Vous avez un as, voulez-vous qu'il compte pour :\n- 1 point ou\n-11 points ? "))
                except TypeError :
                    print("Veuillez choisir 1 ou 11 :")
                except ValueError:
                    if card_A != 1 or card_A != 11:
                        print("veuillez choisir une valeur valide.")
                else :
                    if card_A == 11 :
                        total += 11
                    else :
                        if card_A == 1 :
                            total += 1
            elif value == 'J' or value == 'Q' or value =='K':
                total += 10
            else :
                total += value
            print('\n')
            i+=1
        print(f'                Somme de vos cartes : {total}\n\n')
        while True :
            if total < 21 or total < total_opponent :
                want_to_play = input("Voulez-vous augmenter votre nombre de cartes ? ")
                break
        if want_to_play == "oui" or want_to_play == "o" or want_to_play == "yes":
            Clear(chosen_game)
            j = 0
            while j<len(player_cards):
                prev_card = player_cards[j]
                prev_suit = player_suits[j]
                Blackjack_Card(prev_card, prev_suit)
                if j == len(player_cards):
                    print(f'                Somme de vos cartes : {total}\n\n')
                j += 1

            value = random.choice(values)
            suit = random.choice(suits)
            player_cards.append(value)
            player_suits.append(suit)
            Blackjack_Card(value, suit)
            if value == 'A':
                try :
                    card_A = int(input("Vous avez un as, voulez-vous qu'il compte pour :\n- 1 point ou\n-11 points ? "))
                except TypeError :
                    print("Veuillez choisir 1 ou 11 :")
                except ValueError:
                    if card_A != 1 or card_A != 11:
                        print("veuillez choisir une valeur valide.")
                else :
                    if card_A == 11 :
                        total += 11
                    else :
                        if card_A == 1 :
                            total += 1
            elif value == 'J' or value == 'Q' or value =='K':
                total += 10
            else :
                total += value
        else:
            print("Votre adversaire joue...")
            i = 0
            while i < 2:
                time.sleep(2)
                opponent_suit = random.choice(suits)
                opponent_value = random.choice(values)
                if opponent_value == 'A':
                    if total_opponent <= 10:
                        total_opponent += 11
                    else:
                        total_opponent += random.randint(1,11)
                elif opponent_value == 'J' or opponent_value == 'Q' or opponent_value =='K':
                    total_opponent += 10
                else :
                    total_opponent += opponent_value
                Blackjack_Card(opponent_value,opponent_suit)
                i += 1
            while total_opponent < total :
                opponent_value = random.choice(values)
                opponent_suit = random.choice(suits)
                Blackjack_Card(opponent_value, opponent_suit)
                if opponent_value == 'A':
                    if total_opponent <= 10:
                        total_opponent += 11
                    else:
                        total_opponent += 1
                elif opponent_value == 'J' or opponent_value == 'Q' or opponent_value =='K':
                    total_opponent += 10
                else :
                    total_opponent += opponent_value
                if total_opponent == 21 :
                    print("Le croupier a fait un blackjack")
                    time.sleep(4.5)
                    Clear(chosen_game)
                    PlayAgain(chosen_game,2)
                if total_opponent > 21:
                    print("Vous avez gagné, le score du croupier a dépassé 21")
                    time.sleep(4.5)
                    Clear(chosen_game)
                    PlayAgain(chosen_game,2)
            want_to_play = False

        if total == 21:
            print('Bien joué, vous avez fait un blackjack !')
            time.sleep(4.5)
            Clear(chosen_game)
            PlayAgain(chosen_game,2)
        if total > 21:
            print('La somme de vos cartes a dépassé 21.\nVous avez perdu')
            time.sleep(4.5)
            Clear(chosen_game)
            PlayAgain(chosen_game,2)

    # opponent drawing card if opponent_total <= 16

def Blackjack_Card(value, suit):
    print('                        ┌───────┐')
    print(f'                        | {value:<2}    |')
    print('                        |       |')
    print(f'                        |   {suit}   |')
    print('                        |       |')
    print(f'                        |    {value:>2} |')
    print('                        └───────┘')

def Pendu():
    while True:
        words = open('./casino_games/listedemot.txt')
        choice =words.readlines()
        word =random.choice(choice)
        tries = 7
        display = ""
        letters_found = ""
        letter = 0
        chosen_game = "Pendu"
        used_letters = []
        Clear(chosen_game)

        while letter < len(word):
            letter += 1
            display += "_ "
            print(letter)
        while tries > 0:
            Clear(chosen_game)
            print(" ".join(map(str, used_letters)))
            print(f'\nEssais restants : {tries}')
            print(f'\nMot à trouver : {display} \n')
            user_letter = input("Entrez une lettre : ")
            if user_letter not in used_letters :
                used_letters.append(user_letter)
                used_letters.append(" | ")
            if user_letter in word:
                letters_found = letters_found + user_letter
            else:
                tries = tries - 1
                if tries==0:
                    Clear(chosen_game)
                    print(" ".join(map(str, used_letters)))
                    print(f'\n                   {display}')
                    print(f'\n            Perdu ! Le mot était : {word}')
                    time.sleep(5)
                    Clear(chosen_game)
                    PlayAgain(chosen_game,4)
            display = ""
            for x in word :
                if x in letters_found:
                    display += x + " "
                else:
                    display += "_ "
                    if "_" not in display:
                        print("Bien joué, vous avez trouvé le bon mot")
                        time.sleep(4)
                        Clear(chosen_game)
                        PlayAgain(chosen_game,4)

def JustePrix():
    while True:
        n = random.randint(0, 100)
        answer = ""
        tries = 0
        chosen_game = "Juste Prix"
        Clear(chosen_game)
        prev_answers = []

        while tries < 5:
            remaining_tries = 4 - tries
            var = int(input("Entrez un nombre entre 0 et 100 : "))
            if var < n and var not in prev_answers :
                answer = ": Trop bas !"
                prev_answers.append(var)
                prev_answers.append(answer)
                prev_answers.append(" | ")
            else :
                if var not in prev_answers :
                    answer = ": Trop haut !"
                    prev_answers.append(var)
                    prev_answers.append(answer)
                    prev_answers.append(" | ")
            if var == n:
                answer = "Bravo ! Vous avez touvé !\n"
                print(var, answer)
                prev_answers = []
                tries = 0
                remaining_tries = 5
                time.sleep(2.5)
                PlayAgain(chosen_game,5)
            if remaining_tries == 0:
                if var < n and var not in prev_answers:
                    answer = ": Trop bas !"
                    prev_answers.append(var)
                    prev_answers.append(answer)
                    prev_answers.append(" | ")
                else :
                    answer = ":Trop haut !"
                    if var not in prev_answers :
                        prev_answers.append(var)
                        prev_answers.append(answer)
                        prev_answers.append(" | ")
                Clear(chosen_game)
                print(" ".join(map(str, prev_answers)))
                print("\nDommage, vous avez perdu. \n")
                time.sleep(2.5)
                print(f'le chiffre était : {n}')
                time.sleep(3)
                PlayAgain(chosen_game,5)

            print("\n")
            Clear(chosen_game)
            print(" ".join(map(str, prev_answers)))
            print(f'\nIl vous reste : {remaining_tries} essais\n')
            tries += 1

def RockPS():
    chosen_game = "Pierre Papier Ciseaux"
    Clear(chosen_game)
    AI_choice = randint(1,3)
    ally = Fore.BLUE
    ennemy = Fore.RED
    print("1 - Pierre\n2 - Papier\n3 - Ciseaux\n")
    while True:
        try :
            player_choice = int(input("Votre choix : "))
        except ValueError:
            print("Veuillez choisir 1, 2 ou 3")
            time.sleep(2)
            Clear(chosen_game)
            print("1 - Pierre\n2 - Papier\n3 - Ciseaux\n") 
            continue
        else :
            if 1 <= player_choice <= 3 :
                print("Pierre")
                time.sleep(1)
                print("papier")
                time.sleep(1)
                print("ciseaux")
                Clear(chosen_game)
                RPS(player_choice, ally)
                RPS(AI_choice, ennemy)
                if player_choice == AI_choice :
                    time.sleep(2)
                    print(Fore.WHITE + "égalité ! Veuillez choisir à nouveau...")
                    time.sleep(4)
                    RockPS()
                elif (player_choice == 1 and AI_choice == 2) or (player_choice == 2 and AI_choice == 3) or (player_choice == 3 and AI_choice == 1):
                    time.sleep(2)
                    print(Fore.WHITE + 'vous avez perdu, dommage.')
                    time.sleep(4)
                    Clear(chosen_game)
                    PlayAgain(chosen_game, 6)
                else :
                    time.sleep(2)
                    print(Fore.WHITE + 'Bien joué ! Vous avez gagné.')
                    time.sleep(4)
                    Clear(chosen_game)
                    PlayAgain(chosen_game, 6)

def RPS(player_choice, color) :
    if player_choice == 1:
        print(color + """
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
    elif player_choice == 2 :
        print(color + """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif player_choice == 3 :
        print(color + """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

def TicTacToe():
    cmd = 'python ./casino_games/tictactoe.py'
    os.system(cmd)

ChooseGame()

# THINGS TO PATCH :
#___________________________________________________________________________________________________________________________________
# underscore in Hugo's "Pendu" game
#___________________________________________________________________________________________________________________________________



# TRAVAIL :
#___________________________________________________________________________________________________________________________________
# Paul-Antoine : Pierre Papier Ciseaux, snake (not working)
# Diego : Juste prix
# Hugo : Pendu
# Mathis: Menus, Roulette, Blackjack, bataille navale, début de jeu pygame, modification du pendu de Hugo et du Juste prix de Diego
# Yrlan : Tic Tac Toe
#___________________________________________________________________________________________________________________________________
