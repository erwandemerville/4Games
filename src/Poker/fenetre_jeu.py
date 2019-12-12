import pygame as pygame
from pygame import *
from Poker.Jeu import Jeu
from Poker.affichage import *
import os

width = 756
height = 475

WHITE = (255, 255, 255)
DARK_RED = (153, 0, 76)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (255, 255, 153)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (102, 102, 255)
PURPLE = (128, 0, 128)
PINK = (255, 102, 255)
GRAY = (160, 160, 160)
LIGHT_GRAY = (215, 215, 215)
DARK_GRAY = (96, 96, 96)
LIGHT_BLACK = (32, 32, 32)
CYAN = (0, 255, 255)

table_de_jeu = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'images/table_poker.jpg')
table_de_jeu = pygame.transform.scale(table_de_jeu, (width, height))
LISTE_IMAGES_CARTES = [];
carte_vide = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'images/images-cartes/b2fv.png')
carte_vide = pygame.transform.scale(carte_vide, (54, 72))

donnees_position_joueurs = {3: [(160, 40), (500, 40), (355, 360), ],
                            4: [(160, 40), (510, 40), (520, 320), (180, 320), ],
                            5: [(160, 40), (510, 40), (570, 320), (350, 320), (140, 320), ]}

nb_joueurs = 0  # Initialiser nombre de joueurs à 0


def Recuperer_Images_Cartes():
    chemin = 'images/images-cartes/'
    j = 0

    for symbole in range(4):
        for valeur in range(13):
            j += 1
            nom_image_carte = chemin + str(j) + ".png"
            img = pygame.image.load(nom_image_carte)
            LISTE_IMAGES_CARTES.append(img)


def creer_liste_ID(mon_ID):
    global nb_joueurs
    liste_ID = []

    if mon_ID == 0:
        liste_id_NbJoueursRequis = list(range(nb_joueurs))
    else:
        liste_id_NbJoueursRequis = list(range(mon_ID, nb_joueurs)) + list(range(mon_ID))

    if nb_joueurs == 3:
        liste_ID = liste_id_NbJoueursRequis[1:] + liste_id_NbJoueursRequis[0:1]
    elif nb_joueurs == 4:
        liste_ID = liste_id_NbJoueursRequis[2:] + liste_id_NbJoueursRequis[0:2]
    elif nb_joueurs == 5:
        liste_ID = liste_id_NbJoueursRequis[2:] + liste_id_NbJoueursRequis[0:2]

    return liste_ID


def drawFenetre():
    global nb_joueurs
    win.blit(table_de_jeu, (0, 0))

    texte_attente.draw(win)
    texte_jeu.draw(win)

    # Dessiner pot
    pot.draw(win)

    for joueur in joueurs:
        joueur.draw(win)

    # Dessiner cartes
    for id_joueur in range(nb_joueurs):
        for carte in joueurs_cartes_screen[id_joueur]:
            carte.draw(win)

    # Dessiner cartes communes
    for carte in cartes_communes:
        carte.draw(win)

    # draw mise_pretes
    for mise_prete in mise_pretes:
        mise_prete.draw(win)

    # draw mises
    for m in mises:
        m.draw(win)

    for c in jetons:
        c.draw(win)

    # Dessiner boutons
    for bouton in allbtns:
        bouton.draw(win)

    arrow1.draw(win)

    # Dessiner le résultat du vainqueur de la partie
    resultat_gagnant_dessiner.draw(win)

    pygame.display.update()


def dessiner_mains_joueurs(joueur_cartes, pid, liste_ID):
    global nb_joueurs
    # Fonction affichant la main de chaque joueur lors du dévoilement des cartes
    for id_joueur in range(nb_joueurs):
        screen_id = liste_ID.index(id_joueur)

        if id_joueur != pid:
            joueur_carte = joueur_cartes[id_joueur]  # Récupérer les cartes du joueur dont l'ID est id_joueur

            carte1 = joueur_carte[0]
            carte2 = joueur_carte[1]

            joueur_carte1 = joueurs_cartes_screen[screen_id][0]
            pos_carte1 = joueur_carte1.get_pos()
            joueur_carte1.set_pos(pos_carte1[0] - 10, pos_carte1[1], pos_carte1[2] - 10, pos_carte1[3])
            joueur_carte1.set_image(LISTE_IMAGES_CARTES[(13 * carte1.symbole) + carte1.valeur])

            joueur_carte2 = joueurs_cartes_screen[screen_id][1]
            pos_carte2 = joueur_carte2.get_pos()
            joueur_carte2.set_pos(pos_carte2[0] - 10, pos_carte2[1], pos_carte2[2] - 10, pos_carte2[3])
            joueur_carte2.set_image(LISTE_IMAGES_CARTES[(13 * carte2.symbole) + carte2.valeur])

            joueur_carte1.set_visible(True)
            joueur_carte2.set_visible(True)

    drawFenetre()


