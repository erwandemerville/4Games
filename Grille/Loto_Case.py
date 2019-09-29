# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier

try:
    import Case;
except:
    from Grille import Case;

class Case(Case.Case):
    'Case pour le loto'

    # Constructeur de la Case
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # number : le nombre qui sera contenu dans cette case. Ce nombre sera constant
    #
    # Instancie une Case.
    #
    def __init__(self, number):
        super().__init__();
        self.number = number;
        self.choosen = False;

    # Fonction choose
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque cette case comme choisie
    #
    def choose(self):
        self.choosen = True;

    # Fonction choose
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque cette case comme non-choisie
    #
    def unChoose(self):
        self.choosen = False;

    # Fonction choose
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # retourne le nombre contenu dans cette case.
    #
    def getNumber(self):
        return self.number;

    # Fonction estVide
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant un booleen indiquant si cette case est considérée comme vide
    #
    def estVide(self):
        return not(self.choosen);

    # Fonction contient
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # X : objet a tester
    #
    # Fonction retournant un booleen indiquant si cette case contient l'objet X.
    #
    def contient(self, X):
        return self.number == X;

    # Fonction draw
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # x : coordonnée horizontale du point le plus en haut a gauche de la zone ou dessiner la case.
    # y : coordonnée verticale du point le plus en haut a gauche de la zone ou dessiner la case.
    # x2 : coordonnée horizontale du point le plus en bas a droite de la zone ou dessiner la case.
    # y2 : coordonnée verticlae du point le plus en bas a droite de la zone ou dessiner la case.
    #
    # ARGUMENTS OPTIONELS :
    #
    # selectFill : couleur avec laquelle remplir la case si elle est marquée comme selectionnée
    # hoverFill : couleur avec laquelle remplir la case si elle est marquée comme hovered
    # bothFill : couleur avec laquelle remplir la case si elle est marquée comme selectionnée et comme hovered
    # textFill : couleur avec laquelle écrire le nombre contenu dans la case (si celui-ci est valide).
    # textFont : police d'écriture avec laquelle écrire le nombre contenu dans la case (si celui-ci est valide).
    # choosenFill : couleur avec laquelle remplir la case si elle est marquée comme choisie
    #
    # Si selectFill n'est pas précisé, selectFill sera bleu.
    # Si hoverFill n'est pas précisé, hoverFill sera vert.
    # Si bothFill n'est pas précisé, bothFill sera rouge.
    # Si textFill n'est pas précisé, textFill sera blanc.
    # Si textFont n'est pas précisé, textFont sera "Comic".
    # Si choosenFill n'est pas précisé, choosenFill sera "#757500".
    #
    def draw(self, canvas, x, y, x2, y2, selectFill="blue", hoverFill="green", bothFill="red", textFill="white", textFont="Comic", choosenFill="#757500"):
        # TODO: faire la classe quand le hud sera fait
        super().draw(canvas, x, y, x2, y2, selectFill=selectFill, hoverFill=hoverFill, bothFill=bothFill);

        if self.isSelected() and self.choosen and self.isHovered():
            canvas.create_rectangle(x, y, x2, y2, fill="#"+str(hex(choosenFill[1:])-0x313100));
        elif self.isSelected() and self.choosen:
            canvas.create_rectangle(x, y, x2, y2, fill="#"+str(hex(choosenFill[1:])-0x181800));
        elif self.choosen:
            canvas.create_rectangle(x, y, x2, y2, fill=choosenFill);
        elif self.isSelected() and self.isHovered():
            canvas.create_rectangle(x, y, x2, y2, fill=selectFill);
        elif self.isSelected():
            canvas.create_rectangle(x, y, x2, y2, fill=selectFill);
        elif self.isHovered():
            canvas.create_rectangle(x, y, x2, y2, fill=hoverFill);

        if self.number != 0:
            fontSize = abs(y2-y)-6;
            if self.number > 9:
                fontSize -= 6;
            canvas.create_text(x+abs(x2-x)/2, y+abs(y2-y)/2, fill=textFill, font=textFont+" "+str(int(fontSize)), text=str(self.number));
