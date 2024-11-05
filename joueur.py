class Joueur:
    def __init__(self,MAX_SPEED: list[int] = [0, 0], vitesse: list[int] = [0, 0], animation_frame: int = 0, jump_authorized:bool = True):
        self.MAX_SPEED = MAX_SPEED
        self.vitesse = vitesse
        self.animation_frame = animation_frame
        self.jump_authorized = jump_authorized

    def input_handle(self):
        pass

    def move(self):
        pass

    def animation(self):
        pass

