import pickle
import pygame

class Classement:
    "Classe de base gérant les classements"

    # Constructeur de la classe Classement
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # names : tableau contenant les noms des différentes variables du classement , ex : ["Profil", "Temps", "Erreurs"]
    #
    # ARGUMENTS OPTIONNELS :
    #
    # drawCoords : tableau indiquant la répartition des variables du classement, doit être de taille = len(names)-1
    #
    # Si drawCoords est non spécifié, alors les variables du classement seront réparties équitablement
    #
    def __init__(self, names, drawCoords=[]):
        self.names = names
        self.values = []
        self.drawCoords = drawCoords
        if self.drawCoords == []:
            l = len(self.names)
            l2 = 1.0/l
            for i in range(0, l):
                self.drawCoords.append(l2+l2*i)

    # Fonction save
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # filepath : emplacement relatif du fichier ou sauvegarder le classement
    #
    # Fonction permettant de sauvegarder le classement
    #
    def save(self, filepath):
        try:
            with open(filepath, 'wb') as fichier:
                mon_pickler = pickle.Pickler(fichier)
                mon_pickler.dump(self.values)
                fichier.close()
        except FileNotFoundError:
            return 0
        else:
            return 1

    # Fonction load
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # filepath : emplacement relatif du fichier depuis lequel charger le classement
    #
    # Fonction permettant de charger un classement
    #
    def load(self, filepath):
        try:
            with open(filepath, 'rb') as fichier:
                mon_depickler = pickle.Unpickler(fichier)
                self.values = mon_depickler.load()
                fichier.close()
        except FileNotFoundError:
            return False
        else:
            if self.values == None:
                self.values = []
                return False
            else:
                return len(self.values) > 0

    # Fonction draw
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # frame : instance de la fenêtre
    # start : n° du classement a partir duquel dessiner
    # end : n° du classement ou on arrête de dessiner
    # rect : rectangle dans lequel dessiner le classement, doit être sous la forme (x, y, width, height)
    #
    # ARGUMENTS OPTIONNELS :
    #
    # values : variables du classement a dessiner, si laissé vide : toutes les variables seront dessinées
    #
    # Fonction servant a dessiner le classement
    #
    def draw(self, frame, start, end, rect, values=[]):
        if values == []:
            values = self.values

        nb = abs(end-start)
        h = round(rect[3]/nb)

        police = pygame.font.SysFont("Impact",h)
        frame.blit(police.render(self.names[0], True, (255, 255, 255)), (rect[0], rect[1]))
        for i in range(1, len(self.names)):
            frame.blit(police.render(self.names[i], True, (255, 255, 255)), (rect[0]+rect[2]*self.drawCoords[i-1], rect[1]))
        for i in range(0, nb):
            v = start+i
            if len(values) > v :
                frame.blit(police.render(values[v][0], True, (255, 255, 255)), (rect[0], rect[1]+((i+1)*h)))
                for j in range(1, len(values[v])):
                    frame.blit(police.render(str(values[v][j]), True, (255, 255, 255)), (rect[0]+rect[2]*self.drawCoords[j-1], rect[1]+((i+1)*h)))
            else:
                frame.blit(police.render("-----------", True, (255, 255, 255)), (rect[0], rect[1]+((i+1)*h)))
                for j in range(1, len(self.names)):
                    frame.blit(police.render("------", True, (255, 255, 255)), (rect[0]+rect[2]*self.drawCoords[j-1], rect[1]+((i+1)*h)))

        pass

    # Fonction sort
    #
    # self : instance de la classe, ne doit pas être mis en argument
    # sortingFunc : fonction qui servira a trier le classement, si l'appel retourne True alors on interverti
    # les les valeurs
    #
    # Fonction servant a trier le classement via une fonction externe
    #
    def sort(self, sortingFunc):
        reTurn = True
        while reTurn:
            reTurn = False
            for i in range(0, len(self.values)-1):
                if sortingFunc([self.values[i][1], self.values[i+1][1], self.values[i][2], self.values[i+1][2]]):
                    temp = self.values[i]
                    self.values[i] = self.values[i+1]
                    self.values[i+1] = temp
                    reTurn = True

    # Fonction ajouterScore
    #
    # self : instance de la classe, ne doit pas être mis en argument
    # valueObj : score a ajouter dans le classement
    #
    # Fonction servant a ajouter un score au classement
    #
    def ajouterScore(self, valueObj):
        self.values.append(valueObj)

    # Fonction removeScore
    #
    # self : instance de la classe, ne doit pas être mis en argument
    # valueObj : score a retirer dans le classement
    #
    # Fonction servant a retirer un score au classement
    #
    def removeScore(self,valueObj):
        self.values.remove(valueObj)

    # Fonction getScore
    #
    # self : instance de la classe, ne doit pas être mis en argument
    # nom_joueur : nom du profil duquel récupérer le score
    #
    # Fonction servant a récupérer un score du classement
    #
    def getScore(self,nom_joueur):
        for element in self.values:
            if element[0] == nom_joueur:
                return element
        return 0
