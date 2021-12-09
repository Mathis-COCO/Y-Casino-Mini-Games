from random import randint
import os
import time
from colorama import Fore
from colorama.ansi import clear_line

grille = []
grille1 = []

chosen_game = 'bataille navale'

def Clear(chosen_game):
    os.system('cls')
    print(f'_________________ JEU CHOISI : {chosen_game} _________________\n\n')

for x in range(6):
    grille.append([Fore.BLUE+"O"+Fore.WHITE] * 6)
    grille1.append([Fore.BLUE+"O"+Fore.WHITE] * 6)

def print_grille(grille, user):
    if user == "player":
        print(("================".center(63)+"\n\n"+"\|0|1|2|3|4|5".center(63)))
        for rangee1 in range(len(grille1)):
            print('                         '+(str(rangee1) + "|" + "|".join(grille1[rangee1])))
        print("\n"+'________________'.center(63)+"\n\n"+'Votre grille'.center(63)+'\n'+'________________'.center(63))
    elif user == "ia":
        print('________________'.center(63)+'\n'+'grille ennemie:'.center(63)+'\n'+'_______________'.center(63)+'\n\n'+'\|0|1|2|3|4|5'.center(63))
        for rangee in range(len(grille)):
            print('                         '+str(rangee) + "|" + "|".join(grille[rangee]))

def Choice1(usr_choice_list, compteur):
    while True :
        empty_tab = []
        Clear(chosen_game), print_grille(grille1, "player")
        try :
            rangee_perso = int(input(f"\n                   Colonne de votre bateau {compteur}: "))
            colonne_perso = int(input(f"                   Rangée de votre bateau {compteur}: "))
            print("\n")
            empty_tab.extend((rangee_perso, colonne_perso))
            if (rangee_perso | colonne_perso) not in (0,1,2,3,4,5) or\
            ((empty_tab) in usr_choice_list) :
                print('Valeur invalide.')
                time.sleep(1.5), Clear(chosen_game)
                continues = input('\n!Help pour afficher la liste des valeurs possibles\nAppuyez sur "Entrée" pour continuer...\n')
                if continues.lower() == '!Help'.lower() :
                    if ((empty_tab) in usr_choice_list):
                        Clear(chosen_game), print (f'          La position {rangee_perso},{colonne_perso} est déjà prise.')
                        grille1[rangee_perso][colonne_perso]= Fore.RED+"•"+Fore.WHITE
                        print_grille(grille1,"player") 
                        grille1[rangee_perso][colonne_perso]= Fore.GREEN+"•"+Fore.WHITE
                        continues = input('Appuyer sur "Entrée" pour continuer...'), Clear(chosen_game)
                    else :
                        print('\nListe des valeurs: 0 , 1 , 2 , 3 , 4 , 5')
                        continues = input('Appuyer sur "Entrée" pour continuer...'), Clear(chosen_game)
                else:
                    Clear(chosen_game), Choice1(usr_choice_list, compteur)
                    break
            else:
                if len(usr_choice_list) != 4 :
                    usr_choice_list.append(empty_tab)
                    compteur +=1
                    grille1[rangee_perso][colonne_perso] = Fore.GREEN+"•"+Fore.WHITE
                    print(usr_choice_list)
                if len(usr_choice_list) >= 4 :
                    break
        except ValueError:
            print('Valeur invalide'), time.sleep(1.5), Clear(chosen_game), Choice1(usr_choice_list, compteur)

# ADD BOAT MODIFICATIONS !!!!!!!!!!!!
# print grid to show the player his boats and ask :
# "are you sure you want to keep these positions ? " -yes/no
# if yes : start the game
# else : choose boat to modify

usr_choice_list = []
Choice1(usr_choice_list, 1)
boatperso1=boatperso2=boatperso3=boatperso4=1
print_grille(grille1, "player")

