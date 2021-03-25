from random import randint
import tkinter

grille = []
grille1 = []

for x in range(6):
    grille.append(["O"] * 6)

def print_grille(grille):
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
    print('Ta grille')
    print('================')

rangee_perso = int(input("Choisis la colonne de ton premier bateau:"))
colonne_perso = int(input("Choisis la rangée de ton premier bateau:"))

while ((rangee_perso < 0 or rangee_perso > 5) or (colonne_perso < 0 or colonne_perso > 5)):
    print()
    print("Place ton navire sur la map.")
    print()
    print("Le bateau doit être placé sur des coordonnees allant de 0 à 5")
    rangee_perso = int(input("Choisis à nouveau la colonne de ton premier bateau:"))
    colonne_perso = int(input("Choisis à nouveau la rangée de ton premier bateau:"))

boatperso1=1111

rangee_perso2 = int(input("Choisis la colonne de ton second bateau:"))
colonne_perso2 = int(input("Choisis la rangée de ton second bateau:"))

while ((rangee_perso2 < 0 or rangee_perso2 > 5) or (colonne_perso2 < 0 or colonne_perso2 > 5) or (rangee_perso2 == rangee_perso and colonne_perso2 == colonne_perso)):
    print()
    print("Place ton navire sur la map, et ne le place pas sur le premier.")
    print()
    print("Le bateau doit être placé sur des coordonnees allant de 0 à 5")
    rangee_perso2 = int(input("Choisis à nouveau la colonne de ton second bateau:"))
    colonne_perso2 = int(input("Choisis à nouveau la rangée de ton second bateau:"))

boatperso2=1111

rangee_perso3 = int(input("Choisis la colonne de ton troisième bateau:"))
colonne_perso3 = int(input("Choisis la rangée de ton troisième bateau:"))

while ((rangee_perso3 < 0 or rangee_perso3 > 5) or (colonne_perso3 < 0 or colonne_perso3 > 5) or (rangee_perso3 == rangee_perso and colonne_perso3 == colonne_perso) or (rangee_perso3 == rangee_perso2 and colonne_perso3 == colonne_perso2)):
    print()
    print("Place ton navire sur la map, et ne le place pas sur un bateau déja existant.")
    print()
    print("Le bateau doit être placé sur des coordonnees allant de 0 à 9")
    rangee_perso3 = int(input("Choisis à nouveau la colonne de ton troisième bateau:"))
    colonne_perso3 = int(input("Choisis à nouveau la rangée de ton troisième bateau:"))

boatperso3=1111

rangee_perso4 = int(input("Choisis la colonne de ton quatrième bateau:"))
colonne_perso4 = int(input("Choisis la rangée de ton quatrième bateau:"))

while ((rangee_perso4 < 0 or rangee_perso4 > 5) or (colonne_perso4 < 0 or colonne_perso4 > 5) or (rangee_perso4 == rangee_perso and colonne_perso4 == colonne_perso) or (rangee_perso4 == rangee_perso2 and colonne_perso4 == colonne_perso2) or (rangee_perso4 == rangee_perso3 and colonne_perso4 == colonne_perso3)):
    print()
    print("Place ton navire sur la map, et ne le place pas sur un bateau déja existant.")
    print()
    print("Le bateau doit être placé sur des coordonnees allant de 0 à 5")
    rangee_perso4 = int(input("Choisis à nouveau la colonne de ton quatrième bateau:"))
    colonne_perso4 = int(input("Choisis à nouveau la rangée de ton quatrième bateau:"))

boatperso4=1111

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

boat_rangee = random_rangee(grille)
boat_colonne = random_colonne(grille)

boat1 = 1111

def random_rangee2(grille):
    return(randint(0, len(grille) - 1))

def random_colonne2(grille):
    return(randint(0, len(grille[0]) - 1))

boat_rangee2 = random_rangee2(grille)
boat_colonne2 = random_colonne2(grille)

boat2 = 1111

def random_rangee3(grille):
    return(randint(0, len(grille) - 1))

def random_colonne3(grille):
    return(randint(0, len(grille[0]) - 1))

boat_rangee3 = random_rangee3(grille)
boat_colonne3 = random_colonne3(grille)

boat3 = 1111

def random_rangee4(grille):
    return(randint(0, len(grille) - 1))

def random_colonne4(grille):
    return(randint(0, len(grille[0]) - 1))

