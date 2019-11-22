import socket
from _thread import *
from Jeu import Jeu
import pickle

server = "127.0.0.1"
port = 5555
compteur_de_joueurs = Jeu.NOMBRE_JOUEURS_REQUIS

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(compteur_de_joueurs)  # blank means unlimited connections
print("Attente d'une connexion. Serveur lancé.")

game = Jeu()


def threaded_client(conn, player):
    conn.send(pickle.dumps(player))
    reply = None

    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            data_key = list(data.keys())[0]
            data_val = list(data.values())[0]

            if data_key == "connexion_joueur":
                game.connexion_joueur(player, data_val)
            elif data_key == "joueur_mise":
                game.joueur_mise(player, data_val)
            elif data_key == "joueur_check":
                game.joueur_check(player)
            elif data_key == "joueur_se_couche":
                game.joueur_se_couche(player)
            elif data_key == "get_game":
                game.get_game()
            elif data_key == "lancer_partie":
                game.lancerPartie(player)
            elif data_key == "manche_initialisation":
                game.initialisation_manche(player)
            elif data_key == "preflop":
                game.preflop(player)
            elif data_key == "flop":
                game.flop(player)
            elif data_key == "tournant":
                game.tournant(player)
            elif data_key == "riviere":
                game.riviere(player)
            elif data_key == "devoilement":
                game.devoilement_cartes(player)
            elif data_key == "manche_quittee":
                game.quitter_la_manche(player)

            if data_key != "get_game":
                print("joueur {0}: , data_key {1}, data_val {2}".format(player, data_key, data_val))

            reply = game.repondre_au_client()
            conn.sendall(pickle.dumps(reply))
        except Exception as e:
            print(str(e))
            break

    print("Connexion perdue")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connecté à:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
