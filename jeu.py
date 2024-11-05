from joueur import Joueur

class Jeu:
    def __init__(self):
        self.etat = 0 # 0 = menu principale
        self.joueur = Joueur([10, 10], [0, 0])


    def run(self):
        pass

    def load_levels(self):
        pass