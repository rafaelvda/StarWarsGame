import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.image = pygame.image.load('assets/st.png')
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_rect()
        self.rect.x = 1080 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 2)

    def dammage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1080 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement ne se fait que si il n'y a pas de collision avec un
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity # va se deplacer de droite à gauche
        # si le monstre est en collision av un joueur
        else:
            # infliger des degats au joueur
            self.game.player.damage(self.attack)