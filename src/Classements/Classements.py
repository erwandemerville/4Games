import pickle
import pygame

class Classement:
    "Classe de base gérant les classements"

    def __init__(self, names, drawCoords=[]):
        self.names = names
        self.values = []
        self.drawCoords = drawCoords
        if self.drawCoords == [] :
            l = len(self.names)
            l2 = 1.0/l
            for i in range(0, l):
                self.drawCoords.append(l2)

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

    def sort(self, sortingFunc):
        reTurn = True
        while reTurn:
            reTurn = False
            for i in range(0, len(self.values)-1):
                if sortingFunc(self.values[i][1], self.values[i+1][1], self.values[i][2], self.values[i+1][2]):
                    temp = self.values[i]
                    self.values[i] = self.values[i+1]
                    self.values[i+1] = temp

    def ajouterScore(self, valueObj):
        self.values.append(valueObj)
