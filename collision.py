class Collision:
    def __init__(self, position=None, size=None):
        self.position = position if position else [0, 0]
        self.size = size if size else [0, 0]

    def test_collision_stat(self, c):
        # Vérification de collision statique
        if (
            self.position[0] <= c.position[0] + c.size[0]
            and self.position[0] + self.size[0] >= c.position[0]
            and self.position[1] <= c.position[1] + c.size[1]
            and self.position[1] + self.size[1] >= c.position[1]
        ):
            return True
        return False

    def test_collision_dyn(self, c, vitesse):
    # Clone de la vitesse pour éviter de modifier l'original
        v = vitesse[:]

    # Collision sur l'axe X
        if (
            self.position[1] < c.position[1] + c.size[1]
            and self.position[1] + self.size[1] > c.position[1]
        ):  # Les objets sont alignés verticalement
            if (
                self.position[0] + v[0] < c.position[0] + c.size[0]
                and self.position[0] + self.size[0] + v[0] > c.position[0]
            ):  # Collision sur l'axe X
                if v[0] > 0:  # Mouvement vers la droite
                    v[0] = c.position[0] - (self.position[0] + self.size[0])
                elif v[0] < 0:  # Mouvement vers la gauche
                    v[0] = c.position[0] + c.size[0] - self.position[0]

    # Collision sur l'axe Y
        if (
            self.position[0] < c.position[0] + c.size[0]
            and self.position[0] + self.size[0] > c.position[0]
        ):  # Les objets sont alignés horizontalement
            if (
                self.position[1] + v[1] < c.position[1] + c.size[1]
                and self.position[1] + self.size[1] + v[1] > c.position[1]
            ):  # Collision sur l'axe Y
                if v[1] > 0:  # Mouvement vers le haut
                    v[1] = c.position[1] - (self.position[1] + self.size[1])
                elif v[1] < 0:  # Mouvement vers le bas
                    v[1] = c.position[1] + c.size[1] - self.position[1]
        return v


if __name__ == "__main__":
    # Initialisation des objets
    c1 = Collision(position=[20, 40], size=[2, 2])
    c2 = Collision(position=[20, 20], size=[2, 2])

    # Définition de la vitesse initiale
    vitesse_c2 = [0,3]  # c2 se déplace vers la droite

    for step in range(10):
        print(f"\nÉtape {step + 1}:")
        print(f"Position de c1 : {c1.position}")
        print(f"Position de c2 : {c2.position}")

        # Test de collision dynamique
        v_adjusted = c2.test_collision_dyn(c1, vitesse_c2)
        print("Distance ajustée pour éviter la collision :", v_adjusted)

        # Mise à jour de la position de c2 avec la vitesse ajustée
        c2.position[0] += v_adjusted[0]
        c2.position[1] += v_adjusted[1]
