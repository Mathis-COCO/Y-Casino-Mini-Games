from random import randint
import os
import time

grille = []
grille1 = []

chosen_game = 'bataille navale'

def Clear(chosen_game):
    os.system('cls')
    print(f'_________________ JEU CHOISI : {chosen_game} _________________\n\n')

for x in range(6):
    grille.append(["O"] * 6)

def print_grille(grille):
    Clear(chosen_game)
    print('================')
    print()
    print('grille ennemie:')
    print("  0|1|2|3|4|5")
    for rangee in range(len(grille)):
        print(str(rangee) + "|" + "|".join(grille[rangee]))
    print()
print_grille(grille)

for x in range(6):
    grille1.append(["O"] * 6)

def print_grille1(grille1):
    print('================')
    print()
    print("  0|1|2|3|4|5")
    for rangee1 in range(len(grille1)):
        print(str(rangee1) + "|" + "|".join(grille1[rangee1]))
    print()
    print('Votre grille')
    print('================')

rangee_perso = int(input("Colonne de votre premier bateau:"))
colonne_perso = int(input("Rangée de votre premier bateau:"))

while ((rangee_perso < 0 or rangee_perso > 5) or (colonne_perso < 0 or colonne_perso > 5)):
    print("\nPlacez votre navire sur la carte.\n")
    print("Le bateau doit être placé sur des coordonnees allant de 0 à 5")
    rangee_perso = int(input("Choisissez à nouveau la colonne de votre premier bateau:"))
    colonne_perso = int(input("Choisissez à nouveau la rangée de votre premier bateau:"))

boatperso1=1

rangee_perso2 = int(input("Choisis la colonne de ton second bateau:"))
colonne_perso2 = int(input("Choisis la rangée de ton second bateau:"))

while ((rangee_perso2 < 0 or rangee_perso2 > 5) or (colonne_perso2 < 0 or colonne_perso2 > 5) or (rangee_perso2 == rangee_perso and colonne_perso2 == colonne_perso)):
    print("\nPlace ton navire sur la map, et ne le place pas sur le premier.\n")
    print("Le bateau doit être placé sur des coordonnees allant de 0 à 5")
    rangee_perso2 = int(input("Choisis à nouveau la colonne de ton second bateau:"))
    colonne_perso2 = int(input("Choisis à nouveau la rangée de ton second bateau:"))

boatperso2=1

rangee_perso3 = int(input("Choisis la colonne de ton troisième bateau:"))
colonne_perso3 = int(input("Choisis la rangée de ton troisième bateau:"))

while ((rangee_perso3 < 0 or rangee_perso3 > 5) or (colonne_perso3 < 0 or colonne_perso3 > 5) or (rangee_perso3 == rangee_perso and colonne_perso3 == colonne_perso) or (rangee_perso3 == rangee_perso2 and colonne_perso3 == colonne_perso2)):
    print("\nPlace ton navire sur la map, et ne le place pas sur un bateau déja existant.\n")
    print("Le bateau doit être placé sur des coordonnees allant de 0 à 9")
    rangee_perso3 = int(input("Choisis à nouveau la colonne de ton troisième bateau:"))
    colonne_perso3 = int(input("Choisis à nouveau la rangée de ton troisième bateau:"))

boatperso3=1

rangee_perso4 = int(input("Choisis la colonne de ton quatrième bateau:"))
colonne_perso4 = int(input("Choisis la rangée de ton quatrième bateau:"))

while ((rangee_perso4 < 0 or rangee_perso4 > 5) or (colonne_perso4 < 0 or colonne_perso4 > 5) or (rangee_perso4 == rangee_perso and colonne_perso4 == colonne_perso) or (rangee_perso4 == rangee_perso2 and colonne_perso4 == colonne_perso2) or (rangee_perso4 == rangee_perso3 and colonne_perso4 == colonne_perso3)):
    print("\nPlace ton navire sur la map, et ne le place pas sur un bateau déja existant.\n")
    print("Le bateau doit être placé sur des coordonnees allant de 0 à 5")
    rangee_perso4 = int(input("Choisis à nouveau la colonne de ton quatrième bateau:"))
    colonne_perso4 = int(input("Choisis à nouveau la rangée de ton quatrième bateau:"))

boatperso4=1

grille1[colonne_perso][rangee_perso] = "•"
grille1[colonne_perso2][rangee_perso2] = "•"
grille1[colonne_perso3][rangee_perso3] = "•"
grille1[colonne_perso4][rangee_perso4] = "•"
print()
print_grille1(grille1)
print()

def random_rangee(grille):
    return(randint(0, len(grille) - 1))

def random_colonne(grille):
    return(randint(0, len(grille[0]) - 1))

def random_rangee2(grille):
    return(randint(0, len(grille) - 1))

def random_colonne2(grille):
    return(randint(0, len(grille[0]) - 1))

def random_rangee3(grille):
    return(randint(0, len(grille) - 1))

def random_colonne3(grille):
    return(randint(0, len(grille[0]) - 1))

def random_rangee4(grille):
    return(randint(0, len(grille) - 1))

def random_colonne4(grille):
    return(randint(0, len(grille[0]) - 1))

