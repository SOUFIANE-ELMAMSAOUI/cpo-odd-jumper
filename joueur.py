import pygame
from pygame import K_SPACE

from collision import Collision
from spritesheet import Spritesheet
from sounds import Sounds


class Joueur:
    def __init__(self, MAX_SPEED=[650, 1500], WALK_SPEED=1200, animation_frame=0, fenetre=None, spritesheet_path="",
                 position=[200, 100]):
        self.MAX_SPEED = MAX_SPEED
        self.WALK_SPEED = WALK_SPEED

        self.fenetre = fenetre
        self.spritesheet = Spritesheet(spritesheet_path)
        self.position_init = position
        # attribus pour les déplacements/mouvements
        self.last_time = None  # pour calcule de dt
        self.collision = Collision(position, [32, 70])
        self.gravity = 2000
        self.acceleration = [0, self.gravity]
        self.velocity = [0, 0]
        self.touches = pygame.key.get_pressed()
        self.jump_authorized = False
        self.sounds = Sounds()

        self.items = []

        self.direction = 0
        self.animation = 0
        self.current_frame = 0
        self.n_frames = [7, 13, 10, 10, 10, 10]
        self.animation_times = [200, 90, 90, 90, 170]
        self.last_frame = 0
        self.frame = None
        self.off = 0

    def input_handle(self):
        self.touches = pygame.key.get_pressed()

    def move(self, map_colliders, entities, dt):
        # calcule des déplacements
        v_temp = [0, 0]
        is_moving = False
        is_jumping = False
        # calcule pour x
        if self.touches[pygame.K_q]:
            self.acceleration[0] = -self.WALK_SPEED
            self.direction = 1
            is_moving = True

        elif self.touches[pygame.K_d]:
            self.acceleration[0] = self.WALK_SPEED
            is_moving = True
            self.direction = 0
        else:
            is_moving = False
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

        # calcule pour y
        self.velocity[1] += self.acceleration[1] * dt
        if self.MAX_SPEED[1] < self.velocity[1]:
            self.velocity[1] = self.MAX_SPEED[1]

            # saut
        if self.touches[K_SPACE] and self.jump_authorized:
            self.velocity[1] -= 1000
            #self.sounds.stop('walk')
            self.sounds.play('jump')
            is_jumping = True



        v_temp[1] += self.velocity[1] * dt + (self.acceleration[1] * .5) * (dt * dt)

        # calule des collisions avec la map puis les entitées
        for c in map_colliders:
            v_collid = self.collision.test_collision_dyn(c, v_temp)
            if v_collid[0] < v_temp[0]:
                v_temp[0] = v_collid[0]
            if v_collid[1] < v_temp[1]:
                v_temp[1] = v_collid[1]
            if v_temp == [0, 0]:
                break

        # autorizé le saut

        self.jump_authorized = (v_temp[1] == 0 and self.velocity[1] > 0)
        if v_temp[1] == 0:
            self.velocity[1] = 0
        if v_temp[0] == 0:
            self.velocity[0] = 0
        # changement de la position

        self.collision.position[0] += v_temp[0]
        self.collision.position[1] += v_temp[1]

        if is_moving and v_temp[0] != 0 and self.jump_authorized:
            self.sounds.play('walk',loop=True,volume=0.7)
        else:
            self.sounds.stop('walk')


        n_entities_poped = 0
        for n, entity in enumerate(entities):
            if entity.harmful:
                if entity.collision.test_collision_stat(self.collision):
                    self.collision.position = self.position_init[:]
                    self.velocity = [0, 0]
                    #self.sounds.stop('walk')
                    self.sounds.play('pain')
            if entity.collect:
                if self.touches[pygame.K_e]:
                    if entity.collision.test_collision_stat(self.collision):
                        self.items.append(entity.name)
                        entities.pop(n - n_entities_poped)
                        n_entities_poped += 1
                        self.sounds.play('collect')
            if entity.talking:
                if entity.talking_collision.test_collision_stat(self.collision):
                    entity.is_talking =True
                    self.sounds.play('robot',loop=False,volume=0.2)
                else:
                    entity.is_talking =False
                    self.sounds.stop('robot')



            if entity.take_items:
                if self.touches[pygame.K_e]:
                    if entity.collision.test_collision_stat(self.collision):
                        for item in entity.wanted_items[:]:
                            if item in self.items:
                                entity.wanted_items.remove(item)
                                self.items.remove(item)

    def anim(self):
        if self.direction:
            self.off = 10
        else:
            self.off = 0

        if self.velocity[1] < 0:
            # animation saute (monté) ligne 4
            if self.animation != 4:
                self.animation = 4
            self.current_frame = 2

        elif self.velocity[1] > 0:
            if self.animation !=4:
                self.animation = 4
                self.current_frame = 3
            if self.current_frame > 5:
                self.current_frame = 5
            elif self.current_frame < 3:
                self.current_frame = 3

        elif self.velocity[0] == 0 and self.velocity[1] == 0:
            #animation idle ligne 0
            if self.animation != 0:
                self.animation = 0
                self.current_frame = 0


        elif self.velocity[0] != 0 and self.velocity[1] == 0:
            #animation run ligne 3
            if self.animation != 3:
                self.animation = 3
                self.current_frame = 0






        self.frame = self.spritesheet.get_frame(self.current_frame, self.animation, 128, 128, 0, 0, self.direction)


        time = pygame.time.get_ticks()
        if self.last_frame + self.animation_times[self.animation] < time:
            self.last_frame = time
            self.current_frame = (self.current_frame + 1) % self.n_frames[self.animation]



    def show(self):
        #pygame.draw.rect(self.fenetre, (255, 0, 0), pygame.Rect(self.collision.position[0], self.collision.position[1], self.collision.size[0], self.collision.size[1]))
        self.fenetre.blit(self.frame, (self.collision.position[0] - 44 - self.off, self.collision.position[1] - 56))


