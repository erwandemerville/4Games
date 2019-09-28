# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier

try:
    import Case;
except:
    from Grille import Case;

class Case(Case.Case):
    'Case pour la bataille navale'

    # Constructeur de la Case
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    #
    # Instancie une Case.
    #
    def __init__(self):
        super().__init__();
        self.showShip = False;
        self.pinned = False;
        self.contenu = None;

    # Fonction showShip
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque que cette case doit afficher le bateau qu'elle contient (si elle en contient un)
    #
    def showShip(self):
        self.showShip = True;

    # Fonction unshowShip
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque que cette case ne doit pas afficher le bateau qu'elle contient (si elle en contient un)
    #
    def unshowShip(self):
        self.showShip = False;

    # Fonction isShowingSelected
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Retourne un booleen indiquant si cette case doit afficher le bateau qu'elle contient (si elle en contient un).
    #
    def isShowingSelected(self):
        return self.showShip;

    # Fonction pin
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque que cette case est épinglée
    #
    def pin(self):
        self.pinned = True;

    # Fonction unpin
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque que cette case n'est pas/plus épinglée
    #
    def unpin(self):
        self.pinned = False;

    # Fonction isPinned
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Retourne un booleen indiquant si cette case est marquée comme épinglée
    #
    def isPinned(self):
        return self.pinned;

    # Fonction setContenu
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # contenu : le contenu qui sera placé dans las case.
    #
    # Place l'argument contenu dans la case
    #
    def setContenu(self, contenu):
        self.contenu = contenu;

    # Fonction removeContenu
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Vide la case de son contenu
    #
    def removeContenu(self):
        self.contenu = None;

    # Fonction getcontenu
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Retourne le contenu de la case
    #
    def getcontenu(self):
        return self.contenu;

    # Fonction estVide
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant un booleen indiquant si cette case est considérée comme vide
    #
    def estVide():
        return self.contenu == None;

    # Fonction contient
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # X : objet a tester
    #
    # Fonction retournant un booleen indiquant si cette case contient l'objet X.
    #
    def contient(self, X):
        return self.contenu == X;

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
    #
    # Si selectFill n'est pas précisé, selectFill sera bleu.
    # Si hoverFill n'est pas précisé, hoverFill sera vert.
    # Si bothFill n'est pas précisé, bothFill sera rouge.
    #
    def draw(self, canvas, x, y, x2, y2, selectFill="blue", hoverFill="green", bothFill="red"):
        #TODO : Ajouter l'affichage de pinned et showShip quand les images seront faites.
        if self.isSelected() and self.isHovered():
            canvas.create_rectangle(x, y, x2, y2, fill=selectFill);
        elif self.isSelected():
            canvas.create_rectangle(x, y, x2, y2, fill=selectFill);
        elif self.isHovered():
            canvas.create_rectangle(x, y, x2, y2, fill=hoverFill);
