import pygame
from image import Image


class Spritesheet:
    def __init__(self, path):

        self.image = Image(path)
        self.sprite_sheet = self.image.image

    def get_frame(self, x, y, w, h, offset_x, offset_y, mirror):
        if not self.image.image:
            print("Erreur : La spritesheet n'est pas chargée.")
            return None
        frame = pygame.Surface((w-offset_x, h-offset_y), pygame.SRCALPHA)
        frame.blit(self.image.image, (0, 0), (x*w, y*h, w, h))

        if mirror:
            frame = pygame.transform.flip(frame, True, False)
        frame.set_colorkey((0, 0, 0))
        return frame


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Animation Spritesheet")

    image = Image("image_fond_test.png")
    image.load_image()

    spritesheet = Spritesheet("Joueur.png")
    spritesheet.image.load_image()

    frame_width, frame_height = 128, 128  # Taille des frames
    num_frames = 10                   # Nombre de frames dans la spritesheet
    current_frame = 0
    frame_rate = 100  # Temps entre les frames en millisecondes
    last_update = pygame.time.get_ticks()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        now = pygame.time.get_ticks()
        if now - last_update > frame_rate:
            last_update = now
            current_frame = (current_frame + 1) % num_frames

        x = current_frame
        y = 3
        frame = spritesheet.get_frame(x, y, frame_width, frame_height, -45,-55, False)

        screen.fill((50, 50, 50))  # Fond gris
        image.draw(screen, (0,0))
        if frame:
            screen.blit(frame, (100, 100))


        pygame.display.flip()
        clock.tick(120)

    pygame.quit()