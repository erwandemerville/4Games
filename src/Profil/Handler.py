import joueur
import pickle
import sys
import os

class Handler:
    "Classe servant de pseudo base de donnée qui sert à contenir les profils"

    def __init__(self, data):
        self.data = data
        self.profils = []
        self.currentProfil = -1

    def load(self, filename):
        try:
            with open(filename, 'rb') as fichier:
                mon_depickler = pickle.Unpickler(fichier)
                grille_recup = mon_depickler.load()
                fichier.close()
        except FileNotFoundError:
            return False
        except EOFError:
            return False
        else:
            if not grille_recup:
                return False
            else:
                for i in range(0, len(grille_recup)-1):
                    self.profils.append(joueur.Joueur(grille_recup[i][0], grille_recup[i][2]))
                    self.profils[-1]._setId(grille_recup[i][0])
                    self.profils[-1]._setCredits(grille_recup[i][3])
                self.currentProfil = grille_recup[-1]

    def save(self, filename):
        listeData = []
        for i in self.profils:
            listeData.append([i._getPseudo(), i._getId(), i._getMDP(), i._getCredits()])
        listeData.append(self.currentProfil)
        try:
            with open(filename, 'wb') as fichier:
                mon_pickler = pickle.Pickler(fichier)
                mon_pickler.dump(listeData)
                fichier.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def getcurrentProfil(self):
        if self.currentProfil == -1:
            return None
        else:
            return self.profils[self.currentProfil]

    def ProfilExist(self, Pseudo):
        for p in self.profils:
            if p._getPseudo() == Pseudo:
                return True
        return False

    def getProfil(self, Pseudo):
        i = 0
        for p in self.profils:
            if p._getPseudo() == Pseudo:
                return (p, i)
            i = i+1
        return (None, -1)

    def createProfil(self, Pseudo, MDP):
        if not self.ProfilExist(Pseudo):
            self.profils.append(joueur.Joueur(Pseudo, MDP))
            self.save("profilsData.data")
            return True
        return False

    def connect(self, Pseudo, MDP):
        if self.ProfilExist(Pseudo):
            pr = self.getProfil(Pseudo)
            self.currentProfil = pr[1]
            if self.getcurrentProfil()._getMDP() != MDP:
                self.currentProfil = -1
                return False
            self.save("profilsData.data")
            return True
        else:
            return False

    def deconnect(self):
        self.currentProfil = -1
        self.save("profilsData.data")
