import pygame

class Sounds:
    def __init__(self):
        pygame.mixer.init()

        self.sounds = {
            'background': pygame.mixer.Sound("Sounds/background.wav"),
            'click': pygame.mixer.Sound("Sounds/click.wav"),
            'game_over': pygame.mixer.Sound("Sounds/game_over.wav"),
            'jump': pygame.mixer.Sound("Sounds/jump.wav"),
            'level_completed': pygame.mixer.Sound("Sounds/level_completed.wav")
        }

    def play(self, name, loop=False, volume=1.0):
        sound = self.sounds.get(name)
        if sound:
            sound.set_volume(volume)
            if loop:
                sound.play(loops=-1)
            else:
                sound.play()
        else:
            print(f"Le son '{name}' n'existe pas.")

    def stop(self, name):
        sound = self.sounds.get(name)
        if sound:
            sound.stop()
        else:
            print(f"Le son '{name}' n'existe pas.")

if __name__ == "__main__":
    pygame.init()
    sounds = Sounds()

    sounds.play('background', loop=True, volume=0.5)
    sounds.play('click')
    pygame.time.delay(5000)

    sounds.play('click')
    pygame.time.delay(1000)
    sounds.stop('click')
    pygame.time.delay(1000)



    pygame.quit()
