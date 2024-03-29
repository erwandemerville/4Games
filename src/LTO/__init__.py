# Crée par BendoTV en 2019 pour le projet d'algorithmique et développement

from random import *
import time
from Grille import Grille, Loto_Case
from LTO import ia_loto
from LTO.ia_loto import IA_Loto
from Particules import FireWorkParticule, Particule

# Classe permettant de gérer une partie de loto
class Loto_Party():
    "Classe de lancement de partie de loto"
    def __init__(self,frame,data):
        self.frame = frame
        self.data = data
        self.grilles_mainplayer = []
        self.boules_in_game = []
        self.boules_sorties = []
        self.tab_IA = [ia_loto.IA_Loto(self),ia_loto.IA_Loto(self)]
        self.timer = 0
        self.reset()
        self.isStarted = False

    # Vérifie si une valeur value est dans cont
    @staticmethod
    def existInList(cont,value):
        for j in cont:
            if(j == value):
                return True
        return False

    # Génère à partir d'une grille donnée, une nouvelle grille
    @staticmethod
    def generateRandomContenuGrille(grille):
        cont = []
        for ligne in range(3):
            nb_none = 0
            for p in range(9):
                if (nb_none >= 4) or ((randint(0,1)==1) and not(nb_none <= p-4)):
                    val = randint(0, 9) + p*10
                    while Loto_Party.existInList(cont, val):
                        val = randint(0, 9) + p*10
                    cont.append(val)
                else:
                    cont.append(-1)
                    nb_none = nb_none + 1
        grille.fillByListNumeros(cont)

    # Retourne le nombre de numéros manquants pour faire un bingo
    def nbCasesLeft(self,grille):
        nb = 15
        for i in grille.getListeNumeros():
            if(self.containsNbInBoulesSorties(i)):
                nb = nb - 1
        return nb

    #Ajout la liste de grilles au joueur principal
    def addGrillesToMainPlayer(self,list):
        self.grilles_mainplayer.extend(list)
    # Détermine le nombre nb est sorti
    def containsNbInBoulesSorties(self,nb):
        for i in self.boules_sorties:
            if(i == nb):
                return True
        return False
    # Détermine si une grille donnée est gagnante
    def isOneGrilleWinner(self,grille):
        for i in grille.case:
            if not(self.containsNbInBoulesSorties(i.getNumber())) and not(i.getNumber()==-1):
                return False
        return True
    # Détermine si le joueur principal à gagné
    def isMainPlayerWinner(self):
        for grille in self.grilles_mainplayer:
            if self.isOneGrilleWinner(grille):
                return True
        return False
    # Détermine si une IA a gagné
    def asWinnerInIA(self):
        for ia in self.tab_IA:
            if(ia.isWinner()):
                return True
        return False
    # Permet de lancer le jeu
    def start(self):
        self.reset()
        self.isStarted = True

    # Fonction qui enlève tous les jetons d'une grille
    @staticmethod
    def removeAllJetonsS(grille):
        for case in grille.case:
            case.jetonIn = False
    # Fonction qui enlève tous les jetons du main_player
    def removeAllJetons(self):
        for grille in self.grilles_mainplayer:
            Loto_Party.removeAllJetonsS(grille)

    # Fonction qui affiche la fenetre
    def draw(self,frame,state):
        self.data.menus[9].draw(frame)
    # Fonction appelée toutes les secondes
    def timerTick(self):
        if self.isStarted:
            # Appelée à chaque seconde
            self.timer = self.timer + 1
            if(self.timer >= 5):
                # appel à après les 5 s
                #self.printStateGame()
                self.timer = 0
                self.data.menus[9].nbInBoule = self.sortirUneBoule()
            if self.timer > 2 and self.asWinnerInIA():
                self.stop()
                self.data.setEtat("Loto_End")
                self.data.soundSystem.playSound("BingoIA")
                self.data.soundSystem.playMusic("triste")
                self.data.menus[10].asWin = False
                self.classements(False)
            if(self.data.menus[9].nbInBoule==0):
                self.data.menus[9].titre.text = "Début de partie"
            elif(self.timer > 1):
                self.data.menus[9].titre.text = str(5-self.timer)
                self.data.soundSystem.playSound(str(5-self.timer))
            else:
                self.data.menus[9].titre.text = "Une nouvelle boule est sortie !"
        return 9

    #Fonction appelée pour arrêter le jeu
    def stop(self):
        self.isStarted = False

    # Fonction pour afficher l'état du jeu dans la console
    def printStateGame(self):
        print("--- Etat du jeu ---")
        print(len(self.boules_sorties)," Boules sorties : ",self.boules_sorties)
        print("Liste des Grilles : ")
        for grille in self.grilles_mainplayer:
            print("Reste ",self.nbCasesLeft(grille)," numéros dans ",grille)
        for ia in self.tab_IA:
            print("Pour l'IA ",ia.nom," generalWin?",ia.isWinner())
            for grille in ia.grilles:
                print("Reste ",self.nbCasesLeft(grille)," numéros dans ",grille," win?",ia.isOneGrilleWinner(grille))

    # Fonction appelée pour sortir une boule
    def sortirUneBoule(self):
        boule = choice(self.boules_in_game)
        self.boules_in_game.remove(boule)
        self.boules_sorties.append(boule)
        self.data.soundSystem.playSound("Boule")
        return boule
    # Fonction pour remettre à zéro le jeu
    def reset(self):
        self.boules_sorties.clear();self.boules_in_game.clear();self.grilles_mainplayer.clear()
        self.removeAllJetons()
        for i in range(1,90):
            self.boules_in_game.append(i)
        for ia in self.tab_IA:
            for grille in ia.grilles:
                Loto_Party.generateRandomContenuGrille(grille)

        # Fonction compareTimes
        #
        # self : instance de la partie, ne pas mettre en argument
        # tab : tableau contenant les scores sous la forme : [temps1, temps2, erreurs1, erreurs2]
        #
        # Fonction comparant 2 scores et retourne True si le premier score est le meilleur, sinon retourne False
        #
    def compare(self, tab):
        ratioA = int(tab[2].replace('%',''));ratioB = int(tab[3].replace('%',''))
        if ratioA == ratioB:
            nbWinA = int(tab[0].split("/")[0]);nbWinB = int(tab[1].split("/")[0])
            if nbWinA == nbWinB:
                nbLoseA = int(tab[0].split("/")[1]);nbLoseB = int(tab[1].split("/")[1])
                return nbLoseA > nbLoseB
            return nbWinA < nbWinB
        return ratioA < ratioB
     # Fonction de gestion des classements
    def classements(self,asWin):
        joueur = self.data.profilHandler.getcurrentProfil()
        if joueur != None:
            joueur = joueur._getPseudo()
        else:
            joueur = "Anonyme"
        score = self.data.classements[2].getScore(joueur)
        if score == 0:
            if asWin:
                self.data.classements[2].ajouterScore((joueur,"1/0","100%"))
            else:
                self.data.classements[2].ajouterScore((joueur,"0/1","0%"))
        else:
            self.data.classements[2].removeScore(score)
            wins = int(score[1].split("/")[0]);loses = int(score[1].split("/")[1])
            if asWin:
                avg = str(round(((wins+1)*100) / (wins+loses+1)))+"%"
                self.data.classements[2].ajouterScore((joueur,str(wins+1)+"/"+str(loses),avg))
            else:
                avg = str(round((wins*100) / (wins+loses+1)))+"%"
                self.data.classements[2].ajouterScore((joueur,str(wins)+"/"+str(loses+1),avg))
        self.data.classements[2].sort(self.compare)
        self.data.classements[2].save("Classements_Loto.yolo")

    # Fonction victoire
    #
    # self : instance de la partie, ne pas mettre en argument
    # data : instance de la classe data
    #
    # Fonction activant les feux d'artifices de victoires et ajoutant le score au classement (a Faire)
    #
    def victoire(self,data):
        rayon = 4
        data.particules.addEmitter(FireWorkParticule.FireworkEmitter(data.particules, [Particule.Particule((100,100), 60, (60, 60, 230))], [(10, 10, 235), (1, 1, 50)], rayon, 60, (320, 480), (0, -4) , 0, 2))
