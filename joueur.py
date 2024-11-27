import time

import pygame

from collision import Collision
from spritesheet import Spritesheet


class Joueur:
    def __init__(self, MAX_SPEED = [400, 400], WALK_SPEED = 200, vitesse = [0, 0], animation_frame = 0, jump_authorized = True, fenetre = None, spritesheet_path = ""):
        self.MAX_SPEED = MAX_SPEED
        self.WALK_SPEED = WALK_SPEED
        self.vitesse = vitesse
        self.animation_frame = animation_frame
        self.jump_authorized = jump_authorized
        self.jumping = False
        self.collision = Collision([200,100],[50,100])
        self.fenetre = fenetre
        self.spritesheet = Spritesheet(spritesheet_path)
        self.last_time = None
        self.touches = None

    def input_handle(self):
        self.touches = pygame.key.get_pressed()

    def move(self, map_colliders):
        #calcule du delta time
        t = time.time()
        if self.last_time == None:
            dt = 0
            self.last_time = t
        else:
            dt = t - self.last_time
            self.last_time = t

        #calcule des déplacements
        v_temp = [0, 100]
        if self.touches[pygame.K_q]:  # Gauche
            v_temp[0] -= self.WALK_SPEED * dt
        elif self.touches[pygame.K_d]:  # Droite
            v_temp[0] += self.WALK_SPEED * dt


        #limité la vitesse max
        if self.MAX_SPEED[0]*dt < v_temp[0]:
            v_temp[0] = self.MAX_SPEED[0]*dt
        if self.MAX_SPEED[1]*dt < v_temp[1]:
            v_temp[1] = self.MAX_SPEED[1]*dt

        #calule des collisions avec la map puis les entitées
        for c in map_colliders:
            v_collid = self.collision.test_collision_dyn(c, v_temp)
            if v_collid[0] < v_temp[0]:
                v_temp[0] = v_collid[0]
            if v_collid[1] < v_temp[1]:
                v_temp[1] = v_collid[1]

        #changement de la position
        self.collision.position[0] += v_temp[0]
        self.collision.position[1] += v_temp[1]

    def animation(self):
        pass

    def show(self):
        self.spritesheet.image.draw(self.fenetre, (self.collision.position))


