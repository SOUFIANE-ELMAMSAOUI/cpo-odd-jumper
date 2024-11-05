from joueur import Joueur

class jeu:
    def __init__(self):
        self.etat = 0 # 0 = menu principale
        self.joueur = Joueur([10, 10], [0, 0])
