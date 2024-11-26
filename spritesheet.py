import pygame
from image import Image


class Spritesheet:
    def __init__(self, path):

        self.image = Image(path)
        self.sprite_sheet = self.image.image

    def get_frame(self, x, y, w, h):
        if not self.image.image:
            print("Erreur : La spritesheet n'est pas chargée.")
            return None
        frame = pygame.Surface((w, h), pygame.SRCALPHA)
        frame.blit(self.image.image, (0, 0), (x, y, w, h))
        frame.set_colorkey((0, 0, 0))
        return frame


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Animation Spritesheet")

    spritesheet = Spritesheet("spritesheet.png")
    spritesheet.image.load_image()

    frame_width, frame_height = 85, 128  # Taille des frames
    num_frames = 7                    # Nombre de frames dans la spritesheet
    current_frame = 0
    frame_rate = 180  # Temps entre les frames en millisecondes
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

        x = current_frame * frame_width
        y = 0
        frame = spritesheet.get_frame(x, y, frame_width, frame_height)

        screen.fill((50, 50, 50))  # Fond gris
        if frame:
            screen.blit(frame, (100, 100))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()