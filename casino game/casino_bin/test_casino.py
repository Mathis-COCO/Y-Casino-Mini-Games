from random import randint
import os
import time

cash = 500
keep_playing = True
show_numbers = 0
clear = lambda: os.system('cls')

print("Bienvenue au Ycasino, le casino de Ynov")

while keep_playing :
    try :
        want_to_play = input("Souhaitez-vous jouer à la roulette ? ")
    except ValueError :
        pass
    else :
        if want_to_play == "yes" or "oui" or "y" or "ok" or "y" or "o":
            Roulette("cash", "show_numbers", "clear")
        else :
            print("D'accord, merci pour votre passage.")
            print("""Liste des commandes pour jouer au jeu: "yes" , "y" , "oui" , "o" , "ok" """)
            keep_playing = False
            break
    clear()

def Roulette(cash, show_numbers, clear):
    chosen_number = int(input("Choisissez le numéro sur lequel miser : \n"))

    try :
        bet = int(input("Combien d'argent souhaitez-vous miser ? \n"))
    except ValueError:
        print("Veuillez miser de l'argent pour pouvoir jouer.")
    except NameError:
        print("Veuillez miser de l'argent pour jouer au jeu.")
    else :
        if bet > cash :
           print ("Vous possédez ", cash ,". Veuillez choisir un nommbre choisi entre 0 et ", cash)
        cash -+ bet
        print("Votre solde actuel : ", cash ,"\n")

    while show_numbers < 100 :
        clear()
        random_number = randint(0,49)
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
        print("Bien joué, vous avez gagné ", earned_cash ,"euros.")
        cash += earned_cash
        print("Désormais votre solde s'estime à", cash)