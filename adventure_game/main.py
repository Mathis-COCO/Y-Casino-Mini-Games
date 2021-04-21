import pygame

pygame.init()                                                                   #OBLIGATOIRE

# menu avec choix de reso (modifier les bordures de la map)

# set screen
screen = pygame.display.set_mode((1920, 950))

# background
background = pygame.image.load('adventure game\img/background_marineford.png')

# Icon and title of the game
icon = pygame.image.load('adventure game\img/logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("One Piece Adventure")

# player
playerImg = pygame.image.load('adventure game\img/luffy_balloon.gif')
playerX = 20
playerY = 800
playerX_change = 0
playerY_change = 10
jump = False

def player(x,y):
    screen.blit(playerImg, (x, y))          # prend 2 paramètres: la photo du joueur et ses coordonnées

# game loop
running = True
while running:
    
    screen.fill((0, 0, 0))                              # en premier pour faire spawn le background
    screen.blit(background, (0,0))                      # add bg
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # savoir si une touche est enclenchée
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
                
    #        if event.key == pygame.K_SPACE:
    #            playerY_change = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                playerX_change = 0

        if event.type == pygame.KEYDOWN and jump == False and event.key == pygame.K_SPACE:
                jump = True

        if jump == True:
            playerY -= playerY_change
            playerY_change -= 1
            if playerY_change < -10:
                jump = False
                playerY_change = 10

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 900:
        playerX = 900
    player(playerX, playerY)                                            # on veut faire apparaître le joueur (après la map)
    pygame.display.update()                                                     # OBLIGATOIRE

# menu

# game

# game movements

# shooting

# AI
