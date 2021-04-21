import curses
import time
import sys
from random import randint

class Field:
    def __init__(self, taille):
        self.taille = taille
        self.icons = {
            0: ' . ',
            1: ' ° ',
            2: ' ⚇ ',
            3: ' ֎ ',
        }
        self.serpent_coords = []
        self.generation_espace()
        self.ajout_entite()

    def ajout_entite(self):
        
        while(True):
            i = randint(0, self.taille-1)
            j = randint(0, self.taille-1)
            entite = [i, j]
            
            if entite not in self.serpent_coords:
                self.espace[i][j] = 3
                break

    def generation_espace(self):
        self.espace = [[0 for j in range(self.taille)] for i in range(self.taille)]

    def clear_espace(self):        
        self.espace = [[j if j!= 1 and j!= 2 else 0 for j in i] for i in self.espace]

    def rendu(self, screen):
        taille = self.taille
        self.clear_espace()
        for i, j in self.serpent_coords:
            self.espace[i][j] = 1
        tete = self.serpent_coords[-1]
        self.espace[tete[0]][tete[1]] = 2
        for i in range(taille):
            row = ''
            for j in range(taille):
                row += self.icons[ self.espace[i][j] ]
            screen.addstr(i, 0, row)

    def get_entite_position(self):
        for i in range(self.taille):
            for j in range(self.taille):
                if self.espace[i][j] == 3:
                    return [i, j]
        return [-1, -1]

    def si_serpent_mange_entite(self):
        entite = self.get_entite_position()
        tete = self.serpent_coords[-1]
        return entite == tete

class Snake:
    def __init__(self, name):
        self.name = name
        self.direction = curses.KEY_RIGHT
        self.coords = [[0, 0], [0, 1], [0, 2], [0, 3]]
        
    def set_direction(self, ch):
        if ch == curses.KEY_LEFT and self.direction == curses.KEY_RIGHT:
            return
        if ch == curses.KEY_RIGHT and self.direction == curses.KEY_LEFT:
            return
        if ch == curses.KEY_UP and self.direction == curses.KEY_DOWN:
            return
        if ch == curses.KEY_DOWN and self.direction == curses.KEY_UP:
            return 
        self.direction = ch

    def level_up(self):
        a = self.coords[0]
        b = self.coords[1]
        tail = a[:]
        if a[0] < b[0]:
            tail[0]-=1
        elif a[1] < b[1]:
            tail[1]-=1
        elif a[0] > b[0]:
            tail[0]+=1
        elif a[1] > b[1]:
            tail[1]+=1
        tail = self._check_limit(tail)
        self.coords.insert(0, tail)

    def is_alive(self):
        tete = self.coords[-1]
        snake_body = self.coords[:-1]
        return tete not in snake_body

    def _check_limit(self, point):
        # Check l'espace limite
        if point[0] > self.espace.taille-1:
            point[0] = 0
        elif point[0] < 0:
            point[0] = self.espace.taille-1
        elif point[1] < 0:
            point[1] = self.espace.taille-1
        elif point[1] > self.espace.taille-1:
            point[1] = 0
        return point

    def move(self):
        tete = self.coords[-1][:]
        if self.direction == curses.KEY_UP:
            tete[0]-=1
        elif self.direction == curses.KEY_DOWN:
            tete[0]+=1
        elif self.direction == curses.KEY_RIGHT:
            tete[1]+=1
        elif self.direction == curses.KEY_LEFT:
            tete[1]-=1
        tete = self._check_limit(tete)
        del(self.coords[0])
        self.coords.append(tete)
        self.espace.serpent_coords = self.coords
        if not self.is_alive():
            sys.exit()
        if self.espace.si_serpent_mange_entite():
            self.level_up()
            self.espace.ajout_entite()

    def set_espace(self, espace):
        self.espace = espace

def main(screen):
    screen.timeout(0)
    espace = Field(10)
    serpent = Snake("Joe")
    serpent.set_espace(espace)

    while(True):
        ch = screen.getch()
        if ch != -1:
            serpent.set_direction(ch)
        serpent.move()
        espace.rendu(screen)
        screen.refresh()
        time.sleep(.4)

if __name__=='__main__':
    curses.wrapper(main)