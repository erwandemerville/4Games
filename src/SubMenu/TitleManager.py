class TitleManager:
    "classe gérant les titres dans un menu"

    # Constructeur
    def __init__(self,titles):
        self.titles = titles

    #Fonction draw
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # frames : instance de la fenêtre
    #
    # Fonction permettant de dessiner les titres
    #
    def draw(self, frame):
        for i in  self.titles:
            i.draw(frame)
