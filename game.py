from player import Player
from monster import Monster
import pygame

# creer une classe pour le jeu
class Game:
    def __init__(self):
        # definir si le jeu a commencer ou non
        self.is_playing = False
        #generer un joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remettre le jeu a neuf
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image du joueur sur la fenetre
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectile:
            projectile.move()

        # recuperer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectile.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        # verifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1080:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        if self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.width < 800:
            self.player.move_up()
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_down()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
