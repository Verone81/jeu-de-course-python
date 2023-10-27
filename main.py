import pygame
import random
import time

pygame.init()

# largeur et hauteur de la fenetre
largeur = 400
hauteur = 600

# position et dimension de l'ato du joueur
xx_auto = 240
yy_auto = 500
largeur_auto = 45
hauteur_auto = 75
mouvement_xx_auto = 0

# points et game over quand le joueur passe un obstacle
points = 0
font = pygame.font.Font(None, 30)
score = font.render("0 points", 1, (255, 0, 0))
fin_partie= font.render("Game Over", 1, (255, 0, 0))

# couleur du fond
couleur_fond = (255, 255, 255)

# dimension de la fenetre du jeu
fenetre = pygame.display.set_mode((largeur, hauteur))

# image du fond du jeu: la route et de l'auto du joeur
image_fond = pygame.image.load("images/route.png")
image_auto = pygame.image.load("images/auto.png")


# variable obstacle hasard
xx_obstacle = random.choice([125, 240])
yy_obstacle = 0
vitesse_obstacle = 5

# image des obstacle
mes_obstacles = ["images/auto_jaune.png", "images/auto_bleu.png", "images/auto_verte.png"]
image_obstacle = random.choice(mes_obstacles)
obstacle = pygame.image.load(image_obstacle)


# dimension de l'image du fond qui prend tout l'espace disponible
image_fond = pygame.transform.scale(image_fond, (largeur, hauteur))
# dimension de l'image auto
image_auto = pygame.transform.scale(image_auto, (largeur_auto, hauteur_auto))

# liste de mes obstacle
rect_image_auto = image_auto.get_rect()
rect_obstacle = obstacle.get_rect()


def game_over():
    fenetre.fill(couleur_fond)
    fenetre.blit(fin_partie, (largeur/2 - 100, hauteur/2))
    pygame.display.update()
    time.sleep(2)
    exit()


# la boucle du jeu
while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_RIGHT:
                mouvement_xx_auto = 3

        elif event.type == pygame.KEYUP:
            mouvement_xx_auto = -3

    if xx_auto < 50 or xx_auto > largeur - 50:
        exit()

    fenetre.fill(couleur_fond)
    fenetre.blit(image_fond, (0, 0))
    fenetre.blit(image_auto, (xx_auto, yy_auto))
    fenetre.blit(obstacle, (xx_obstacle, yy_obstacle))
    fenetre.blit(score, (10, 40))
    # on reintilise le defilement des vehicule en haut de la page
    if yy_obstacle > hauteur:
        image_obstacle = random.choice(mes_obstacles)
        obstacle = pygame.image.load(image_obstacle)
        xx_obstacle = random.choice([125, 240])
        yy_obstacle = 0
        points += 1
        score = font.render(str(points) + "points", 1, (255, 0, 0))

    # les boites de coolision
    rect_image_auto.topleft = (xx_auto, yy_auto)
    rect_obstacle.topleft = (xx_obstacle, yy_obstacle)

    # codition pour detecter les collision
    if rect_image_auto.colliderect(rect_obstacle):
        game_over()

    yy_obstacle += vitesse_obstacle
    xx_auto += mouvement_xx_auto
    pygame.display.update()