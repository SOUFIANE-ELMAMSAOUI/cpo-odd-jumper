from collision import Collision
from spritesheet import Spritesheet

class Entity:
    def __init__(self,MAX_SPEED = [0, 0], vitesse= [0, 0], name = "", path_image = "", position= [0, 0], size = [0, 0],fenetre = None):
        self.MAX_SPEED = MAX_SPEED
        self.vitesse = vitesse
        self.spritesheet = Spritesheet(path_image)
        self.name = name
        self.collision = Collision(position, size)
        self.fenetre = fenetre

    def animation(self):
        self.spritesheet.image.draw(self.fenetre, self.collision.position)

    def move(self):
        pass