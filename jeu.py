import pygame
from menu import Menu
#from joueur import Joueur

class Jeu:
    def __init__(self):
        self.etat = 0 # 0 = menu principale
        #self.joueur = Joueur([10, 10], [0, 0])
        pygame.init()

        # définir les fps du jeu
        self.window_size = (1920, 1080)
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        #créer la fenetre
        self.fenetre = pygame.display.set_mode(self.window_size, pygame.FULLSCREEN)
        pygame.display.set_caption('ODD jumper')

        #création des menus TEMPORAIRE
        self.menu_1 = Menu("./menu/menu_principal.json",0,  self.fenetre)
        self.menu_1.create_boutons()

        self.menu_niveau = Menu("./menu/menu_niveau.json", 1, self.fenetre)
        self.menu_niveau.create_boutons()

        self.menu_badge = Menu("./menu/menu_badge.json", 2, self.fenetre)
        self.menu_badge.create_boutons()

        self.loop = True


    def run(self):
        # boucle de simulation
        while self.loop:

            if self.etat == -1:
                #bouton quitté
                self.loop = False

            elif self.etat == 0:
                #menu principale
                self.loop, self.etat = self.menu_1.run()

            elif self.etat == 1:
                #menu des niveaux
                self.loop, self.etat = self.menu_niveau.run()

            elif self.etat == 2:
                #menu des badges
                self.loop, self.etat = self.menu_badge.run()


            #on update l'écran avec la nouvelle fram
            pygame.display.update()

    def load_levels_data(self):
        pass