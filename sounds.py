import pygame
from pygame.mixer import Sound


class Sounds:
    channels = {}
    def __init__(self):
        pygame.mixer.init()

        self.sounds = {
            'background': pygame.mixer.Sound("Sounds/background.wav"),
            'click': pygame.mixer.Sound("Sounds/click.wav"),
            'game_over': pygame.mixer.Sound("Sounds/game_over.wav"),
            'jump': pygame.mixer.Sound("Sounds/jump.wav"),
            'level_completed': pygame.mixer.Sound("Sounds/level_completed.wav"),
            'walk':  pygame.mixer.Sound("Sounds/walk.wav"),
            'collect': pygame.mixer.Sound("Sounds/collect.wav"),
            'pain':pygame.mixer.Sound("Sounds/pain.wav"),
            'robot':pygame.mixer.Sound("Sounds/robot.wav")
        }
        

    def play(self, name, loop=False, volume=1.0):
        if name in self.sounds:
            sound = self.sounds[name]
            sound.set_volume(volume)

            # Si le son doit être joué en boucle, on utilise un canal dédié
            if loop:
                if name not in Sounds.channels:  # Si le son n'est pas déjà joué sur un canal
                    Sounds.channels[name] = pygame.mixer.Channel(
                        len(Sounds.channels))  # Crée un canal unique pour chaque son en boucle
                Sounds.channels[name].play(sound, loops=-1)  # Joue le son en boucle
            else:
                pygame.mixer.Sound.play(sound)  # Jouer le son normalement
        else:
            print(f"Le son '{name}' n'existe pas.")

    def stop(self, name):
        if name in Sounds.channels:
            Sounds.channels[name].stop()  # Arrêter le canal spécifique
            del Sounds.channels[name]  # Supprimer le canal du dictionnaire
        elif name in self.sounds:
            self.sounds[name].stop()  # Arrêter un son sans canal
        else:
            print(f"Le son '{name}' n'existe pas.")

    def stop_all(self):
        for c in Sounds.channels:
            Sounds.channels[c].stop()
            del Sounds.channels[c]

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
