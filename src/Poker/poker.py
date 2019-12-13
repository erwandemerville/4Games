# Importer ce fichier et appeler la fonction start pour lancer le jeu.

import importlib

def start(frame):
    import Poker.fenetre_jeu
    importlib.reload(Poker.fenetre_jeu)
    Poker.fenetre_jeu.reset(frame)