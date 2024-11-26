
from collision import Collision
from spritesheet import Spritesheet

class Joueur:
    def __init__(self, MAX_SPEED = [10, 10], vitesse = [0, 0], animation_frame = 0, jump_authorized = True, fenetre = None, spritesheet_path = ""):
        self.MAX_SPEED = MAX_SPEED
        self.vitesse = vitesse
        self.animation_frame = animation_frame
        self.jump_authorized = jump_authorized
        self.collision = Collision([200,100],[50,100])
        self.fenetre = fenetre
        self.spritesheet = Spritesheet(spritesheet_path)

    def input_handle(self):
        pass

    def move(self, map_colliders):
        v_temp = [0, 10]
        for c in map_colliders:
            print(c.position)
            v_collid = self.collision.test_collision_dyn(c, v_temp)
            if v_collid[0] < v_temp[0]:
                v_temp[0] = v_collid[0]
            if v_collid[1] < v_temp[1]:
                v_temp[1] = v_collid[1]
        self.collision.position[0] += v_temp[0]
        self.collision.position[1] += v_temp[1]

    def animation(self):
        pass

    def show(self):
        self.spritesheet.image.draw(self.fenetre, (self.collision.position))

