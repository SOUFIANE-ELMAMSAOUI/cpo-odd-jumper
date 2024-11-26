from collision import Collision
from entity import Entity
from objectif import Objectif
import os
import json
import pygame

class Niveau:

    def __init__(self, data_path):
        self.name = ""
        self.data_path = data_path
        self.entities = []  # Initialiser la liste des entités
        self.objectif = None
        self.colliders = []

    def load_data_level(self):
        entities_dir = os.path.join("levels_data", "Entités")

        if not os.path.isdir(entities_dir):
            print(f"Le dossier {entities_dir} n'existe pas.")
            return

        for filename in os.listdir(entities_dir):
            if filename.endswith(".json"):
                file_path = os.path.join(entities_dir, filename)

                with open(file_path, 'r') as file:
                    entity_data = json.load(file)
                entity = Entity(MAX_SPEED=entity_data["MAX_SPEED"], vitesse=entity_data["vitesse"], name = entity_data["name"], path_image = entity_data["path_image"], position = entity_data["position"])

                self.entities.append(entity)


        objectif_path = os.path.join(entities_dir, "objectif.json")
        if os.path.isfile(objectif_path):
            with open(objectif_path, 'r') as file:
                objectif_data = json.load(file)
                self.objectif = Objectif(description=objectif_data["description"], recompense=objectif_data["recompense"])

        print(f"{len(self.entities)} entités chargées avec succès.")

    def create_colliders(self):
        file = open("./levels_data/niveau_test.json", 'r')
        data = json.load(file)

        for layers in data["layers"]:
            if layers["name"] ==  "collision":
                for n, tile_value in enumerate(layers["data"]):
                    if tile_value > 0:
                        self.colliders.append(Collision([n%data["tilewidth"], int((n-n%data["tilewidth"])/data["tilewidth"])], [data["tilewidth"], data["tileheight"]]))


    def load_level(self):
        #changement des images du niveau
        #=> image du fond, images de toute les entitées
        pass

    def run(self):
        #boucle de simulation pour un niveau
        pass


if __name__ == "__main__":
    data_path = "Entités"

    niveau = Niveau(data_path)
    niveau.load_data_level()

    print(f"Nom du niveau : {niveau.name}")
    print("Entités chargées :")
    for entity in niveau.entities:
        print(f"Nom: {getattr(entity, 'name', 'N/A')}, Image: {getattr(entity, 'image', 'N/A')}, Position: {getattr(entity, 'position', 'N/A')}, "
              f"Échelle: {getattr(entity, 'scale', 'N/A')}, Taille d'image: {getattr(entity, 'image_size', 'N/A')}")

    if niveau.objectif:
        print(f"Objectif chargé à la position: {niveau.objectif.position}")
    else:
        print("Aucun objectif trouvé.")

    niveau.create_colliders()
    print(niveau.colliders)