def dessiner_main(joueur_cartes, liste_ID, id_joueur_doitJouer):
    # Fonction affichant la main d'un joueur.
    # La fonction remplace les images utilisée pour représenter les cartes par celles appropriées.

    screen_id = liste_ID.index(id_joueur_doitJouer)

    joueur_carte = joueur_cartes[id_joueur_doitJouer]  # Récupérer les cartes du joueur dont l'ID est id_joueur

    carte1 = joueur_carte[0]
    carte2 = joueur_carte[1]

    joueur_carte1 = joueurs_cartes_screen[screen_id][0]
    joueur_carte1.set_image(LISTE_IMAGES_CARTES[(13 * carte1.symbole) + carte1.valeur])
    joueur_carte1.set_joueur_carte(True)

    joueur_carte2 = joueurs_cartes_screen[screen_id][1]
    joueur_carte2.set_image(LISTE_IMAGES_CARTES[(13 * carte2.symbole) + carte2.valeur])
    joueur_carte2.set_joueur_carte(True)

    drawFenetre()


def cacher_main(joueur_cartes, liste_ID, id_joueur_doitJouer):
    # Fonction cachant la main d'un joueur.
    # La fonction remplace les images utilisée pour représenter les cartes par celles appropriées.
    global carte_vide

    screen_id = liste_ID.index(id_joueur_doitJouer)

    joueur_carte = joueur_cartes[id_joueur_doitJouer]  # Récupérer les cartes du joueur dont l'ID est id_joueur

    joueur_carte1 = joueurs_cartes_screen[screen_id][0]
    joueur_carte1.set_image(carte_vide)
    joueur_carte1.set_joueur_carte(True)

    joueur_carte2 = joueurs_cartes_screen[screen_id][1]
    joueur_carte2.set_image(carte_vide)
    joueur_carte2.set_joueur_carte(True)

    drawFenetre()


def dessiner_resultat_gagnant(gagnant):
    nom_gagnant = gagnant.nom
    id_joueur_gagnant = gagnant.id
    resultat_gagnant = gagnant.resultat_manche

    # Dessiner résultat du gagnant
    result_text = "Gagnant: " + nom_gagnant + "(" + str(id_joueur_gagnant) + ") , " + resultat_gagnant.result_name + \
                  ', (' + str(
        resultat_gagnant.high_suit) + ', ' + str(resultat_gagnant.high_rank) + ')'
    result_cartes = resultat_gagnant.hands

    img_list = []
    for c in result_cartes:
        img = LISTE_IMAGES_CARTES[(13 * c.symbole) + c.valeur]
        img_list.append(img)

    resultat_gagnant_dessiner.set_carte_imgs(img_list)
    resultat_gagnant_dessiner.set_result_text(result_text)
    resultat_gagnant_dessiner.set_visible(True)

    drawFenetre()


def dessiner_resultat_gagnant_forfait(gagnant):
    if gagnant is not None:
        nom_gagnant = gagnant.nom
        id_joueur_gagnant = gagnant.id
        resultat_gagnant = "Tous les autres joueurs se sont couchés !"

        # Dessiner résultat du gagnant
        result_text = "Gagnant : " + nom_gagnant + "(" + str(id_joueur_gagnant) + ") , " + resultat_gagnant
        print(result_text)
        dessiner_resultat_gagnantforf.set_result_text(result_text)
        dessiner_resultat_gagnantforf.set_visible(True)

        drawFenetre()


def initialiser_mises(joueurs_dico_donnees, liste_ID):
    global nb_joueurs
    for id_joueur in range(nb_joueurs):
        pid_ecran = liste_ID.index(id_joueur)

        if joueurs_dico_donnees[id_joueur]["estCouche"]:
            joueur_rect = joueurs[pid_ecran].get_rect()

            if joueur_rect[1] < height // 2:  # Partie haute
                mises[pid_ecran].set_pos(joueur_rect[0] + 60, joueur_rect[1] + joueur_rect[3] - 15)
            else:  # Partie basse
                mises[pid_ecran].set_pos(joueur_rect[0] + 60, joueur_rect[1] - 15)

            mises[pid_ecran].set_mise("Couche", 0)
            mises[pid_ecran].set_visible(True)
        else:
            mises[pid_ecran].set_visible(False)


