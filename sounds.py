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
            'walk': pygame.mixer.Sound("Sounds/walk.wav"),
            'collect': pygame.mixer.Sound("Sounds/collect.wav"),
            'pain': pygame.mixer.Sound("Sounds/pain.wav"),
            'robot': pygame.mixer.Sound("Sounds/robot.wav"),
            'industry':pygame.mixer.Sound("Sounds/industry.wav"),
            'nature':pygame.mixer.Sound("Sounds/nature.wav"),
            'forest':pygame.mixer.Sound("Sounds/forest.wav")
        }

    def play(self, name, loop=False, volume=1.0):
        if name in self.sounds:
            sound = self.sounds[name]
            sound.set_volume(volume)

            # Check if the sound is looping
            if loop:
                if name not in Sounds.channels:  # If the sound is not already on a channel
                    # Create a new channel for looping sound if it doesn't exist
                    available_channel = pygame.mixer.find_channel()
                    if available_channel:  # If there is an available channel
                        Sounds.channels[name] = available_channel
                        available_channel.play(sound, loops=-1)
            else:
                # Play non-looping sounds on available channels
                available_channel = pygame.mixer.find_channel()
                if available_channel:  # If there is an available channel
                    available_channel.play(sound)
        else:
            print(f"Le son '{name}' n'existe pas.")

    def stop(self, name):
        if name in Sounds.channels:
            Sounds.channels[name].stop()  # Stop the specific channel
            del Sounds.channels[name]  # Remove the channel from the dictionary
        elif name in self.sounds:
            self.sounds[name].stop()  # Stop a non-looping sound
        else:
            print(f"Le son '{name}' n'existe pas.")

    def stop_all(self):
        for c in Sounds.channels:
            Sounds.channels[c].stop()  # Stop all looping sounds
        pygame.mixer.stop()  # Stop all sounds


if __name__ == "__main__":
    pygame.init()
    sounds = Sounds()

    sounds.play('background', loop=True, volume=0.5)  # Play background sound in loop
    sounds.play('click', loop=False, volume=1.0)  # Play click sound
    pygame.time.delay(5000)

    sounds.play('click', loop=False, volume=1.0)  # Play click again
    pygame.time.delay(1000)
    sounds.stop('click')  # Stop click sound after 1 second
    pygame.time.delay(1000)

    sounds.stop_all()  # Stop all sounds before quitting
    pygame.quit()
