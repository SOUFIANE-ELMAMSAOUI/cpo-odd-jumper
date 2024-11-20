import json
import pygame
from bouton import Bouton

class Menu:
    def __init__(self, path, etat,  fenetre):
        self.path = path
        self.boutons = []
        self.fenetre = fenetre
        self.font = pygame.font.Font(None, 24)
        self.etat = etat


    def create_boutons(self):
        file = open(self.path, 'r')
        data = json.load(file)
        for bouton_data in data["boutons"]:
            self.boutons.append(Bouton(bouton_data["size"], bouton_data["text"], self.font, bouton_data["position"], bouton_data["command"], self.fenetre))


    def run(self):
        self.fenetre.fill((150, 150, 150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game
                return (False, -1)
            # Check for the mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                for b in self.boutons:
                    if b.button_rect.collidepoint(event.pos):
                        return (True, b.command)
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