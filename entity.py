import pygame

from collision import Collision
from spritesheet import Spritesheet

class Entity:
    def __init__(self,MAX_SPEED = [0, 0], vitesse= [0, 0], name = "", path_image = "default_entity.png", position= [0, 0],
                 size = [50, 50], fenetre = None,harmful = False, collect = False, talking = {"cond":False}, taker = {"cond":False}):

        self.MAX_SPEED = MAX_SPEED
        self.vitesse = vitesse
        self.spritesheet = Spritesheet(path_image)
        self.name = name
        self.collision = Collision(position, size)
        self.fenetre = fenetre

        self.harmful = harmful
        self.collect = collect

        self.talking = talking["cond"]
        self.is_talking = False
        if self.talking:
            p_temp = [position[0]-talking["range"],position[1]-talking["range"]]
            s_temp = [size[0]+talking["range"]*2,size[1]+talking["range"]*2]
            self.talking_collision = Collision(p_temp, s_temp)
            self.font = pygame.font.Font(None, 24)
            self.text = self.font.render(talking["text"], False, (0, 0, 0))

        self.take_items = taker["cond"]
        if self.take_items:
            self.wanted_items = taker["items"]

    def animation(self):
        self.spritesheet.image.draw(self.fenetre, self.collision.position)
        if self.is_talking:

            self.fenetre.blit(self.text, self.talking_collision.position)

    def move(self):
        pass
