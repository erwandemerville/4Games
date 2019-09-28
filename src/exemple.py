# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier

import tkinter
from Grille import Grille, Sudoku_Case, Loto_Case;

#instanciation de la grille
g = Grille.Grille(30, 30, 10, 10, 590, 590, Sudoku_Case);
#instanciation de tkinter
root = tkinter.Tk();
#On garde la fenêtre en global pour pouvoir accéder au canvas nécéssaire pour dessiner.
gui = None;

# Fonction appellée quand un clic de souris est détecté.
def click(event):
    #print("clic souris : ", event.x, event.y);
    g.selectCase(event.x,event.y);
    gui.canvas.delete("all");
    g.draw(gui.canvas, "#858585");

# Fonction appellée quand la souris bouge.
def hover(event):
    g.hoverCase(event.x,event.y);
    gui.canvas.delete("all");
    g.draw(gui.canvas, "#858585");

# L'application sera contenue dans un objet qui hérite de /Frame/ (un conteneur).
# Cette frame contiendra un /Canvas/ qui contiendra des objets graphique.
# On peut faire ce programme *sans* utiliser de /Frame/, mais directement le
# canvas. Cependant, si par la suite on souhaite ajouter d'autres éléments graphiques
# ce sera tout prêt...

class Fenetre(tkinter.Frame):
    def __init__(self, parent):
        # Initialiseur de la classe parente :
        super().__init__(parent);
        # Titre de l'application :
        parent.title("Example graphique Tkinter avec classe");
        # Disposition de la Frame (dans la fenêtre application). La frame va prendre toute la place
        # disponible dans la fenêtre, même si on change la taille de la fenêtre
        self.pack(fill='both', expand=1);
        # On crée un canevas  de taille 400x300 dans la Frame /self/
        self.canvas = tkinter.Canvas(self, width=600, height=600, background="#121212");
        # Le canevas est "packé" dans sa fenêtre en laissant une petite bordure de taille 8
        self.canvas.pack(padx=8, pady=8);#  Ajouter  fill='both', expand=1 pour voir...
        #self.image = None # initialisation propre d'un attribut utilisé plus loin
        # On dessine
        self.draw_board();
        # On demande à associer la callback /click/ à l'événement /<Button-1>/
        # l'événement /<Button-1>/ est l'événement représentant un clic de souris.
        self.canvas.bind("<Button-1>", click);
        self.canvas.bind("<Motion>", hover);


    def draw_board(self):

        #Guide dessiner une image avec PIL (Pillow pour python 3)

        # On charge l'image
        #self.image = ImageTk.PhotoImage(file="python.png")
        # Et on l'affichge, les coordonnées sont celles du centre (anchor="c")
        #self.canvas.create_image(128,128, image=self.image, anchor="c")

        # Attention, on ne peut pas utiliser de variable locale pour l'image car après avoir
        # donné l'ordre d'affichage /create_image/ Tk doit pouvoir continuer à disposer des données.
        # Or les variables locales sont libérées (et l'image effacée) à la sortie de la fonction
        # qui les contient. C'est pourquoi on utilise ici un attribut de classe. self.image a ainsi
        # la même durée de vie que l'objet global /gui/ (voir plus bas)
        root.update();
        g.draw(self.canvas, "#858585");

def main():
    # Création de l'application
    # Ajout des éléments graphiques
    #instanciation de la fenêtre
    global gui;
    gui = Fenetre(root);
    # Boucle des événements
    root.mainloop();

main();
