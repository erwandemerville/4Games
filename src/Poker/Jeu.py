# !/usr/bin/python3.7
# -*-coding:Utf-8 -*

import random
import time
from Poker.definir_gagnant import PokerHelper

nb_joueurs = 0

class Carte:
    # Classe représentant une carte. Une carte possède un symbole (0 à 3, pique, carreau, coeur ou trèfle) et une
    # valeur (0 à 12, 10 = valet, 11 = dame, 12 = roi).
    def __init__(self, symbole, valeur):
        self.symbole = symbole
        self.valeur = valeur

    def GetValeur(self):
        return self.valeur

    def GetSymbole(self):
        return self.symbole

    def __str__(self):
        return '(symbole:' + str(self.symbole) + ', valeur: ' + str(self.valeur) + ')'


class Pot:
    # Pot contenant de l'argent (pour le pot commun de la partie).
    # Attribut : pot_argent (argent contenu dans le pot)
    # Méthodes : retirer_argent (remet le pot à 0 et retourne la valeur du pot avant remise à zéro.)
    # ajouter_argent : Ajouter de l'argent au pot.

    def __init__(self):
        self.pot_argent = 0

    def retirer_argent(self):
        quantite = self.pot_argent
        self.pot_argent = 0
        return quantite

    def ajouter_argent(self, quantite):
        self.pot_argent += quantite


class Pile:
    # Classe représentant une pile de cartes.
    # Un seul attribut : pile_cartes représentant la liste de toutes les cartes.
    # Méthodes :
    # initialiser_pile : Remplir la pile avec toutes le cartes dans l'ordre.
    # melanger_pile : Mélanger la pile aléatoirement
    # piocher_pile : Récupérer le premier élément de la pile et le retirer de la pile.
    def __init__(self):
        self.pile_cartes = []
        self.initialiser_pile()

    def initialiser_pile(self):
        self.pile_cartes.clear()
        # Ajout des 52 cartes dans le pile. (13 cartes pour les 4 symboles)
        for i in range(0, 4):
            for j in range(0, 13):
                self.pile_cartes.append(Carte(i, j))

    def melanger_pile(self):
        piletemp = []

        c = 51
        while c >= 0:
            selec = random.randint(0, c)
            piletemp.append(self.pile_cartes[selec])
            self.pile_cartes.remove(self.pile_cartes[selec])
            c -= 1

        self.pile_cartes = piletemp

    def piocher_pile(self):
        return self.pile_cartes.pop(0)


class Joueur:
    def __init__(self, nom, id_joueur, argent=500):
        self.nom = nom
        self.id = id_joueur
        self.argent = argent
        self.estHorsjeu = False

        self.liste_cartes = []

        self.estDonneur = False
        self.estPetiteBlinde = False
        self.estGrosseBlinde = False

        self.aChecke = False
        self.estCouche = False
        self.aAll_In = False

        self.derniere_action_mise = ""  # Spécifie si le joueur est couché, a checké, a augmenté la mise, etc.
        self.valeur_derniere_mise = 0
        self.augmentation_mise_actuelle = 0

        self.resultat_manche = None

    def obtenir_resultat_main(self, cartes_communes):
        # Obtenir un résultat contenant le score de la main du joueur en comparaison avec les cartes communes.
        liste_cartes = self.liste_cartes + cartes_communes
        resultat = PokerHelper.GetBestChoise(liste_cartes)
        # resultat = valueHand(cartes_communes, self.liste_cartes)
        self.resultat_manche = resultat

    def retirer_argent(self, quantite):
        # Retire une quantité d'argent donnée à ce que possède le joueur.
        # S'il ne reste plus rien au joueur, on considère qu'il a "All_In".
        if self.argent >= quantite:
            self.argent -= quantite

            if self.argent == quantite:
                self.aAll_In = True

    def ajouter_argent(self, quantite):
        # Ajouter de l'argent au joueur
        self.argent += quantite

    def definir_derniere_mise(self, derniere_action_mise, argent_mise):
        # Change la valeur de la dernière mise, à savoir l'action effectuée et la valeur de la mise

        self.derniere_action_mise = derniere_action_mise
        self.valeur_derniere_mise = argent_mise

        if self.derniere_action_mise == "Relance":
            self.augmentation_mise_actuelle += 1

    def se_couche(self):
        # Passe l'état "couché" du joueur sur "Oui"
        self.estCouche = True
        self.derniere_action_mise = "Couche"

    def check(self):
        self.aChecke = True
        self.derniere_action_mise = "Check"

    def reinit_joueur(self):
        # Si le joueur n'est pas hors-jeu, réinitialise toutes ses caractéristiques.
        if not self.estHorsjeu:
            self.liste_cartes = []
            self.estCouche = False
            self.aAll_In = False
            self.valeur_derniere_mise = ""
            self.estDonneur = False
            self.estPetiteBlinde = False
            self.estGrosseBlinde = False
            self.aChecke = False

            self.augmentation_mise_actuelle = 0
            self.resultat_manche = None

    def ajouter_carte(self, carte):
        # Ajoute une carte au joueur s'il a moins de deux cartes.
        if len(self.liste_cartes) < 2:
            self.liste_cartes.append(carte)
            return True
        else:
            return False


