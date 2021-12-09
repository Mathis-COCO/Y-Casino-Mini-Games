import colorama
from colorama import Fore
import time
import os
colorama.init()

def Clear():
    os.system('cls')

i= 0
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.YELLOW]
while True :
    if i%8 == 1:
        print(Fore.BLUE + '+__________________________________ RGB LIGHTNING +__________________________________')
    if i%8 == 2:
        print(Fore.CYAN + '_____+_____________________________ RGB LIGHTNING _____+_____________________________')
    if i%8 == 3:
        print(Fore.GREEN + '__________+________________________ RGB LIGHTNING __________+________________________')
    if i%8 == 4:
        print(Fore.YELLOW + '_______________+___________________ RGB LIGHTNING _______________+___________________')
    if i%8 == 5: 
        print(Fore.RED + '__________________________+________ RGB LIGHTNING __________________________+________ ')
    if i%8 == 7:
        print(Fore.MAGENTA + '__________________________________+ RGB LIGHTNING __________________________________+')
    i += 1
    time.sleep(0.00001)
    print(i)
    Clear()