def dessiner_elements_mise(id_dernier_ayant_joue, id_joueur_doitJouer, liste_ID, joueurs_dico_donnees, miseTerminee):
    pid_ecran = liste_ID.index(id_joueur_doitJouer)

    joueur_rect = joueurs[pid_ecran].get_rect()

    if joueur_rect[1] < height // 2:  # on the upper half
        mise_pretes[pid_ecran].set_pos(joueur_rect[0], joueur_rect[1] + joueur_rect[3] + 12)
    else:  # on the lower half
        mise_pretes[pid_ecran].set_pos(joueur_rect[0], joueur_rect[1] - 42)

    mise_pretes[pid_ecran].set_visible(True)

    if not id_dernier_ayant_joue == -1 and id_dernier_ayant_joue != id_joueur_doitJouer:
        pid_ecran = liste_ID.index(id_dernier_ayant_joue)
        mise_pretes[pid_ecran].set_visible(False)

    # to draw mise & jeton when it has changed id_joueur_doitJouer
    if (not id_dernier_ayant_joue == -1 and id_dernier_ayant_joue != id_joueur_doitJouer) or miseTerminee:
        joueur_dans_partie = joueurs_dico_donnees[id_dernier_ayant_joue]
        derniere_action_mise = joueur_dans_partie["derniere_action_mise"]
        valeur_derniere_mise = joueur_dans_partie["valeur_derniere_mise"]

        pid_ecran = liste_ID.index(id_dernier_ayant_joue)
        joueur_rect = joueurs[pid_ecran].get_rect()

        # print(
        #    "id_dernier_ayant_joue: {0}, id_joueur_doitJouer: {1}, pid_ecran: {2}".format(id_dernier_ayant_joue,
        #                                                                               id_joueur_doitJouer,
        #                                                                               pid_ecran))

        if joueur_rect[1] < height // 2:  # on the upper half
            mises[pid_ecran].set_pos(joueur_rect[0] + 65, joueur_rect[1] + joueur_rect[3] - 25)
        else:  # on the lower half
            mises[pid_ecran].set_pos(joueur_rect[0] + 65, joueur_rect[1] + 15)

        mises[pid_ecran].set_mise(derniere_action_mise, valeur_derniere_mise)
        mises[pid_ecran].set_visible(True)

        if miseTerminee:
            mise_pretes[pid_ecran].set_visible(False)

        # Dessiner jeton
        global jetons

        if derniere_action_mise == "Relance" or derniere_action_mise == "Suivre" or derniere_action_mise == "All_In":

            if joueur_rect[1] < height // 2:  # on the upper half
                new_jeton_pos_y = joueur_rect[1] + joueur_rect[3] + 5
                new_jeton_pos_y_end = new_jeton_pos_y + 30
            else:
                new_jeton_pos_y = joueur_rect[1] - 5
                new_jeton_pos_y_end = new_jeton_pos_y - 30

            longueur_jetons = len(jetons)
            jeton_color = BLACK

            if longueur_jetons <= len(jeton_colors) - 1:
                jeton_color = jeton_colors[longueur_jetons]

            new_jeton = jeton('', 100, 100, 24, 17, 50, width, height, jeton_color, BLACK, BLACK)

            if longueur_jetons >= 3:

                if joueur_rect[1] < width // 2:  # on the left half
                    new_jeton_pos_x = joueur_rect[0] + 30 - (longueur_jetons // 3) * 10
                else:
                    new_jeton_pos_x = joueur_rect[0] + 30 + (longueur_jetons // 3) * 10
            else:
                if joueur_rect[1] < width // 2:  # on the left half
                    new_jeton_pos_x = joueur_rect[0] + 30
                else:
                    new_jeton_pos_x = joueur_rect[0] + 30

            new_jeton.set_pos(new_jeton_pos_x, new_jeton_pos_y, new_jeton_pos_y_end)
            new_jeton.set_text(str(valeur_derniere_mise))
            new_jeton.set_visible(True)

            jetons.append(new_jeton)

            print(jetons[len(jetons) - 1].IsVisible)
            print("Un nouveau jeton ({0}, {1}, {2}) a été créé !".format(new_jeton_pos_x, new_jeton_pos_y,
                                                                         new_jeton_pos_y_end))

    drawFenetre()


def init_joueur_cartes():
    global nb_joueurs
    global joueurs_cartes_screen
    global joueur_pos
    global carte_vide

    joueurs_cartes_screen = {}

    id_joueur = 0

    for pos in joueur_pos:
        # Créer des cartes vides et les ajouter aux joueurs.
        # La position des cartes est également définie ici.
        carte1 = carte(pos[0] - 105, 0, pos[0] - 105, pos[1] - 4, carte_vide)
        joueurs_cartes_screen[id_joueur] = []
        joueurs_cartes_screen[id_joueur].append(carte1)
        carte2 = carte(pos[0] - 60, 0, pos[0] - 60, pos[1] - 4, carte_vide)
        joueurs_cartes_screen[id_joueur].append(carte2)
        id_joueur += 1


Recuperer_Images_Cartes()

texte_attente = text(200, 195, 'En attente des autres joueurs...', 28, color=(220, 220, 80))
texte_jeu = text(180, 190, '', 40, color=(220, 220, 200))

pot = pot(width - 100, 20)

joueurs = []
nb_j_max = 5

# Création positions joueurs
joueur_pos = donnees_position_joueurs[nb_j_max]

for pos in joueur_pos:
    new_joueur = joueur(pos[0], pos[1], "")
    joueurs.append(new_joueur)

id_joueur_courant = round((nb_j_max + 0.1) / 2)

# create joueurs_cartes_screen
joueurs_cartes_screen = {}
init_joueur_cartes()

# create community cartes
cartes_communes = []

com_carte_pos_x = 172
com_carte_pos_y = 157

for i in range(5):
    cartes_communes.append(carte(com_carte_pos_x + i * 80, 0, com_carte_pos_x + i * 80, com_carte_pos_y, carte_vide))

# create mise_pretes
mise_pretes = []

for pos in joueur_pos:
    new_mise_prete = mise_prete(pos[0], pos[1])
    mise_pretes.append(new_mise_prete)

# create mises
mises = []

for pos in joueur_pos:
    new_mise = mise(pos[0], pos[1])
    mises.append(new_mise)

# create jetons
jetons = []
jeton_colors = [RED, GREEN, YELLOW, PURPLE, BLUE, DARK_RED, BLACK, LIGHT_BLUE, PINK, GRAY, LIGHT_GRAY, LIGHT_BLACK,
                CYAN]

# Résultat gagnant
resultat_gagnant_dessiner = resultat_gagnant(width // 2 - 170, height // 2 - 53)

# Résultat gagnant par abandon
dessiner_resultat_gagnantforf = resultat_gagnant_forfait(width // 2 - 260, height // 2 - 15)

# Création boutons
dy = 160
dx = -300
btn_pos_x, btn_pos_y = 300, 280
btn_check = btn('Check', btn_pos_x + 140 + dx, btn_pos_y + dy, 30, LIGHT_BLACK, WHITE, LIGHT_YELLOW, BLACK)
btn_se_coucher = btn('Couche', btn_pos_x + 220 + dx, btn_pos_y + dy, 30, RED, WHITE, LIGHT_YELLOW, BLACK)
mise_btn = btn('Miser', btn_pos_x + 300 + dx, btn_pos_y + dy, 30, CYAN, WHITE, LIGHT_YELLOW, BLACK)

btns = [btn_check, btn_se_coucher, mise_btn]

btn_Suivre = btn('Suivre', btn_pos_x + 400 + dx, btn_pos_y + dy, 30, BLUE, LIGHT_BLUE, LIGHT_GRAY, BLACK)
btn_Relance = btn('Relance', btn_pos_x + 400 + 70 + dx, btn_pos_y + dy, 30, RED, PINK, LIGHT_GRAY, BLACK)
btn_All_In = btn('All_In', btn_pos_x + 400 + 140 + dx, btn_pos_y + dy, 30, GREEN, LIGHT_YELLOW, LIGHT_GRAY, BLACK)

mise_btns = [btn_Suivre, btn_Relance, btn_All_In]

allbtns = btns + mise_btns

arrow1 = arrow(btn_pos_x + 340, btn_pos_y - 10, 20, 0, BLACK)

def main(texte_saisi):
    run = True

    global nb_joueurs
    jeu = Jeu(nb_joueurs)

    win.blit(table_de_jeu, (0, 0))
    pygame.display.set_caption("Poker")
    pygame.display.update()

    clock = pygame.time.Clock()

    liste_ID = creer_liste_ID(0)
    jeu.ordre_des_joueurs = liste_ID

    # ------- DEFINIR NOMS DES JOUEURS : ---------
    joueurs_nom = texte_saisi
    id_nt = 0
    for id_joueur in jeu.ordre_des_joueurs:
        jeu.connexion_joueur(id_joueur, joueurs_nom[id_nt])
        id_nt += 1
    # --------------------------------------------

    # Supprimer joueurs en trop :
    for k in range(nb_joueurs, len(joueurs)):
        del joueurs[-1]

    non_effectue_etape_initialisation = True
    non_effectue_etape_preflop = True
    non_effectue_etape_flop = True
    non_effectue_etape_tournant = True
    non_effectue_etape_riviere = True
    non_effectue_etape_devoilement = True
    non_effectue_etape_abandon_joueurs = True

    petiteBlinde_mise = False
    grosseBlinde_mise = False

    id_dernier_ayant_joue = -1

    while run:
        clock.tick(10)
        global jetons

        try:
            etat_jeu = jeu.etat_jeu
            joueurs_dico_donnees = jeu.recuperer_donnees_joueurs()
            id_joueur_doitJouer = jeu.id_joueur_enTrainDe_jouer
            miseTerminee = jeu.miseTerminee
            pot_argent = jeu.pot.pot_argent

            # Infos mises
            init_valeur_mise = jeu.mise_initiale

            valeur_mise_suivre = jeu.valeur_Suivre
            is_check_allowable = jeu.estCheckAutorise
            est_suivre_autorise = jeu.estSuivreAutorise
            raise_amount = jeu.valeur_relance

            if etat_jeu != "LancementJeu" and etat_jeu != "MancheInitialisation":
                # =============================== Afficher les cartes ====================================
                jeu.recuperer_liste_cartes()

                # Rendre les cartes visibles :
                if etat_jeu == "PreFlop":
                    for id_joueur in range(nb_joueurs):
                        joueurs_cartes_screen[id_joueur][0].set_visible(True)
                        joueurs_cartes_screen[id_joueur][1].set_visible(True)
                # --------------------------------------------------------

                if not petiteBlinde_mise and not grosseBlinde_mise:
                    if not id_dernier_ayant_joue == id_joueur_doitJouer:
                        cacher_main(jeu.joueurs_cartes, liste_ID, id_dernier_ayant_joue)
                        dessiner_main(jeu.joueurs_cartes, liste_ID, id_joueur_doitJouer)
                # ========================================================================================

            if etat_jeu == "LancementJeu":
                texte_attente.set_visible(False)

                texte_jeu.set_text("Lancement Jeu")
                texte_jeu.set_visible(True)

                drawFenetre()

                pygame.time.delay(1000)

                # Accès à la manche d'initialisation
                for id_joueur in jeu.ordre_des_joueurs:
                    jeu.lancerPartie(id_joueur)

            elif etat_jeu == "MancheInitialisation":
                if non_effectue_etape_initialisation:
                    non_effectue_etape_devoilement = True
                    non_effectue_etape_abandon_joueurs = True

                    texte_jeu.set_text("Initialisation de la manche...")

                    petiteBlinde_mise = True
                    grosseBlinde_mise = True
                    jeu.grosseBlindeAparle = False

                    pot.set_visible(True)

                    # Ne plus afficher le résultat du dernier gagnant
                    resultat_gagnant_dessiner.set_visible(False)

                    jetons = []

                    init_joueur_cartes()

                    for c in cartes_communes:
                        c.set_visible(False)

                    for miseprete in mise_pretes:
                        miseprete.set_visible(False)

                    for butn in allbtns:
                        butn.set_visible(False)

                    arrow1.set_visible(False)

                    non_effectue_etape_initialisation = False

                tmp_id_joueur = 0
                # Récupérer données sur chaque joueur (nom, argent, statut, etc.)
                for joueur in joueurs:
                    # new joueur's dict
                    joueur_dans_partie = joueurs_dico_donnees[liste_ID[tmp_id_joueur]]
                    nom = joueur_dans_partie["nom"]
                    argent = joueur_dans_partie["argent"]

                    tmp_id_joueur += 1
                    joueur.maj_nom(nom)
                    joueur.maj_argent(argent)

                    # Afficher donneur, petite blinde, grosse blinde
                    estDonneur = joueur_dans_partie["estDonneur"]
                    estPetiteBlinde = joueur_dans_partie["estPetiteBlinde"]
                    estGrosseBlinde = joueur_dans_partie["estGrosseBlinde"]

                    # Effacer les rôles existants
                    joueur.maj_estDonneur(False)
                    joueur.maj_estPblinde(False)
                    joueur.maj_estGblinde(False)

                    if estDonneur:
                        joueur.maj_estDonneur(True)
                    if estPetiteBlinde:
                        joueur.maj_estPblinde(True)
                    if estGrosseBlinde:
                        joueur.maj_estGblinde(True)

                # set current joueur visible
                for j in joueurs:
                    j.set_visible(True)

                drawFenetre()

                pygame.time.delay(1000)

                jeu.etat_jeu = "MancheInitialisation"
                for id_joueur in jeu.ordre_des_joueurs:
                    jeu.initialisation_manche(id_joueur)

            elif etat_jeu == "PreFlop":
                if non_effectue_etape_preflop:
                    texte_jeu.set_text("Pré-Flop")

                    id_dernier_ayant_joue = -1
                    jetons = []
                    initialiser_mises(joueurs_dico_donnees, liste_ID)

                    non_effectue_etape_preflop = False

                # Envoi d'une requête indiquant la fin du Pré-flop lorsque le tour de mise est terminé
                if miseTerminee:
                    for id_joueur in jeu.ordre_des_joueurs:
                        jeu.preflop(id_joueur)
                    continue

                # Afficher mises et jetons
                dessiner_elements_mise(id_dernier_ayant_joue, id_joueur_doitJouer, liste_ID, joueurs_dico_donnees,
                                       miseTerminee)

                # Petite et grosse blindes relancent automatiquement.
                # Si c'est au tour d'une petite ou grosse blinde de jouer, et que ce client est celui d'un de ces
                # deux joueurs, la relance s'effectue automatiquement.
                if True:
                    if joueurs_dico_donnees[id_joueur_doitJouer]["estPetiteBlinde"] and petiteBlinde_mise:
                        jeu.joueur_mise(id_joueur_doitJouer, ("Relance", init_valeur_mise))
                        petiteBlinde_mise = False

                    elif joueurs_dico_donnees[id_joueur_doitJouer]["estGrosseBlinde"] and grosseBlinde_mise:
                        jeu.joueur_mise(id_joueur_doitJouer, ("Relance", raise_amount))
                        grosseBlinde_mise = False

                id_dernier_ayant_joue = id_joueur_doitJouer

                drawFenetre()

            elif etat_jeu == "Flop":
                if non_effectue_etape_flop:
                    texte_jeu.set_text("Flop")

                    id_dernier_ayant_joue = -1

                    jetons = []

                    initialiser_mises(joueurs_dico_donnees, liste_ID)

                    for mise_p in mise_pretes:
                        mise_p.set_visible(False)

                    for butn in allbtns:
                        butn.set_visible(False)

                    arrow1.set_visible(False)

                    non_effectue_etape_flop = False

                # Requête si tour de mise du flop est terminé
                if miseTerminee:
                    for id_joueur in jeu.ordre_des_joueurs:
                        jeu.flop(id_joueur)
                    continue

                # Afficher cartes communes
                list_cartes = jeu.cartes_communes

                cartes_communes[0].set_image(
                    LISTE_IMAGES_CARTES[(13 * list_cartes[0].symbole) + list_cartes[0].valeur])
                cartes_communes[0].set_visible(True)

                cartes_communes[1].set_image(
                    LISTE_IMAGES_CARTES[(13 * list_cartes[1].symbole) + list_cartes[1].valeur])
                cartes_communes[1].set_visible(True)

                cartes_communes[2].set_image(
                    LISTE_IMAGES_CARTES[(13 * list_cartes[2].symbole) + list_cartes[2].valeur])
                cartes_communes[2].set_visible(True)

                # to draw mise_pretes, mises, jetons
                dessiner_elements_mise(id_dernier_ayant_joue, id_joueur_doitJouer, liste_ID, joueurs_dico_donnees,
                                       miseTerminee)

                id_dernier_ayant_joue = id_joueur_doitJouer

                drawFenetre()

            elif etat_jeu == "Tournant":
                if non_effectue_etape_tournant:
                    texte_jeu.set_text("Tournant")

                    id_dernier_ayant_joue = -1

                    jetons = []
                    initialiser_mises(joueurs_dico_donnees, liste_ID)

                    for mise_p in mise_pretes:
                        mise_p.set_visible(False)

                    for butn in allbtns:
                        butn.set_visible(False)

                    arrow1.set_visible(False)

                    non_effectue_etape_tournant = False

                # Si la mise est terminée, passer au Tournant
                if miseTerminee:
                    for id_joueur in jeu.ordre_des_joueurs:
                        jeu.tournant(id_joueur)
                    continue

                # Afficher cartes communes
                list_cartes = jeu.cartes_communes

                cartes_communes[3].set_image(
                    LISTE_IMAGES_CARTES[(13 * list_cartes[3].symbole) + list_cartes[3].valeur])
                cartes_communes[3].set_visible(True)

                # to draw mise_pretes, mises, jetons
                dessiner_elements_mise(id_dernier_ayant_joue, id_joueur_doitJouer, liste_ID, joueurs_dico_donnees,
                                       miseTerminee)

                id_dernier_ayant_joue = id_joueur_doitJouer

                drawFenetre()

            elif etat_jeu == "Riviere":
                if non_effectue_etape_riviere:
                    texte_jeu.set_text("Riviere")

                    id_dernier_ayant_joue = -1

                    jetons = []
                    initialiser_mises(joueurs_dico_donnees, liste_ID)

                    for mise_p in mise_pretes:
                        mise_p.set_visible(False)

                    for butn in allbtns:
                        butn.set_visible(False)

                    arrow1.set_visible(False)

                    non_effectue_etape_riviere = False

                if miseTerminee:
                    for id_joueur in jeu.ordre_des_joueurs:
                        jeu.riviere(id_joueur)
                    continue

                # Afficher cartes communes
                list_cartes = jeu.cartes_communes

                cartes_communes[4].set_image(
                    LISTE_IMAGES_CARTES[(13 * list_cartes[4].symbole) + list_cartes[4].valeur])
                cartes_communes[4].set_visible(True)

                # Dessiner mises pretes, mises, jetons
                dessiner_elements_mise(id_dernier_ayant_joue, id_joueur_doitJouer, liste_ID, joueurs_dico_donnees,
                                       miseTerminee)

                id_dernier_ayant_joue = id_joueur_doitJouer

                drawFenetre()

            elif etat_jeu == "Devoilement":
                print("ON ENTRE DANS DEVOILEMENT")
                if non_effectue_etape_devoilement:
                    texte_jeu.set_text("Devoilement")

                    # Mises, jetons, boutons, flèches sur FALSE
                    jetons = []

                    for mis in mises:
                        mis.set_visible(False)

                    for butn in allbtns:
                        butn.set_visible(False)

                    arrow1.set_visible(False)

                    non_effectue_etape_devoilement = False

                # Dessiner main de chaque joueur
                dessiner_mains_joueurs(jeu.joueurs_cartes, id_joueur_doitJouer, liste_ID)
                drawFenetre()
                pygame.time.delay(500)

                # Dessiner résultat vainqueur
                dessiner_resultat_gagnant(jeu.gagnant)
                drawFenetre()
                pygame.time.delay(6000)

                # Pour afficher le résultat du gagnant
                # Envoyer devoilement à la prochaine requête
                for id_joueur in jeu.ordre_des_joueurs:
                    jeu.devoilement_cartes(id_joueur)

                non_effectue_etape_initialisation = True
                non_effectue_etape_preflop = True
                non_effectue_etape_flop = True
                non_effectue_etape_tournant = True
                non_effectue_etape_riviere = True

            elif etat_jeu == "MancheQuittee":
                if non_effectue_etape_abandon_joueurs:
                    texte_jeu.set_text("Manche terminée")
                    print("Manche terminée")

                    jetons = []

                    for mis in mises:
                        mis.set_visible(False)

                    for butn in allbtns:
                        butn.set_visible(False)

                    arrow1.set_visible(False)

                    non_effectue_etape_abandon_joueurs = False

                # Dessiner résultat vainqueur_quit
                dessiner_resultat_gagnant_forfait(jeu.gagnant)
                drawFenetre()
                pygame.time.delay(3000)

                # Envoi requête au serveur
                for id_joueur in jeu.ordre_des_joueurs:
                    jeu.quitter_la_manche(id_joueur)

                # Réinitialisation des étapes :
                non_effectue_etape_initialisation = True
                non_effectue_etape_preflop = True
                non_effectue_etape_flop = True
                non_effectue_etape_tournant = True
                non_effectue_etape_riviere = True

            else:
                texte_attente.set_visible(True)
                drawFenetre()

            # Dessiner boutons
            if etat_jeu == "PreFlop" or etat_jeu == "Flop" or etat_jeu == "Tournant" or etat_jeu == "Riviere":

                # Afficher joueur
                tmp_id_joueur = 0
                for joueur in joueurs:
                    # new joueur's dict
                    joueur_dans_partie = joueurs_dico_donnees[liste_ID[tmp_id_joueur]]
                    nom = joueur_dans_partie["nom"]
                    argent = joueur_dans_partie["argent"]

                    tmp_id_joueur += 1
                    joueur.maj_nom(nom)
                    joueur.maj_argent(argent)

                # Afficher pot
                pot.maj_argent(pot_argent)

                # Les boutons représentant les actions possibles pour le joueur devant jouer s'affichent.
                if True:  # Tout le temps vrai car pour chaque joueur on affiche des boutons
                    for butn in btns:
                        butn.set_visible(True)  # Rendre les boutons visibles

                        if butn.is_equal("Check"):
                            if not is_check_allowable:  # Ne pas afficher bouton "Check" si action non autorisée
                                butn.set_visible(False)

                    for evenement in pygame.event.get():
                        # Si un bouton est pressé
                        if evenement.type == pygame.MOUSEBUTTONDOWN:
                            print("bouton pressé")
                            pos = pygame.mouse.get_pos()

                            type_mise = ""
                            valeur_mise = 0

                            for btn in btns:
                                if btn.inside_pos(pos):
                                    if btn.is_equal("Check"):  # SI joueur clique sur "Check"
                                        type_mise = "Check"
                                    elif btn.is_equal("Couche"):  # SI joueur clique sur "Couche"
                                        type_mise = "Couche"
                                        print("\n {}".format(type_mise))
                                    elif btn.is_equal("Miser"):  # SI joueur clique sur "Miser"

                                        afficher_bouton = 0
                                        argent_joueur = joueurs_dico_donnees[id_joueur_doitJouer]["argent"]

                                        # Afficher les boutons de la catégorie "miser"
                                        for item in mise_btns:
                                            if not item.is_equal("Suivre"):  # Si le bouton n'est pas "suivre" :
                                                if item.is_equal("Relance") and (argent_joueur - raise_amount) >= 0:
                                                    item.toggle_visible()  # Afficher bouton "relance"
                                                    afficher_bouton = 1
                                                if item.is_equal("All_In") and (argent_joueur >= valeur_mise_suivre):
                                                    item.toggle_visible()  # Afficher bouton All_In
                                                    afficher_bouton = 1
                                            else:  # Afficher "Suivre" uniquement si autorisé
                                                if est_suivre_autorise and (argent_joueur -
                                                                            valeur_mise_suivre) >= 0:
                                                    item.toggle_visible()
                                                    afficher_bouton = 1

                                        # Cacher la flèche apparaissant à droite du bouton "Miser" si aucune option
                                        # de mise n'est disponible.
                                        if afficher_bouton:
                                            arrow1.toggle_visible()

                            for btn in mise_btns:
                                if btn.inside_pos(pos):
                                    if btn.is_equal("Suivre"):  # SI joueur clique sur "Suivre"
                                        type_mise = "Suivre"
                                        valeur_mise = valeur_mise_suivre
                                    elif btn.is_equal("Relance"):  # SI joueur clique sur "Relance"
                                        type_mise = "Relance"
                                        valeur_mise = raise_amount
                                    elif btn.is_equal("All_In"):  # SI joueur clique sur "All_In"
                                        type_mise = "All_In"
                                        valeur_mise = joueurs_dico_donnees[id_joueur_doitJouer]["argent"]

                            if type_mise == "Check":
                                jeu.joueur_check(id_joueur_doitJouer)
                            elif type_mise == "Couche":
                                jeu.joueur_se_couche(id_joueur_doitJouer)
                            elif type_mise == "Suivre" or type_mise == "Relance" or type_mise == "All_In":
                                for btn in mise_btns:
                                    if btn.is_equal("Suivre") or btn.is_equal("Relance") or btn.is_equal("All_In"):
                                        btn.set_visible(False)
                                        arrow1.set_visible(False)
                                jeu.joueur_mise(id_joueur_doitJouer, (type_mise, valeur_mise))

                        elif event.type == pygame.MOUSEMOTION:
                            pos = pygame.mouse.get_pos()

                            for btn in allbtns:
                                if btn.inside_pos(pos):
                                    btn.set_ismousedown(True)
                                else:
                                    btn.set_ismousedown(False)

                else:
                    pass

                drawFenetre()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                        run = False
                        pygame.quit()

        except Exception as e:
            run = False
            print(str(e))

def choix_nb_joueurs():
    global nb_joueurs

    pos_init_x, pos_init_y = 130, 100

    input_box = pygame.Rect(pos_init_x, pos_init_y + 50, 140, 32)
    color_inactive = pygame.Color('LIGHTSKYBLUE')
    color_active = pygame.Color('DODGERBLUE')
    color = color_inactive
    continuer_btn = btn2('Valider', 'saisie', pos_init_x + 120, pos_init_y + 60, 33, pygame.Color('DARKBLUE'),
                     pygame.Color('WHITE'), pygame.Color('THISTLE'), pygame.Color('FIREBRICK'))
    continuer_btn.set_visible(True)

    active = False
    nombre_joueurs = ''
    done = False

    clock = pygame.time.Clock()

    while not done:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if continuer_btn.inside_pos(pos):
                    print(nombre_joueurs)
                    nb_joueurs = int(nombre_joueurs)
                    saisir_noms_joueurs()

                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive

            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()

                if continuer_btn.inside_pos(pos):
                    continuer_btn.set_ismousedown(True)
                else:
                    continuer_btn.set_ismousedown(False)

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(nombre_joueurs)
                        nombre_joueurs = ''
                    elif event.key == pygame.K_BACKSPACE:
                        nombre_joueurs = nombre_joueurs[:-1]
                    else:
                        nombre_joueurs += event.unicode

        win.fill((30, 30, 30))

        font = pygame.font.Font(None, 28)
        txt_nbj = font.render("Combien y a-t-il de joueurs ? (3 à 5)", True, (255, 255, 255))
        win.blit(txt_nbj, (pos_init_x, pos_init_y))

        # Render the current text.
        txt_surface = font.render(nombre_joueurs, True, color)
        # Resize the box if the text is too long.
        input_box_width = max(60, txt_surface.get_width() + 10)
        input_box.w = input_box_width
        # Blit the text.
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(win, color, input_box, 2)
        # Blit the Btn
        continuer_btn.draw(win)

        pygame.display.update()

def saisir_noms_joueurs():

    global nb_joueurs
    texte_saisi = [0 for i in range(nb_joueurs)]
    for i in range(nb_joueurs):
        print("Bonjour")
        pos_init_x, pos_init_y = 130, 100

        input_box = pygame.Rect(pos_init_x, pos_init_y + 50, 140, 32)
        color_inactive = pygame.Color('LIGHTSKYBLUE')
        color_active = pygame.Color('DODGERBLUE')
        color = color_inactive
        enter_btn = btn2('Valider', 'Nom', pos_init_x + 300, pos_init_y + 60, 33, pygame.Color('DARKBLUE'),
                        pygame.Color('WHITE'), pygame.Color('THISTLE'), pygame.Color('FIREBRICK'))
        enter_btn.set_visible(True)

        active = False
        texte_saisi[i] = ''
        done = False

        clock = pygame.time.Clock()

        while not done:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if enter_btn.inside_pos(pos):
                        print(texte_saisi[i])
                        if i == nb_joueurs - 1:
                            main(texte_saisi)
                        else:
                            done = 1

                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive

                elif event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()

                    if enter_btn.inside_pos(pos):
                        enter_btn.set_ismousedown(True)
                    else:
                        enter_btn.set_ismousedown(False)

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(texte_saisi[i])
                            texte_saisi[i] = ''
                        elif event.key == pygame.K_BACKSPACE:
                            texte_saisi[i] = texte_saisi[i][:-1]
                        else:
                            texte_saisi[i] += event.unicode

            win.fill((30, 30, 30))

            font = pygame.font.Font(None, 28)
            txt = font.render("Entrez le nom du joueur {}".format(i + 1), True, (255, 255, 255))
            win.blit(txt, (pos_init_x, pos_init_y))

            # Render the current text.
            txt_surface = font.render(texte_saisi[i], True, color)
            # Resize the box if the text is too long.
            input_box_width = max(250, txt_surface.get_width() + 10)
            input_box.w = input_box_width
            # Blit the text.
            win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(win, color, input_box, 2)
            # Blit the Btn
            enter_btn.draw(win)

            pygame.display.update()


pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.update()

while True:
    choix_nb_joueurs()
