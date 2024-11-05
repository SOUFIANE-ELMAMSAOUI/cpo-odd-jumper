import pygame
 #from joueur import Joueur

class Jeu:
    def __init__(self):
        self.etat = 0 # 0 = menu principale
        #self.joueur = Joueur([10, 10], [0, 0])
        pygame.init()


    def run(self):
        # boucle de simulation
        fenetre = pygame.display.set_mode((640, 480))
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False


    def load_levels(self):
        pass