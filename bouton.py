import pygame


class Bouton:
    def __init__(self, size=[150, 50], text_bouton="Bouton", font= None, position = [10, 10], command = 0, fenetre = None):
        self.size = size
        self.text_bouton = text_bouton
        self.button_surface = pygame.Surface(size)
        self.font = font
        self.text = self.font.render(self.text_bouton, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.button_surface.get_width() / 2, self.button_surface.get_height() / 2))
        self.button_rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.command = command
        self.fenetre = fenetre

    def animation(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.button_surface, (127, 255, 212), (1, 1, self.size[0]-2, self.size[1]-2))
        else:
            pygame.draw.rect(self.button_surface, (255, 255, 255), (1, 1, self.size[0]-2, self.size[1]-2))

        self.button_surface.blit(self.text, self.text_rect)
        self.fenetre.blit(self.button_surface, (self.button_rect.x, self.button_rect.y))






#test
if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    window_size = (500, 400)
    fenetre = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Test Bouton')
    clock.tick(60)

    font = pygame.font.Font(None, 24)

    bouton = Bouton([150, 40], "Quitter", font, fenetre= fenetre)

    loop = True
    while loop:


        # Fill the display with color
        fenetre.fill((155, 255, 155))

        # Get events from the event queue
        for event in pygame.event.get():
            # Check for the quit event
            if event.type == pygame.QUIT:
                # Quit the game
                loop = False

            # Check for the mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                if bouton.button_rect.collidepoint(event.pos):
                    loop = False

        # Check if the mouse is over the button. This will create the button hover effect
        bouton.animation()
        # Update the game state
        pygame.display.update()