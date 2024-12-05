from collision import Collision
from entity import Entity
from objectif import Objectif
from image import Image
from joueur import Joueur
import os
import json
import pygame


class Niveau:

    def __init__(self, name, entities_path, data_path, path_image_fond, data_joueur, fenetre):
        self.name = name
        self.entities_path = entities_path
        self.data_path = data_path
        self.entities = []  # Initialiser la liste des entités
        self.objectif = None
        self.colliders = []
        self.image_fond = Image(path_image_fond)
        self.fenetre = fenetre
        self.joueur = Joueur(fenetre=fenetre, spritesheet_path=data_joueur)

    def load_data_level(self):
        entities_dir = os.path.join("levels_data", self.entities_path)

        if not os.path.isdir(entities_dir):
            print(f"Le dossier {entities_dir} n'existe pas.")
            return

        for filename in os.listdir(entities_dir):
            if filename.endswith(".json"):
                file_path = os.path.join(entities_dir, filename)

                with open(file_path, 'r') as file:
                    entity_data = json.load(file)
                entity = Entity(
                    MAX_SPEED=entity_data["MAX_SPEED"],
                    size=entity_data["size"],
                    vitesse=entity_data["vitesse"],
                    harmful=entity_data["harmful"],
                    collect = entity_data["collect"],
                    name = entity_data["name"],
                    path_image = entity_data["path_image"],
                    position = entity_data["position"],
                    talking = entity_data["talking"],
                    fenetre=self.fenetre
                )

                self.entities.append(entity)


        objectif_path = os.path.join(entities_dir, "objectif.json")
        if os.path.isfile(objectif_path):
            with open(objectif_path, 'r') as file:
                objectif_data = json.load(file)
                self.objectif = Objectif(description=objectif_data["description"], recompense=objectif_data["recompense"])

        print(f"{len(self.entities)} entités chargées avec succès.")

    def create_colliders(self):
        file = open(self.data_path, 'r')
        data = json.load(file)

        for layers in data["layers"]:
            if layers["name"] ==  "collision":
                for n, tile_value in enumerate(layers["data"]):
                    if tile_value > 0 :
                        self.colliders.append(Collision([n%data["width"]*data["tilewidth"], int((n-n%data["width"])/data["width"])*data["tileheight"]], [data["tilewidth"], data["tileheight"]]))

    def pre_run(self):
        #charger l'image de fond
        self.image_fond.load_image()
        #charger le spritesheet du joueur
        self.joueur.spritesheet.image.load_image()
        for entity in self.entities:
            entity.spritesheet.image.load_image()



    def run(self, dt, etat):
        #boucle de simulation pour un niveau
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (False, 0)

        #game input
        self.joueur.input_handle()
        #game physique : movements etc
        self.joueur.move(self.colliders, self.entities, dt)
        #affichager des images dans le plan du fond (ex :niveau)
        self.show()
        #affichage des images dans l'avant plan (ex: joueur, entité)
        self.joueur.show()
        for entity in self.entities:
            entity.animation()


        if False: #condition fin du niveau
            return (True, etat + 1)
        return True, etat

    def show(self):
        self.image_fond.draw(self.fenetre,(0,0))





if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    pygame.display.set_caption("Test niveau")


    # test entites et colliders
    p = "./levels_data/level_test.json"
    file = open(p, 'r')
    d = json.load(file)


    niveau = Niveau(d["name"], d["entities_path"], d["data_path"], d["path_image_fond"], d["joueur"]["spritesheet"], screen)
    niveau.load_data_level()

    print(f"Nom du niveau : {niveau.name}")
    print("Entites chargées :")
    for entity in niveau.entities:
        print(f"Nom: {getattr(entity, 'name', 'N/A')}, MAX_SPEED: {getattr(entity, 'MAX_SPEED', 'N/A')}, collision: {getattr(entity, 'collision', 'N/A')}")

    if niveau.objectif:
        print(f"Objectif chargé à la position: {niveau.objectif.position}")
    else:
        print("Aucun objectif trouvé.")

    niveau.create_colliders()
    print(niveau.colliders)


    #test fenetre

    clock = pygame.time.Clock()

    niveau.pre_run()
    police = pygame.font.Font(None, 36)
    running = True
    while running:
        dt = clock.tick() / 1000
        running, etat = niveau.run(dt, 0)

        fps = int(clock.get_fps())
        texte_fps = police.render(f"FPS: {fps}", True, (255, 100, 255))
        screen.blit(texte_fps, (10, 10))

        pygame.display.flip()

