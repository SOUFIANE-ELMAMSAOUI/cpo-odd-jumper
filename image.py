import pygame


class Image:
    def __init__(self, path):
        self.path = path
        self.image = pygame.image.load(path)