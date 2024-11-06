import json
import pygame
from bouton import Bouton

class Menu:
    def __init__(self, path, fenetre):
        self.path = path
        self.boutons = []
        self.fenetre = fenetre



    def create_boutons(self):
        file = open(self.path, 'r')
        data = json.load(file)
        for bouton_data in data["boutons"]:
            self.boutons.append(Bouton(bouton_data["size"], bouton_data["text"], font, bouton_data["position"], self.fenetre))


    def run(self):
        self.fenetre.fill((155, 255, 155))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game
                return False
            # Check for the mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                for b in menu_test.boutons:
                    if b.button_rect.collidepoint(event.pos):
                        print(b.text_bouton)
        for b in menu_test.boutons:
            b.animation()
        return True


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    window_size = (500, 400)
    fenetre = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Test Bouton')
    clock.tick(60)

    font = pygame.font.Font(None, 24)

    menu_test = Menu("./menu/menu_test.json", fenetre)
    menu_test.create_boutons()


    loop = True

    while loop:
        loop = menu_test.run()

        # Update the game state
        pygame.display.update()