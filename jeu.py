import json

import pygame
from menu import Menu
from niveau import Niveau
from sounds import Sounds

class Jeu:
    def __init__(self):
        self.etat = 0 # liste des état dans le fichier ./menu/info_etat.txt
        #self.joueur = Joueur([10, 10], [0, 0])
        pygame.init()

        # définir les paramètre de la fenetre
        self.window_size = (1920, 1080)
        self.clock = pygame.time.Clock()


        #créer la fenetre
        self.fenetre = pygame.display.set_mode(self.window_size, pygame.FULLSCREEN)
        pygame.display.set_caption('ODD jumper')

        #création des menus TEMPORAIRE
        self.menu_1 = Menu("./menu/menu_principal.json",0,  self.fenetre)
        self.menu_1.create_data()

        self.menu_niveau = Menu("./menu/menu_niveau.json", 1, self.fenetre)
        self.menu_niveau.create_data()

        self.menu_badge = Menu("./menu/menu_badge.json", 2, self.fenetre)
        self.menu_badge.create_data()

        #créer niveau TEMPORAIRE
        p = "./levels_data/level_test.json"
        file = open(p, 'r')
        d = json.load(file)

        self.niveau0 = Niveau(d["name"], d["entities_path"], d["data_path"], d["path_image_fond"], d["joueur"]["spritesheet"],self.fenetre)


        self.loop = True
        self.sounds = Sounds()


    def run(self):
        # boucle de simulation
        while self.loop:
            dt = self.clock.tick() / 1000

            if self.etat == -1:
                #quitté
                self.loop = False

            elif self.etat == 0:
                #menu principale
                if not pygame.mixer.get_busy():
                    self.sounds.play('background', loop=True, volume=0.3)

                self.loop, self.etat = self.menu_1.run()

            elif self.etat == 1:
                #menu des niveaux
                if not pygame.mixer.get_busy():
                    self.sounds.play('background', loop=True, volume=0.3)

                self.loop, self.etat = self.menu_niveau.run()

            elif self.etat == 2:
                #menu des badges
                if not pygame.mixer.get_busy():
                    self.sounds.play('background', loop=True, volume=0.3)

                self.loop, self.etat = self.menu_badge.run()


            elif self.etat == 10000:
                #prerun niveau 0
                self.sounds.stop('background')
                self.niveau0.load_data_level()
                self.niveau0.create_colliders()
                self.niveau0.pre_run()
                self.etat = 10001

            elif self.etat == 10001:
                #boucle pour le niveau
                self.loop, self.etat = self.niveau0.run(dt, self.etat)

            elif self.etat == 10002:
                #décharger les images du niveau
                self.niveau0.post_run()
                self.etat = 0

            elif self.etat == 10003:
                #afficher le résultat
                pass




            #on update l'écran avec la nouvelle frame
            pygame.display.update()

    def load_levels_data(self):
        pass