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
        p = "./levels_data/levels.json"
        file = open(p, 'r')
        l = json.load(file)

        self.niveaux = []
        for map_path in l["levels"]:
            file_map = open(map_path, "r")
            d = json.load(file_map)
            self.niveaux.append(Niveau(d["name"], d["entities_path"], d["data_path"], d["path_image_fond"], d["joueur"],self.fenetre, d["badge"],d["background_sound"]))


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

            elif self.etat >= 10000:
                n_map = round(self.etat/10000)
                sub_etat = self.etat%10000

                if sub_etat == 0:
                    #prerun du niveau
                    self.sounds.stop('background')
                    self.niveaux[n_map-1].load_data_level()
                    self.niveaux[n_map-1].create_colliders()
                    self.niveaux[n_map-1].pre_run()
                    self.etat +=1

                elif sub_etat == 1:
                    #boucle simulation du niveau
                    self.loop, self.etat = self.niveaux[n_map-1].run(dt, self.etat)

                elif sub_etat == 2:
                    #déchargement des datas du niveaux
                    self.niveaux[n_map-1].post_run()
                    self.etat +=1

                elif sub_etat == 3:
                    #récompenses
                    self.menu_badge.unlock_badge(self.niveaux[n_map-1].recompense)
                    self.etat = 0

                elif sub_etat == 4:
                    #quitté sans récompenses
                    self.niveaux[n_map - 1].post_run()
                    self.etat = 0

                elif sub_etat == 5:
                    #menu pause
                    self.loop, self.etat = self.niveaux[n_map - 1].pause(self.etat)
                    if self.etat%10000 == 0:
                        self.niveaux[n_map - 1].post_run()




            #on update l'écran avec la nouvelle frame
            pygame.display.update()

    def load_levels_data(self):
        pass