boat_rangee = random_rangee(grille)
boat_colonne = random_colonne(grille)
boat1 = 1
boat_rangee2 = random_rangee2(grille)
boat_colonne2 = random_colonne2(grille)
boat2 = 1
boat_rangee3 = random_rangee3(grille)
boat_colonne3 = random_colonne3(grille)
boat3 = 1
boat_rangee4 = random_rangee4(grille)
boat_colonne4 = random_colonne4(grille)
boat4 = 1

infinite_mode = input("Activer le mode infini ? (oui/non): ")
infinite_mode = infinite_mode.lower()
print(infinite_mode)


if infinite_mode == 'n' or infinite_mode == "no" or infinite_mode == "non" :
    infinite_mode = False
    nbtour=int(input("Choisis le nombre de tours:"))
    while nbtour < 4 or nbtour > 100:
        print()
        print("Choisis un nombre de tours entre 4 et 100:")
        nbtour=int(input("Choisis à nouveau le nombre de tours:"))
else:
    nbtour = 99999

for tour in range(nbtour):
    print(f"Tour {tour} sur {nbtour}")
    print('=====================')
    devine_colonne = int(input("Devine la Colonne:"))
    devine_rangee = int(input("Devine la rangée:"))
    def randomrangeeIA(grille):
        return(randint(0, len(grille) - 1))

    def randomcolonneIA(grille):
        return(randint(0, len(grille[0]) - 1))

    randomrangeeIA = randomrangeeIA(grille)
    randomcolonneIA = randomcolonneIA(grille)

    if (devine_rangee == boat_rangee and devine_colonne == boat_colonne) or (devine_rangee == boat_rangee2 and devine_colonne == boat_colonne2) or (devine_rangee == boat_rangee3 and devine_colonne == boat_colonne3) or (devine_rangee == boat_rangee4 and devine_colonne == boat_colonne4):
        if devine_rangee == boat_rangee and devine_colonne == boat_colonne:
            boat1 = 0
        elif devine_rangee == boat_rangee2 and devine_colonne == boat_colonne2:
            boat2 = 0
        elif devine_rangee == boat_rangee3 and devine_colonne == boat_colonne3:
            boat3 = 0
        elif devine_rangee == boat_rangee4 and devine_colonne == boat_colonne4:
            boat4 = 0
        print('\nTu a coulé un navire ennemi!\n\nBien joué matelot')
        grille[devine_rangee][devine_colonne] = "X"
        time.sleep(3)

    if ((boat1==0) and (boat2==0) and (boat3==0) and (boat4==0)):
        print('\nFélicitations matelot, tu as coulé toute la flotte ennemie!\n')
        time.sleep(3)
        break
    else:
        if ((devine_rangee < 0 or devine_rangee > 9) or (devine_colonne < 0 or devine_colonne > 9)):
            print("\nTire dans le bon océan matelot! Tu t'es trompé d'océan")
        elif(grille[devine_rangee][devine_colonne] == "X"):
            print("\nTu as déjà choisi cet endroit, dommage.")
        else:
            grille[devine_rangee][devine_colonne] = "~"
            print("\nLoupé!")
        time.sleep(1.5)
    if (randomrangeeIA == rangee_perso and randomcolonneIA == colonne_perso) or (randomrangeeIA == rangee_perso2 and randomcolonneIA == colonne_perso2) or (randomrangeeIA == rangee_perso3 and randomcolonneIA == colonne_perso3) or (randomrangeeIA == rangee_perso4 and randomcolonneIA == colonne_perso4):
        if randomrangeeIA == rangee_perso and randomcolonneIA == colonne_perso:
            boatperso1=0
        if randomrangeeIA == rangee_perso2 and randomcolonneIA == colonne_perso2:
            boatperso2=0
        if randomrangeeIA == rangee_perso3 and randomcolonneIA == colonne_perso3:
            boatperso3=0
        if randomrangeeIA == rangee_perso4 and randomcolonneIA == colonne_perso4:
            boatperso4=0
        print("\nMince! Un de tes navires a été coulé par l'ennemi !\n")
        grille1[randomrangeeIA][randomcolonneIA] = "X"
        time.sleep(3)

    if(boatperso1==0) and (boatperso2==0) and (boatperso3==0) and (boatperso4==0):
        print("\nMince! Tous vos bateaux ont été coulés par l'ennemi\n")
        print(f'Les navires rivaux étaient en: col {random_colonne(grille)} ran {random_rangee(grille)}, en col {random_colonne2(grille)} et en ran {random_rangee2(grille)} , en col {random_colonne3(grille)} et en ran {random_rangee3(grille)} , puis en col {random_colonne4(grille)} et en ran {random_rangee4(grille)}\n')
        time.sleep(3)
        break
    else:
        if (randomrangeeIA and randomcolonneIA == "X"):
            print('\nVotre ennemi a déjà attaqué cet endroit.')
        else:
            grille1[randomrangeeIA][randomcolonneIA]="X"
            print("\nVotre ennemi ne vous a pas touché.\n")
            if tour==nbtour:
                print("PERDU, vous n'avez plus de coups.\n")
                time.sleep(1.5)
                break
        time.sleep(1.5)

        print_grille(grille)
        print_grille1(grille1)