class Jeu:
    def __init__(self, nb_j):
        global nb_joueurs
        self.NOMBRE_JOUEURS_REQUIS = nb_j
        nb_joueurs = nb_j

        self.liste_joueurs = []
        self.cartes_communes = []

        self.pot = Pot()  # Pot commun
        self.etat_jeu = "PreparationJeu"
        self.pile = Pile()

        self.id_donneur = -1
        self.ordre_des_joueurs = []  # ID des joueurs triés dans l'ordre de jeu
        self.liste_dernieres_actions = []
        self.liste_id_joueurs_couches = []
        self.id_joueur_enTrainDe_jouer = 0
        self.miseTerminee = False

        # Attributs relatifs aux mises :
        self.mise_initiale = 1  # Valeur de la mise initiale (petite blinde)
        self.ratio_relance = 2  # Une relance multipliera par cette valeur la mise
        self.nombre_relances_max = 3
        self.valeur_Suivre = 0
        self.estCheckAutorise = False
        self.estSuivreAutorise = False
        self.valeur_relance = 0
        self.id_dernier_joueur_relance = -1

        # S'il y a un gagnant, passer à True (pour le dévoilement des cartes) :
        self.gagnant = None

        # Les attributs suivants permettent de stocket la liste des joueurs ayant effectués chacune des requêtes.
        # Cela permet de ne passer à l'étape suivante que lorsque tous les joueurs sont au même stade
        self.liste_requetes_lancement_jeu = set()
        self.liste_requetes_initialisation_manche = set()
        self.liste_requetes_preflop = set()
        self.liste_requetes_flop = set()
        self.liste_requetes_tournant = set()
        self.liste_requetes_riviere = set()
        self.liste_requetes_devoilement_cartes = set()
        self.liste_requetes_fin_tour = set()

        self.CompteurTours = 0
        self.CompteurPreFlop = 0
        self.CompteurFlop = 0
        self.CompteurTournant = 0
        self.CompteurRiviere = 0
        self.devoilement_cartes_compteur = 0
        self.CompteurFinTours = 0

        # Pour le tour "pré-flop", permet de ne pas mettre fin au tour sans que la grosse blinde n'ait pu parler
        self.grosseBlindeAparle = 0

        self.joueurs_cartes = {}

    @staticmethod
    def AfficherCartes(liste_cartes):
        for carte in liste_cartes:
            print(carte)

    def recuperer_liste_cartes(self):
        for id_joueur in self.ordre_des_joueurs:
            self.joueurs_cartes[id_joueur] = self.liste_joueurs[id_joueur].liste_cartes

    def repondre_au_client(self):
        # Cette méthode crée un dictionnaire qui contiendra toutes les données relatives à la partie.
        # Ces informations sont transmises au client.

        donnees_partie = {"etat_jeu": self.etat_jeu}

        # Informations concernant le joueur :

        donnees_joueurs = self.recuperer_donnees_joueurs()
        donnees_partie["joueurs_info"] = donnees_joueurs

        # Récupérer la liste des cartes de chaque joueur dans un tuple :
        joueurs_cartes = {}
        for id_joueur in self.ordre_des_joueurs:
            joueurs_cartes[id_joueur] = self.liste_joueurs[id_joueur].liste_cartes

        donnees_partie["joueurs_cartes"] = joueurs_cartes
        # --------------------------------------------------------------

        # Cartes communes :
        donnees_partie["cartes_communes"] = self.cartes_communes

        # Argent contenu dans le pot commun
        donnees_partie["pot_commun"] = self.pot.pot_argent

        # ID du joueur auquel c'est le tour de jouer
        donnees_partie["id_joueur_doitJouer"] = self.id_joueur_enTrainDe_jouer

        # Etat de la mise
        donnees_partie["miseTerminee"] = self.miseTerminee

        # Informations relatives aux mises
        donnees_partie["mise_initiale"] = self.mise_initiale
        donnees_partie["ratio_relance"] = self.ratio_relance
        donnees_partie["nombre_relances_max"] = self.nombre_relances_max

        donnees_partie["valeur_Suivre"] = self.valeur_Suivre
        donnees_partie["estCheckAutorise"] = self.estCheckAutorise
        donnees_partie["estSuivreAutorise"] = self.estSuivreAutorise
        donnees_partie["valeur_relance"] = self.valeur_relance

        donnees_partie["gagnant"] = self.gagnant

        # Retourner le dictionnaire de données pour le transmettre au client (afin que le joueur reçoive tout)
        return donnees_partie

    def recuperer_donnees_joueurs(self):
        # Cette méthode retourne un dictionnaire de données de chaque joueur, à condition qu'il y ait le nombre de
        # joueurs requis.
        # Chaque joueur correspond lui-même à un dictionnaire de données.

        donnees_joueurs = {}

        if len(self.liste_joueurs) == nb_joueurs:
            for id_joueur in range(nb_joueurs):
                donnees_joueurs[id_joueur] = {}
                joueur = self.liste_joueurs[id_joueur]
                donnees_joueurs[id_joueur]["nom"] = joueur.nom
                donnees_joueurs[id_joueur]["argent"] = joueur.argent

                donnees_joueurs[id_joueur]["derniere_action_mise"] = joueur.derniere_action_mise
                donnees_joueurs[id_joueur]["valeur_derniere_mise"] = joueur.valeur_derniere_mise
                donnees_joueurs[id_joueur]["augmentation_mise_actuelle"] = joueur.augmentation_mise_actuelle

                donnees_joueurs[id_joueur]["estCouche"] = joueur.estCouche
                donnees_joueurs[id_joueur]["estHorsjeu"] = joueur.estHorsjeu
                donnees_joueurs[id_joueur]["aAll_In"] = joueur.aAll_In
                donnees_joueurs[id_joueur]["estDonneur"] = joueur.estDonneur
                donnees_joueurs[id_joueur]["estPetiteBlinde"] = joueur.estPetiteBlinde
                donnees_joueurs[id_joueur]["estGrosseBlinde"] = joueur.estGrosseBlinde
                donnees_joueurs[id_joueur]["aChecke"] = joueur.aChecke

                donnees_joueurs[id_joueur]["liste_cartes"] = joueur.liste_cartes

        return donnees_joueurs

    def connexion_joueur(self, id_joueur, joueur_nom):
        # Ajoute un nouveau joueur associé à un nom et un ID.
        # Le joueur est placé dans la liste des joueurs de la partie.

        joueur = Joueur(str(joueur_nom), id_joueur)
        self.liste_joueurs.append(joueur)

        # S'il y a suffisamment de joueurs, lancement automatique de la partie !
        if len(self.liste_joueurs) == nb_joueurs:
            print("LANCEMENT DE LA PARTIE")
            self.etat_jeu = "LancementJeu"
            self.lancerPartie()

    def deconnexion_joueur(self, id_joueur):
        # Permet de déconnecter un joueur dont l'ID est saisie
        # L'ID du joueur est supprimée de la liste.

        self.liste_joueurs.pop(id_joueur)

    def lancerPartie(self, id_joueur=-1):
        # Si l'ID d'un joueur est spécifié et que l'état du jeu est sur "LancementJeu",
        # le joueur est ajouté à la liste des joueurs ayant effectué une requête de lancement du jeu.
        # Quand le nombre de requêtes de lancement du jeu correspond au nombres de joueurs requis :
        # Accéder au premier tour de jeu !

        if id_joueur == -1:
            pass
        elif self.etat_jeu == "LancementJeu":
            self.liste_requetes_lancement_jeu.add(id_joueur)

            if len(self.liste_requetes_lancement_jeu) == nb_joueurs:
                print("Accès au premier tour")

                # Eviter problèmes de communication (ajouter délai de 1s)
                time.sleep(1)

                self.etat_jeu = "MancheInitialisation"
                self.initialisation_manche()

    def initialisation_manche(self, id_joueur=-1):
        # Cette méthode permet d'initialiser la manche en cours

        if id_joueur == -1 and self.CompteurTours == 0:
            for joueur in self.liste_joueurs:
                joueur.reinit_joueur()

            self.cartes_communes = []
            self.ordre_des_joueurs = []
            self.liste_dernieres_actions = []
            self.liste_id_joueurs_couches = []
            self.id_dernier_joueur_relance = -1

            self.pile.initialiser_pile()
            self.pile.melanger_pile()

            self.maj_id_donneur()
            self.maj_ordre_mises()
            self.init_liste_dernieres_actions()
            self.designer_les_roles()
            self.miseTerminee = False

            self.gagnant = None

            self.CompteurTours += 1

        elif self.etat_jeu == "MancheInitialisation" and id_joueur != -1:
            self.liste_requetes_initialisation_manche.add(id_joueur)

            # Si tous les joueurs ont eu accès au tour d'initialisation, passer à la phase Pré-flop
            if len(self.liste_requetes_initialisation_manche) == nb_joueurs:
                # Aller à la phase Pré-flop
                print("Accès à la phase pré-flop")

                time.sleep(1)  # Délai de 1 seconde

                self.etat_jeu = "PreFlop"
                self.initialiser_tour()
                self.preflop()

    def creer_liste_joueurs_nonHorsJeu(self):
        # Crée une liste des joueurs qui ne sont pas hors jeu

        liste_temp = []
        for id_joueur in range(len(self.liste_joueurs)):
            if not self.liste_joueurs[id_joueur].estHorsjeu:
                liste_temp.append(id_joueur)

        return liste_temp

    def init_liste_dernieres_actions(self):
        # Initialise la liste des mises.

        self.liste_dernieres_actions = []

        for i in range(len(self.liste_joueurs)):
            self.liste_dernieres_actions.append('')

    def maj_id_donneur(self):
        # Le donneur devient le joueur suivant, c-à-d l'ID du donneur augmente de 1.
        # On s'assure que le nouveau donneur ne soit pas hors-jeu

        ok = 0

        if self.etat_jeu == "MancheInitialisation":

            while not ok:
                if len(self.liste_joueurs) - 1 <= self.id_donneur:
                    self.id_donneur = 0

                else:
                    self.id_donneur += 1

                if not self.liste_joueurs[self.id_donneur].estHorsjeu:
                    ok = 1

    def maj_ordre_mises(self):
        # Mettre à joueur la liste d'ordre des mises en fonction du donneur
        # Dans l'ordre : Petite blinde, grosse blinde, les autres joueurs

        if self.etat_jeu == "MancheInitialisation":

            id_petiteBlinde_listeEnJeu = -1  # Initialisation de l'ID

            # Liste des joueurs encore en jeu
            liste_joueurs_enJeu = self.creer_liste_joueurs_nonHorsJeu()
            # Récupérer l'ID du donneur dans la liste des joueurs en jeu
            id_donneur_listeEnJeu = liste_joueurs_enJeu.index(self.id_donneur)

            # Déterminer la petite blinde
            if id_donneur_listeEnJeu == len(liste_joueurs_enJeu) - 1:
                id_joueur_petiteBlinde = 0
            else:
                id_petiteBlinde_listeEnJeu = id_donneur_listeEnJeu + 1
                id_joueur_petiteBlinde = liste_joueurs_enJeu[id_petiteBlinde_listeEnJeu]

            if id_joueur_petiteBlinde == 0:
                self.ordre_des_joueurs = liste_joueurs_enJeu
            else:  # Modifier l'ordre des joueurs en mettant la petite blinde en premier
                self.ordre_des_joueurs = liste_joueurs_enJeu[id_petiteBlinde_listeEnJeu:] + liste_joueurs_enJeu[
                                                                                            :id_petiteBlinde_listeEnJeu]

    def designer_les_roles(self):
        # Désigner le donneur, la petite blinde et la grosse blinde
        # Dans l'ordre des joueurs, le premier est la petite blinde, le second la grosse blinde

        if self.etat_jeu == "MancheInitialisation":
            donneur = self.liste_joueurs[self.id_donneur]  # Récupération du donneur dans la lister des joueurs
            id_joueur_petiteBlinde = self.ordre_des_joueurs[0]
            petiteBlinde = self.liste_joueurs[id_joueur_petiteBlinde]
            id_grosseBlinde = self.ordre_des_joueurs[1]
            grosseBlinde = self.liste_joueurs[id_grosseBlinde]

            donneur.estDonneur = True
            petiteBlinde.estPetiteBlinde = True
            grosseBlinde.estGrosseBlinde = True
            self.id_joueur_enTrainDe_jouer = self.ordre_des_joueurs[0]

    def preflop(self, id_joueur=-1):
        # Etape "pré-flop"
        # Pour chaque joueur (dans l'ordre), piocher 2 cartes

        if id_joueur == -1 and self.CompteurPreFlop == 0:
            for i in range(2):
                for id_joueur in self.ordre_des_joueurs:
                    carte = self.pile.piocher_pile()
                    self.liste_joueurs[id_joueur].ajouter_carte(carte)  # Ajout de la carte

        elif self.etat_jeu == "PreFlop" and id_joueur != -1:
            self.liste_requetes_preflop.add(id_joueur)

            # Quand tous les joueurs ont eu accès au pré-flop
            if len(self.liste_requetes_preflop) == nb_joueurs:
                print("Accès au flop")

                # to prevent the misorder in communication
                time.sleep(1)

                self.etat_jeu = "Flop"
                self.initialiser_tour()
                self.flop()

    def flop(self, id_joueur=-1):
        # FLOP : Ajout de 3 cartes aux cartes communes

        if id_joueur == -1 and self.CompteurFlop == 0:
            if len(self.cartes_communes) == 0:
                for i in range(3):
                    self.cartes_communes.append(self.pile.piocher_pile())

        elif self.etat_jeu == "Flop" and id_joueur != -1:
            self.liste_requetes_flop.add(id_joueur)

            if len(self.liste_requetes_flop) == nb_joueurs:
                print("Accès au Tournant")

                time.sleep(1)

                self.etat_jeu = "Tournant"
                self.initialiser_tour()
                self.tournant()

    def tournant(self, id_joueur=-1):
        # TOURNANT : Ajout d'une carte aux cartes communes

        if id_joueur == -1 and self.CompteurTournant == 0:
            # S'il y a déjà 3 cartes en commun :
            if len(self.cartes_communes) == 3:
                self.cartes_communes.append(self.pile.piocher_pile())

        elif self.etat_jeu == "Tournant" and id_joueur != -1:
            self.liste_requetes_tournant.add(id_joueur)

            if len(self.liste_requetes_tournant) == nb_joueurs:
                print("Accès à la phase Rivière")

                time.sleep(1)

                self.etat_jeu = "Riviere"
                self.initialiser_tour()
                self.riviere()

    def riviere(self, id_joueur=-1):
        # RIVIERE : Ajout d'une carte aux cartes communes

        if id_joueur == -1 and self.CompteurRiviere == 0:
            # S'il y a déjà 4 cartes en commun :
            if len(self.cartes_communes) == 4:
                self.cartes_communes.append(self.pile.piocher_pile())
        elif self.etat_jeu == "Riviere" and id_joueur != -1:
            self.liste_requetes_riviere.add(id_joueur)

            if len(self.liste_requetes_riviere) == nb_joueurs:
                # go to the next step
                print("Accès au dévoilement des cartes")

                time.sleep(1)

                self.etat_jeu = "Devoilement"
                self.devoilement_cartes()

    def devoilement_cartes(self, id_joueur=-1):
        # Cette méthode dévoile les cartes de chaque joueur, défini le gagnant, et donne l'argent du pot au gagnant.

        if id_joueur == -1 and self.devoilement_cartes_compteur == 0:
            # Afficher la main de chaque joueur et calculer leur score
            for joueur in self.liste_joueurs:
                joueur.obtenir_resultat_main(self.cartes_communes)  # Obtenir le score de chaque main
                PokerHelper.PrintCards(joueur.resultat_manche.hands)
                # self.AfficherCartes(joueur.resultat_manche.mains)  # Afficher chaque main

            # Définir le gagnant
            self.gagnant = self.obtenirGagnant()

            # Ajouter l'argent du pot commun à l'argent du joueur ayant gagné, et le retirer du pot
            self.liste_joueurs[self.gagnant.id].ajouter_argent(self.pot.pot_argent)
            self.pot.retirer_argent()

        elif self.etat_jeu == "Devoilement" and id_joueur != -1:
            self.liste_requetes_devoilement_cartes.add(id_joueur)

            # Une fois que tout le monde a eu accès au dévoilement des cartes, retour au tour d'initialisation
            if len(self.liste_requetes_devoilement_cartes) == nb_joueurs:
                print("Retour au tour d'initialisation")

                self.clear_round()
                self.etat_jeu = "MancheInitialisation"
                self.initialisation_manche()

    def quitter_la_manche(self, id_joueur=-1):
        # Méthode appelée lorsque tous les joueurs se sont couchés sauf 1.
        # Récupérer le gagnant et lui attribuer l'argent du pot.

        if id_joueur == -1 and self.CompteurFinTours == 0:
            print("Fin anticipée de la manche")

            # Définir le gagnant
            self.gagnant = self.obtenirGagnant_mancheQuittee()

            self.liste_joueurs[self.gagnant.id].ajouter_argent(self.pot.pot_argent)
            self.pot.retirer_argent()

        elif self.etat_jeu == "MancheQuittee" and id_joueur != -1:
            self.liste_requetes_fin_tour.add(id_joueur)

            if len(self.liste_requetes_fin_tour) == nb_joueurs:
                print("Retour au tour d'initialisation")

                time.sleep(3)

                self.clear_round()
                self.etat_jeu = "MancheInitialisation"
                self.initialisation_manche()

    def obtenirGagnant(self):
        # Méthode permettant de classer les joueurs selon leur score, et de retourner le gagnant, c'est-à-dire le
        # premier joueur de la liste des joueurs classés. La méthode affiche par ailleurs les résultats de chaque
        # joueur lors de la manche

        liste_joueurs_nonCouches = []

        for joueur in self.liste_joueurs:
            if not joueur.estCouche:
                liste_joueurs_nonCouches.append(joueur)

        liste_joueurs_classes = sorted(liste_joueurs_nonCouches,
                                       key=PokerHelper.cmp_to_key(PokerHelper.CompareTwoPlayerHands),
                                       reverse=True)

        print('--------------------- Joueurs classés ---------------------')
        for joueur in liste_joueurs_classes:
            print(joueur.nom)
            print(joueur.resultat_manche)

        gagnant = liste_joueurs_classes[0]

        print(gagnant.resultat_manche)

        return gagnant

    def obtenirGagnant_mancheQuittee(self):
        # Fonction retournant le seul joueur n'étant pas couché.
        # Fonction appelée pour retourner le gagnant lorsque tous les autres joueurs se couchent.

        for joueur in self.liste_joueurs:
            couche = False
            for id_joueur in self.liste_id_joueurs_couches:
                if joueur.id == id_joueur:
                    couche = True

            if not couche:
                return joueur

    def EstMonTour(self, id_joueur):
        # Retourne TRUE si c'est au tour du joueur dont l'id est id_joueur de jouer

        if self.id_joueur_enTrainDe_jouer == id_joueur:
            return True
        else:
            return False

    def joueur_se_couche(self, id_joueur):
        # Permet de coucher un joueur dont l'ID est passé en paramètre.
        # On vérifie que l'on soit bien dans une phase de jeu dans laquelle l'action est permise

        if self.etat_jeu == "PreFlop" or self.etat_jeu == "Flop" or self.etat_jeu == "Tournant" or \
                self.etat_jeu == "Riviere":
            joueur = self.liste_joueurs[id_joueur]
            joueur.se_couche()
            print("{} s'est couché".format(id_joueur))

            self.liste_id_joueurs_couches.append(id_joueur)

            # Si tous les joueurs sont couchés, la manche est terminée
            if len(self.liste_id_joueurs_couches) == nb_joueurs - 1:
                print("Fin de la manche")
                self.etat_jeu = "MancheQuittee"
                self.quitter_la_manche()
                return

            self.definir_derniere_action_mise_joueur("Couche")
            self.definir_prochain_joueur_a_miser()

    def joueur_check(self, id_joueur):
        # Méthode appelée lorsqu'un joueur checke.
        # Vérifie si l'état du jeu actuel permet cette action et si le check est autorisé (estCheckAutorise = TRUE)

        if self.etat_jeu == "PreFlop" or self.etat_jeu == "Flop" or self.etat_jeu == "Tournant" or \
                self.etat_jeu == "Riviere":
            if self.estCheckAutorise:
                joueur = self.liste_joueurs[id_joueur]
                joueur.check()
                print("{} a checké".format(id_joueur))

                # Mettre à jour la dernière action effectuée durant ce tour
                self.definir_derniere_action_mise_joueur("Check")
                self.definir_prochain_joueur_a_miser()
            else:
                print("Le check n'est pas autorisé")

    def joueur_mise(self, id_joueur, mise):
        # Méthode appelée lorsqu'un joueur mise
        # "mise" est un tuple qui contient 2 éléments : Le type de mise et la valeur de la mise.

        if self.etat_jeu == "PreFlop" or self.etat_jeu == "Flop" or self.etat_jeu == "Tournant" or \
                self.etat_jeu == "Riviere":
            if self.EstMonTour(id_joueur):
                joueur = self.liste_joueurs[id_joueur]  # Récupérer le joueur a partir de son ID
                type_mise = mise[0]
                valeur_mise = mise[1]
                print("{}, {}".format(type_mise, valeur_mise))

                if type_mise == "Suivre":
                    if not self.estSuivreAutorise:
                        print("Impossible de suivre")
                        return

                # En cas de relance, modifier la valeur de la prochaine relance en fonction du ratio indiqué
                if type_mise == "Relance":
                    self.maj_valeur_suivre(valeur_mise)
                    self.maj_valeur_relance(round(valeur_mise * self.ratio_relance))

                # En cas de All_In, changer la valeur de la prochaine mise à effectuer, calculer le nouveau ratio
                # pour la prochaine relance, et indiquer que le joueur est couché
                if type_mise == "All_In":
                    self.maj_valeur_suivre(valeur_mise)
                    self.maj_valeur_relance(round(valeur_mise * self.ratio_relance))
                    joueur.aAll_In = True

                time.sleep(1)

                joueur.definir_derniere_mise(type_mise, valeur_mise)  # Définir dernière mise (classe Joueur)
                joueur.retirer_argent(valeur_mise)
                self.pot.ajouter_argent(valeur_mise)
                self.definir_derniere_action_mise_joueur(type_mise)  # Définir dernière action (classe Jeu)
                self.definir_prochain_joueur_a_miser()

    def maj_valeur_suivre(self, valeur_suivre):
        # Méthode permettant de mettre à jour la valeur d'une mise lorsque le joueur choisit de "Suivre"

        self.valeur_Suivre = valeur_suivre

    def maj_valeur_relance(self, valeur_relance):
        self.valeur_relance = valeur_relance

    def definir_derniere_action_mise_joueur(self, derniere_action_mise):
        # Défini la dernière action du joueur en train de jouer.
        # S'il y a eu relance ou All_In, redéfinie l'ID du dernier joueur à avoir relancé

        self.liste_dernieres_actions[self.id_joueur_enTrainDe_jouer] = derniere_action_mise

        if derniere_action_mise == "Relance" or derniere_action_mise == "All_In":
            self.id_dernier_joueur_relance = self.id_joueur_enTrainDe_jouer

    def maj_autorisation_check(self):
        # Modifie la valeur de estCheckAutorise
        # Si un joueur a relancé, on ne peut pas checker (False), autrement on peut.

        if self.id_dernier_joueur_relance == -1:  # Si pas de relance
            self.estCheckAutorise = True
        else:
            self.estCheckAutorise = False

    def maj_autorisation_suivre(self):
        # Modifie la valeur de estSuivreAutorise
        # S'il n'y a pas eu de relance, on ne peut pas suivre (False), autrement on peut.

        if self.id_dernier_joueur_relance == -1:  # Si pas de relance
            self.estSuivreAutorise = False
        else:
            self.estSuivreAutorise = True

    def tour_de_mise_termine(self):
        # Défini si un tour de mise est terminé ou non. (Retourne TRUE le cas échéant, FALSE sinon)
        # Un tour de mise est terminé si tous les joueurs se sont couchés ou ont checké, ou si l'on revient au joueur
        # ayant relancé.
        # On effectue la vérification si le dernier joueur à avoir joué vient de checker, se coucher ou suivre.

        if self.liste_dernieres_actions[self.id_joueur_enTrainDe_jouer] == 'Check' or self.liste_dernieres_actions[
            self.id_joueur_enTrainDe_jouer] == 'Couche' or \
                self.liste_dernieres_actions[self.id_joueur_enTrainDe_jouer] == 'Suivre':

            compteur_Check_Couche = 0
            # Compter le nombre de joueurs s'étant couchés et ayant checké
            for derniere_action_mise in self.liste_dernieres_actions:
                if derniere_action_mise == "Check" or derniere_action_mise == "Couche":
                    compteur_Check_Couche += 1

            # Si tout le monde s'est couché ou a checké
            if compteur_Check_Couche == len(self.liste_dernieres_actions):
                return True

            # Définir l'ID du prochain joueur devant jouer
            if self.id_joueur_enTrainDe_jouer == len(self.liste_dernieres_actions) - 1:  # Si c'est le dernier joueur
                # de la liste
                id_prochain_joueur = 0
            else:
                id_prochain_joueur = self.id_joueur_enTrainDe_jouer + 1

            # Sauter les joueurs couchés
            id_prochain_joueur = self.idj_sauterJoueursCouches(self.ordre_des_joueurs,
                                                               self.liste_id_joueurs_couches,
                                                               id_prochain_joueur)

            # Si le prochain joueur devant jouer est celui qui a relancé, alors le tour de mise est terminé.
            if self.id_dernier_joueur_relance == id_prochain_joueur:
                if self.etat_jeu == "PreFlop":
                    if self.liste_joueurs[id_prochain_joueur].estGrosseBlinde and not self.grosseBlindeAparle:
                        self.grosseBlindeAparle = True

                        # On modifie l'ID du dernier joueur ayant relancé pour que le tour de mise s'arrête
                        # si le joueur étant la grosse blinde décide de checker ou de se coucher.
                        index = self.ordre_des_joueurs.index(id_prochain_joueur)
                        if index + 1 == len(self.ordre_des_joueurs):
                            self.id_dernier_joueur_relance = self.ordre_des_joueurs[0]
                        else:
                            self.id_dernier_joueur_relance = self.ordre_des_joueurs[index + 1]
                        # ---------------------------------------------------------------------------------

                        self.estSuivreAutorise = False  # La grosse blinde ne peut pas se suivre elle-même
                        self.estCheckAutorise = True  # La grosse blinde peut checker
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return False

    def definir_prochain_joueur_a_miser(self):
        # Défini l'ID du joueur devant jouer.
        # Met à jour l'autorisation de checker et de suivre.

        self.maj_autorisation_check()
        self.maj_autorisation_suivre()

        if self.tour_de_mise_termine():
            self.miseTerminee = True
            self.maj_joueurs_zero_argent()
        else:
            id_joueur_devant_jouer = self.ordre_des_joueurs.index(self.id_joueur_enTrainDe_jouer)
            id_joueur_devant_jouer += 1

            # Si l'ID du prochain joueur à jouer dépasse la liste "ordre_des_joueurs", id du joueur = 0
            if id_joueur_devant_jouer >= len(self.ordre_des_joueurs):
                id_joueur_devant_jouer = 0

            self.id_joueur_enTrainDe_jouer = self.ordre_des_joueurs[id_joueur_devant_jouer]

            # Sauter les joueurs couchés
            self.id_joueur_enTrainDe_jouer = self.idj_sauterJoueursCouches(self.ordre_des_joueurs,
                                                                           self.liste_id_joueurs_couches,
                                                                           self.id_joueur_enTrainDe_jouer)

    @staticmethod
    def idj_sauterJoueursCouches(ordre_des_joueurs, liste_id_joueurs_couches,
                                 id_joueur_devant_jouer):
        # Si le joueur devant jouer actuellement est couché, chercher le prochain joueur dans la liste
        # d'ordre des joueurs qui ne soit pas couché.

        id_prochain_joueur_dans_listeOrdre = ordre_des_joueurs.index(id_joueur_devant_jouer)

        ok = 0

        while not ok:
            ok = 1

            for id_joueur in liste_id_joueurs_couches:
                if id_joueur == ordre_des_joueurs[id_prochain_joueur_dans_listeOrdre]:
                    id_prochain_joueur_dans_listeOrdre += 1
                    ok = 0

                    if id_prochain_joueur_dans_listeOrdre == len(ordre_des_joueurs):
                        id_prochain_joueur_dans_listeOrdre = 0

        id_prochainJoueur_a_jouer = ordre_des_joueurs[id_prochain_joueur_dans_listeOrdre]
        return id_prochainJoueur_a_jouer

    def initialiser_tour(self):
        # Initialisation d'un nouveau tour.
        # Définir le prochain joueur à jouer comme le premier joueur de la liste (ordre_des_joueurs) n'étant pas couché.

        self.miseTerminee = False
        self.id_joueur_enTrainDe_jouer = self.ordre_des_joueurs[0]

        self.id_joueur_enTrainDe_jouer = self.idj_sauterJoueursCouches(self.ordre_des_joueurs,
                                                                       self.liste_id_joueurs_couches,
                                                                       self.id_joueur_enTrainDe_jouer)

        self.init_liste_dernieres_actions()
        self.maj_liste_dernieres_actions_Couches()
        self.id_dernier_joueur_relance = -1
        self.maj_autorisation_check()
        self.maj_autorisation_suivre()

    def maj_liste_dernieres_actions_Couches(self):
        # Initialiser à "Couché" la dernière action de chaque joueur s'étant couché auparavant.

        for id_joueur in self.liste_id_joueurs_couches:
            self.liste_dernieres_actions[id_joueur] = "Couche"

    def maj_joueurs_zero_argent(self):
        # Méthode permettant de passer le statut "aAll_In" des joueurs ayant joué tout leur argent sur TRUE.

        for joueur in self.liste_joueurs:
            if joueur.argent <= 0:
                joueur.aAll_In = True
            joueur.derniere_action_mise = ""
            joueur.valeur_derniere_mise = 0

    def clear_round(self):
        # Réinitialiser les états des listes relatives aux requêtes
        self.liste_requetes_lancement_jeu = set()
        self.liste_requetes_initialisation_manche = set()
        self.liste_requetes_preflop = set()
        self.liste_requetes_flop = set()
        self.liste_requetes_tournant = set()
        self.liste_requetes_riviere = set()
        self.liste_requetes_devoilement_cartes = set()
        self.liste_requetes_fin_tour = set()

        self.CompteurTours = 0
        self.CompteurPreFlop = 0
        self.CompteurFlop = 0
        self.CompteurTournant = 0
        self.CompteurRiviere = 0
        self.devoilement_cartes_compteur = 0
        self.CompteurFinTours = 0

    def get_game(self):
        pass
