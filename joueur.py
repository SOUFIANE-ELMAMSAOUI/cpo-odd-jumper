import time

import pygame

from collision import Collision
from spritesheet import Spritesheet


class Joueur:
    def __init__(self, MAX_SPEED = [800, 1500], WALK_SPEED = 500, vitesse = [0, 0], animation_frame = 0, falling = True, fenetre = None, spritesheet_path = ""):
        self.MAX_SPEED = MAX_SPEED
        self.WALK_SPEED = WALK_SPEED
        self.vitesse = vitesse
        self.animation_frame = animation_frame
        self.falling = falling
        self.collision = Collision([200,100],[50,100])
        self.fenetre = fenetre
        self.spritesheet = Spritesheet(spritesheet_path)
        self.last_time = None
        self.touches = None
        self.gravity = 500
        self.falling = True

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
        v_temp = [0, self.vitesse[1]]
        if self.touches[pygame.K_q]:  # Gauche
            v_temp[0] -= self.WALK_SPEED * dt
        elif self.touches[pygame.K_d]:  # Droite
            v_temp[0] += self.WALK_SPEED * dt

        if self.touches[pygame.K_SPACE] and not self.falling: #sauter
            v_temp[1] = -6*self.gravity * dt

        v_temp[1] += self.gravity * dt
        v_wanted = v_temp

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

        #autorizé le saut
        self.falling = (v_temp[1] != 0)

        #changement de la position
        self.vitesse = v_temp
        self.collision.position[0] += self.vitesse[0]
        self.collision.position[1] += self.vitesse[1]






    def animation(self):
        pass

    def show(self):
        self.spritesheet.image.draw(self.fenetre, (self.collision.position))


