from jeu import Jeu
import os

if __name__ == "__main__":

    if os.name == "nt":
        import ctypes
        ctypes.windll.user32.SetProcessDPIAware()

    jeu = Jeu()
    jeu.run()
