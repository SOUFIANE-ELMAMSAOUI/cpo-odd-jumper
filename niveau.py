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

                max_speed = entity_data.get("MAX_SPEED", [0, 0])
                vitesse = entity_data.get("vitesse", [0, 0])
                entity = Entity(MAX_SPEED=max_speed, vitesse=vitesse)


                entity.name = entity_data["name"]
                entity.image = entity_data["image"]
                entity.position = entity_data["position"]
                entity.scale = entity_data["scale"]
                entity.image_size = entity_data["image_size"]

                self.entities.append(entity)


        objectif_path = os.path.join(entities_dir, "objectif.json")
        if os.path.isfile(objectif_path):
            with open(objectif_path, 'r') as file:
                objectif_data = json.load(file)
                position = objectif_data.get("position", [0, 0])
                self.objectif = Objectif(position=position)

        print(f"{len(self.entities)} entités chargées avec succès.")


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
