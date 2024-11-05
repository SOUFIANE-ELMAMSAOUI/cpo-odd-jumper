from entity import Entity
from objectif import Objectif
class Niveau:

    def __init__(self, data_path):
        self.name = ""
        self.data_path = data_path
        self.entity = Entity([8,7],[0,0])
        self.objectif = None

    def load_data_level(self):
        #charge toute les donées du niveau par rapport a son fichier
        pass