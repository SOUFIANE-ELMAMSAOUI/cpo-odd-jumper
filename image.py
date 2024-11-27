import pygame
import os

class Image:
    def __init__(self, path):
        self.path = path
        self.image = None                    #pygame.image.load(path)

    def load_image(self):
            self.path = os.path.join("Image",self.path)
            try:
                self.image = pygame.image.load(self.path).convert()
                print(f"Image chargée depuis : {self.path}")
            except pygame.error as e:
                print(f"Erreur lors du chargement de l'image : {self.path} - {e}")

    def unload_image(self):
            if self.image:
                print(f"Image déchargée : {self.path}")
                self.image = None
            else:
                print("Aucune image à décharger.")

    def draw(self, surface, position):
            if self.image:
                surface.blit(self.image, position)
            else:
                print("Aucune image chargée à afficher.")

if __name__ == "__main__":
    pygame.init()


    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Gestion des images avec Pygame")


    image = Image("img.png")
    image2 = Image("img_1.png")


    image.load_image()
    image2.load_image()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((50, 50, 50))  # Fond gris foncé


        image.draw(screen, (0, 0))
        image2 .draw(screen, (50, 50))


        pygame.display.flip()

    image.unload_image()
    image2.unload_image()

    pygame.quit()