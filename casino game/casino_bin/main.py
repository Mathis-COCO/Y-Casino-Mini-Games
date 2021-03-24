from random import randint
import os
import time
import sys

cash = 500
keep_playing = False
show_numbers = 0
clear = lambda: os.system('cls')
chosen_game = "Casino"

def Menu() :
    chosen_game = "Roulette"
    print("Bienvenue au Ycasino, le casino de Ynov")
    print("                                                     Votre solde actuel: ", cash)
    print("                                                     Jeu actuel: ", chosen_game,"\n \n \n \n ")
    print("                      ", chosen_game, "                   \n \n \n ")

while True :
    clear()
    Menu()
    want_to_play = input("Souhaitez-vous jouer à la roulette ? ( Oui/Non ) ")
    if want_to_play == "Oui" or want_to_play == "oui" :
        keep_playing = True
        clear()
        break
    else :
        print("D'accord, merci d'être passé.")
        time.sleep(2)
        keep_playing = False
        want_to_play = input("Souhaitez-vous jouer à un autre jeu ? ( Oui/Non )")
        if want_to_play == "Oui" or want_to_play == "oui" :
            clear()

while keep_playing == True:
    clear()
    Menu()

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
    show_numbers = 100

    if chosen_number%2 == random_number%2 :
        earned_cash = bet/2
        print("Dommage, vous avez perdu 50%' de votre mise.")
        cash += earned_cash
        print("Désormais votre solde s'estime à", cash)
    else:
        print("Dommage, vous avez perdu votre mise.\n Peut-être une autre fois.")
    time.sleep(6)