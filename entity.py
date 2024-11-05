from spritesheet import Spritesheet
class Entity:
    def __init__(self,MAX_SPEED: list[int] = [0, 0], vitesse: list[int] = [0, 0]):
        self.MAX_SPEED = MAX_SPEED
        self.vitesse = vitesse
        self.spritesheet = None

    def animation(self):
        pass

    def move(self):
        pass

    def animation(self):
        pass