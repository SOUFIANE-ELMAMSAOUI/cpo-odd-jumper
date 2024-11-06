import pygame
 #from joueur import Joueur

class Jeu:
    def __init__(self):
        self.etat = 0 # 0 = menu principale
        #self.joueur = Joueur([10, 10], [0, 0])
        pygame.init()

        # définir les fps du jeu
        self.window_size = (1920, 1280)
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        #créer la fenetre
        self.fenetre = pygame.display.set_mode(self.window_size, pygame.FULLSCREEN)
        pygame.display.set_caption('ODD jumper')

        self.loop = True


    def run(self):
        # boucle de simulation
        while self.loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False

            if self.etat == 0:
                #menu
                self.main_menu()

    def main_menu(self):
        pass

    def load_levels(self):
        pass