import pygame
from pygame import K_SPACE
import copy
from collision import Collision
from spritesheet import Spritesheet


class Joueur:
    def __init__(self, MAX_SPEED = [1000, 1500], WALK_SPEED = 1200, animation_frame = 0, fenetre = None, spritesheet_path = "",position = [200,100],position_init =[200,100]):
        self.MAX_SPEED = MAX_SPEED
        self.WALK_SPEED = WALK_SPEED
        self.animation_frame = animation_frame

        self.fenetre = fenetre
        self.spritesheet = Spritesheet(spritesheet_path)
        self.position_init = position_init
        #attribus pour les déplacements/mouvements
        self.last_time = None #pour calcule de dt
        self.collision = Collision( position, [50, 100])
        self.gravity = 2000
        self.friction = -0.1
        self.acceleration = [0, self.gravity]
        self.velocity = [0, 0]
        self.touches = pygame.key.get_pressed()
        self.jump_authorized = False



        self.items = []


    def input_handle(self):
        self.touches = pygame.key.get_pressed()


    def move(self, map_colliders, entities, dt):
        #calcule des déplacements
        v_temp = [0,0]

        #calcule pour x
        if self.touches[pygame.K_q]:
            self.acceleration[0] = -self.WALK_SPEED
        elif self.touches[pygame.K_d]:
            self.acceleration[0] = self.WALK_SPEED
        else:
            self.acceleration[0] = 0
            self.velocity[0] = 0
        if (self.velocity[0] < 0 < self.acceleration[0]) or (self.velocity[0] > 0 > self.acceleration[0]):
            self.velocity[0] = 0

        self.velocity[0] += self.acceleration[0] * dt


        if self.MAX_SPEED[0] < self.velocity[0]:
            self.velocity[0] = self.MAX_SPEED[0]
        elif -self.MAX_SPEED[0] > self.velocity[0]:
            self.velocity[0] = -self.MAX_SPEED[0]

        v_temp[0] += self.velocity[0] * dt + (self.acceleration[0] * 0.5) * (dt * dt)

        #calcule pour y
        self.velocity[1] += self.acceleration[1] * dt
        if self.MAX_SPEED[1] < self.velocity[1]:
            self.velocity[1] = self.MAX_SPEED[1]

            #saut
        if self.touches[K_SPACE] and self.jump_authorized:
            self.velocity[1]-=1000

        v_temp[1] += self.velocity[1] * dt + (self.acceleration[1] * .5) * (dt * dt)


        #calule des collisions avec la map puis les entitées
        for c in map_colliders:
            v_collid = self.collision.test_collision_dyn(c, v_temp)
            if v_collid[0] < v_temp[0]:
                v_temp[0] = v_collid[0]
            if v_collid[1] < v_temp[1]:
                v_temp[1] = v_collid[1]
            if v_temp == [0,0]:
                break
            

        #autorizé le saut

        self.jump_authorized = (v_temp[1] == 0 and self.velocity[1] >0)
        if v_temp[1] == 0:
            self.velocity[1]=0
        if v_temp[0] == 0:
            self.velocity[0] = 0
        #changement de la position

        self.collision.position[0] += v_temp[0]
        self.collision.position[1] += v_temp[1]

        for n,entity in enumerate(entities) :
            if entity.harmful:
                if entity.collision.test_collision_stat(self.collision):
                    print("Collision avec l'entite",entity)
                    self.collision.position =  copy.deepcopy(self.position_init)
            if self.touches[pygame.K_e] :
                if entity.collect : 
                    if entity.collision.test_collision_stat(self.collision) :
                        self.items.append(entity.name)
                        entities.pop(n)
                        #print("liste entities :", entities, "\nliste items :", self.items)


    def show(self):
        self.spritesheet.image.draw(self.fenetre, self.collision.position)