boat_rangee4 = random_rangee4(grille)
boat_colonne4 = random_colonne4(grille)

boat4 = 1111

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
    print("Tour", tour,"sur", nbtour)
    print('=====================')
    devine_colonne = int(input("Devine la Colonne:"))
    devine_rangee = int(input("Devine la rangée:"))
    def randomrangeeIA(grille):
        return(randint(0, len(grille) - 1))

    def randomcolonneIA(grille):
        return(randint(0, len(grille[0]) - 1))

    randomrangeeIA = randomrangeeIA(grille)
    randomcolonneIA = randomcolonneIA(grille)

    if devine_rangee == boat_rangee and devine_colonne == boat_colonne:
        print('\nTu a coulé un navire ennemi!\n\nBien joué matelot!')
        boat1 = 101
        grille[devine_rangee][devine_colonne] = "X"

    if devine_rangee == boat_rangee2 and devine_colonne == boat_colonne2:
        print('\nTu a coulé un navire ennemi!\n\nBien joué matelot!')
        boat2 = 101
        grille[devine_rangee][devine_colonne] = "X"

    if devine_rangee == boat_rangee3 and devine_colonne == boat_colonne3:
        print('\nTu a coulé un navire ennemi!\n\nBien joué matelot !')
        boat3 = 101
        grille[devine_rangee][devine_colonne] = "X"

    if devine_rangee == boat_rangee4 and devine_colonne == boat_colonne4:
        print('\nTu a coulé un navire ennemi!\n\nBien joué matelot')
        boat4 = 101
        grille[devine_rangee][devine_colonne] = "X"

    if ((boat1==101) and (boat2==101) and (boat3==101) and (boat4==101)):
        print('\nFélicitations matelot, tu as coulé toute la flotte ennemie!\n')
        break
    else:
        if ((devine_rangee < 0 or devine_rangee > 9) or (devine_colonne < 0 or devine_colonne > 9)):
            print()
            print("Tire dans le bon océan matelot! Tu t'es trompé d'océan")
        elif(grille[devine_rangee][devine_colonne] == "X"):
            print()
            print("Tu as déjà choisi cet endroit, dommage.")

        else:
            grille[devine_rangee][devine_colonne] = "X"
            print()
            print("Loupé!")

    if randomrangeeIA == rangee_perso and randomcolonneIA == colonne_perso:
        print ()
        print("Mince! Un de tes navires a été coulé par l'ennemi !")
        print ()
        boatperso1=101
        grille1[randomrangeeIA][randomcolonneIA] = "X"

    if randomrangeeIA == rangee_perso2 and randomcolonneIA == colonne_perso2:
        print ()
        print("Mince! Un de tes navires a été coulé par l'ennemi !")
        print ()
        boatperso2=101
        grille1[randomrangeeIA][randomcolonneIA] = "X"

    if randomrangeeIA == rangee_perso3 and randomcolonneIA == colonne_perso3:
        print ()
        print("Mince! Un de tes navires a été coulé par l'ennemi !")
        print ()
        boatperso3=101
        grille1[randomrangeeIA][randomcolonneIA] = "X"

    if randomrangeeIA == rangee_perso4 and randomcolonneIA == colonne_perso4:
        print ()
        print("Mince! Un de tes navires a été coulé par l'ennemi !")
        print ()
        boatperso4=101
        grille1[randomrangeeIA][randomcolonneIA] = "X"

    if(boatperso1==101) and (boatperso2==101) and (boatperso3==101) and (boatperso4==101):
        print()
        print("Mince! Tous tes bateaux ont été coulés par l'ennemi")
        print()
        print('Les navires rivaux étaient en: col', random_colonne(grille) ,'ran', random_rangee(grille) , ', en col', random_colonne2(grille) ,'et en ran', random_rangee2(grille) , ', en col', random_colonne3(grille) ,'et en ran', random_rangee3(grille) , ', puis en col', random_colonne4(grille) ,'et en ran', random_rangee4(grille))
        print()
        break
    else:
        if (randomrangeeIA and randomcolonneIA == "X"):
            print()
            print('Ton ennemi a déjà attaqué cet endroit.')
        else:
            grille1[randomrangeeIA][randomcolonneIA]="X"
            print()
            print("Ton ennemi ne t'a pas touché.")
            print()
            if tour==nbtour:
                print("PERDU, tu n'as plus de coups.")
                print()
                break

        print_grille(grille)
        print_grille1(grille1)