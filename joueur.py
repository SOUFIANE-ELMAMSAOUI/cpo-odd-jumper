class JOUEUR:
    def __init__(self,max_speed: list[int] = [0, 0], vitesse: list[int] = [0, 0], animation_frame: int = 0, jump_authorized:bool = True):
        self.max_speed = max_speed
        self.vitesse = vitesse
        self.animation_frame = animation_frame
        self.jump_authorized = jump_authorized

    def input_handle(self):
        pass

    def move(self):
        pass

    def animation(self):
        pass