ia_boats_list = []
def ChoiceIA(ia_boats_list) :
    for x in range(4):
        ia_boats = []
        random_rangee_IA = randint(0, len(grille) - 1)
        random_colonne_IA = randint(0, len(grille[0]) - 1)
        ia_boats.extend((random_rangee_IA, random_colonne_IA))
        if ia_boats not in ia_boats_list :
            ia_boats_list.append(ia_boats)
            x+=1
ChoiceIA(ia_boats_list)
print(ia_boats_list)
Clear(chosen_game)
infinite_mode = input("Activer le mode infini ? (oui/non): ").lower()
if infinite_mode == 'n' or infinite_mode == "no" or infinite_mode == "non" :
    infinite_mode = False
    while True:
        try :
            nbtour=int(input("Choisis le nombre de tours:"))
            if nbtour < 4 or nbtour > 100:
                print("\nChoisis un nombre de tours entre 4 et 100:")
                time.sleep(2.5), Clear(chosen_game)
        except ValueError:
            print("Valeur incorrecte.")
else:
    nbtour = 99999
dest_count = 0
IA_dest_count = 0

for tour in range(nbtour):
    print(f"Tour {tour} sur {nbtour}\n=====================") if infinite_mode==False else print(f"Tour {tour}")
    while True :
        try :
            if tour == 0 :
                Clear(chosen_game), print_grille(grille, "ia")
            devine_colonne = int(input("\nDevine la colonne:"))
            devine_rangee = int(input("Devine la rangée:"))
            if 0 <= (devine_rangee & devine_colonne) <= 5:
                if grille[devine_rangee][devine_colonne] != "X" :
                    if grille[devine_rangee][devine_colonne] != "~" :
                        break
            print("Valeur incorrecte.")
        except ValueError :
            print ("Valeur incorrecte.")
    player_attack = [devine_colonne, devine_rangee]

    randomrangeeIA = (randint(0, len(grille) - 1))
    randomcolonneIA = (randint(0, len(grille[0]) - 1))
    if grille1[randomrangeeIA][randomcolonneIA] != "0":
        randomrangeeIA = (randint(0, len(grille) - 1))
        randomcolonneIA = (randint(0, len(grille[0]) - 1))
    IA_attack = [randomcolonneIA, randomrangeeIA]

    if (player_attack in ia_boats_list):
        print(Fore.GREEN+'\nTu a coulé un navire ennemi!\n\nBien joué matelot'+Fore.WHITE)
        grille[devine_rangee][devine_colonne] = Fore.RED+"X"+Fore.WHITE
        dest_count += 1
        time.sleep(3)
        if (dest_count == 4):
            print(Fore.GREEN+'\nFélicitations matelot, tu as coulé toute la flotte ennemie!\n'+Fore.WHITE)
            time.sleep(3)
            break
    else:
        grille[devine_rangee][devine_colonne] = "~"
        print("\nLoupé!")
        time.sleep(1.5)
    if (IA_attack in usr_choice_list):
        print(Fore.RED+"\nMince! Un de vos navires a été coulé par l'ennemi !\n"+Fore.WHITE)
        grille1[randomrangeeIA][randomcolonneIA] = Fore.RED+"X"+Fore.WHITE
        IA_dest_count += 1
        time.sleep(3)
        if(IA_dest_count == 4):
            print(Fore.RED+"\nMince! Tous vos bateaux ont été coulés par l'ennemi\n"+Fore.WHITE)
            # turn IA boats positions on
            print_grille(grille, "ia")
            time.sleep(3)
            break
    else:
        grille1[randomrangeeIA][randomcolonneIA]="~"
        print(Fore.GREEN+"\nVotre ennemi ne vous a pas touché.\n"+Fore.WHITE)
        if tour==nbtour:
            print(Fore.RED+"PERDU, vous n'avez plus de coups.\n"+Fore.WHITE)
            time.sleep(1.5)
            break
    time.sleep(1.5)
    Clear(chosen_game)
    print_grille(grille, "ia")
    print_grille(grille1, "player")

# add hints to find ennemy boats
# add ennemy boats show after lose
# add boat modifications