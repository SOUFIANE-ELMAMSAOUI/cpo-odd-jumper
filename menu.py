import json
import pygame
from bouton import Bouton
from image import Image
from sounds import Sounds

class Menu:
    def __init__(self, path, etat, fenetre):
        self.path = path
        self.boutons = []
        self.fenetre = fenetre
        self.font = pygame.font.Font(None, 24)
        self.etat = etat
        self.image = None
        self.sounds = Sounds()

    def create_data(self):
        file = open(self.path, 'r')
        data = json.load(file)
        for bouton_data in data["boutons"]:
            self.boutons.append(Bouton(bouton_data["size"], bouton_data["text"], self.font, bouton_data["position"], bouton_data["command"], self.fenetre))
        if "background" in data:
            self.image = Image(data["background"])
            self.image.load_image()

    def run(self):
        #on affiche une image si il y en a une, autrement on affiche un fond uni gris
        if self.image is not None:
            self.image.draw(self.fenetre, [0, 0])
        else:
            self.fenetre.fill((150, 150, 150))

        #vérification des event sur la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (False, -1)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for b in self.boutons:
                    if b.button_rect.collidepoint(event.pos):
                        self.sounds.play('click', loop=False, volume=1.0)
                        return (True, b.command)
        # on affiche les animation des boutons
        for b in self.boutons:
            b.animation()
        return (True, self.etat)



if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    window_size = (500, 400)
    fenetre = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Test Bouton')
    clock.tick(60)



    menu_test = Menu("./menu/menu_test.json", fenetre)
    menu_test.create_boutons()


    loop = True

    while loop:
        loop, e = menu_test.run()
        # Update the game state
        pygame.display.update()