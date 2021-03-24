from random import randint
import os
import time
import sys
import tkinter as tk
from tkinter import END

cash = 500
clear = lambda: os.system('cls')

def GamesList():
    print("Bienvenue au Ycasino, le casino de Ynov \n")
    print("Voici la liste de nos jeux : \n\n 1 - Roulette \n 2 - Blackjack \n 3 - Bataille navale \n ")

def Menu(chosen_game) :
    print("                                                     Votre solde actuel: ", cash)
    print("                                                     Jeu actuel: ", chosen_game,"\n \n \n \n ")
    print("                      ", chosen_game, "                   \n \n \n ")

def ChooseGame():
    clear()
    GamesList()
    user_choice = int(input("A quel jeu voulez-vous jouer ? \n "))
    if user_choice == 1 :
        Chosen_Roulette()
    elif user_choice == 2:
        Blackjack(cash)
    elif user_choice == 3:
        Navale(cash)

def PlayAgain(chosen_game):
    print("solde actuel : ", cash,)
    print("jeu actuel : ", chosen_game)
    play_choice = input("souhaitez-vous rejouer au jeu précédent ? ( oui/non )")
    if play_choice == "oui" or play_choice == "o" :
        print("88888888888888888888888888888888888888888888888888888888888888888888888")
    else:
        ChooseGame()

def Chosen_Roulette():
    chosen_game = "Roulette"
    while True :
        clear()
        Menu(chosen_game)
        want_to_play = input("Souhaitez-vous jouer à la roulette ? ( oui/non ) ")
        if want_to_play == "o" or want_to_play == "oui" :
            Roulette(cash)
            clear()
            break
        else :
            print("D'accord, merci d'être passé.")
            time.sleep(2)
            want_to_play = input("Souhaitez-vous jouer à un autre jeu ? ( oui/non )")
            if want_to_play == "o" or want_to_play == "oui" :
                clear()
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
        clear()
        Menu(chosen_game)

        try :
            chosen_number = int(input("Choisissez le numéro sur lequel miser : \n"))
        except ValueError :
            print("Veuillez choisir un nombre")
        else :
            while chosen_number > 49 or chosen_number < 0 :
                clear()
                print("Veuillez choisir un nombre compris entre 0 et 49 inclus")
                chosen_number = int(input("Choisissez le numéro sur lequel miser : \n"))

        color = chosen_number%2
        if color == 0 :
            print("Couleur associée à votre numéro: Noir")
        else:
            print("Couleur associée à votre numéro: Rouge")

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
            clear()
            random_number = randint(0,49)
            color2 = random_number%2
            if color2 == 0 :
                print("Couleur associée au numéro: Noir")
            else:
                print("Couleur associée au numéro: Rouge")
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
        clear()
        PlayAgain(chosen_game)

def Blackjack(cash):
    test = "toto"
    print(test)

def Navale(cash):
    test = "tata"
    print (test)

ChooseGame()