import pygame
import math
from game import Game
pygame.init()

# generer la fenetre du jeu
pygame.display.set_caption("StarWars Game")
screen = pygame.display.set_mode((1080, 800))

# charger l'arriere plan
background = pygame.image.load('assets/space.png')

# impoter notre banniere
banner = pygame.image.load('assets/ban.png')
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.33)
banner_rect.y = math.ceil(screen.get_height() / 4)


# importer le bouton de lancement
play_button = pygame.image.load('assets/bt.png')
play_button = pygame.transform.scale(play_button, (250, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.7)
play_button_rect.y = math.ceil(screen.get_height() / 1.8)

# charger notre jeu
game = Game()

running = True

while running:
    # appliquer la fenetre du jeu
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencer ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # verifier si le jeu n'a pas commencer
    else:
        # ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # si on ferme la fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fin du jeux")
        # detecter si le joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verificayion pour savoir si la souris est en contact av le boutton
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancé
                game.start()
