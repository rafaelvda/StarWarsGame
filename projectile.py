import pygame

# definir la classe pour le projectile
class Projectile(pygame.sprite.Sprite):
    # constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 7
        self.player = player
        self.image = pygame.image.load('assets/laser.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0


    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
        self.rect.x += self.velocity

        # verifier si le projectile entre en collision av un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supp le projectile
            self.remove()
            # infliger des degats
            monster.dammage(self.player.attack)

        # verifier si notre projectile n'est plus present sut l'ecran
        if self.rect.x > 1080:
            # supprimer le projectile (en dehors de l'ecran)
            self.remove()


