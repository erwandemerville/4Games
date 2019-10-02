from tkinter import *
import Sudoku

class Application(object):
    def __init__(self):
        #Constructeur
        self.frame = Tk()
        self.frame.title("L'application de jeux")

        self.canv = Canvas(self.frame,bg="black",height=300,width=300)
        self.canv.pack(side=TOP,padx=0,pady=20)

        self.btn_profil = Button(self.frame,text="profil", width=60,command=self.goToProfil)
        self.btn_profil.pack()

        self.btn_bn = Button(self.frame,text="bataille navale", width=60,command=self.goToBN)
        self.btn_bn.pack()

        self.btn_loto = Button(self.frame,text="loto", width=60,command=self.goToLoto)
        self.btn_loto.pack()

        self.btn_poker = Button(self.frame,text="poker", width=60,command=self.goToPoker)
        self.btn_poker.pack()

        self.btn_sudoku = Button(self.frame,text="sudoku", width=60,command=self.goToSudoku)
        self.btn_sudoku.pack()

        self.btn_optn = Button(self.frame,text="options", width=60,command=self.goToOption)
        self.btn_optn.pack()

    def goToOption(self):
        #Méthode pour afficher les options
        print("Options")

    def goToProfil(self):
        #Méthode pour afficher le menu du profil
        print("profil")

    def goToSudoku(self):
        #Méthode pour appeller le jeu du sudoku
        print("Sudoku")
        Partie()

    def goToLoto(self):
        #Méthode pour appeller le jeu du loto
        print("loto")

    def goToBN(self):
        #Méthode pour appeller le jeu de la bataille navale
        print("bataille navale")

    def goToPoker(self):
        #Méthode pour appeller le jeu du poker
        print("poker")

    def goToMain(self):
        #Méthode pour appeller le menu principal
        print("main")



a = Application()
