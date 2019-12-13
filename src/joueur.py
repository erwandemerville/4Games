class Joueur:
    """Classe définissant un joueur caractérisé par :
    - un pseudo
    - un id
    - un mot de passe
    - des crédits (pour le poker)"""

    _nbJoueurs = 0

    def __init__(self, pseudo, mdp):
        # Constructeur de la classe Joueur
        self._pseudo = pseudo
        self._id = Joueur._nbJoueurs
        Joueur._nbJoueurs += 1
        self._mdp = mdp
        self._score_poker = 0
        self._credits = 1000

    # Getteur et setter pour pseudo
    def _getPseudo(self):
        return self._pseudo

    def _setPseudo(self, nouvPseudo):
        self._pseudo = nouvPseudo

    pseudo = property(_getPseudo, _setPseudo)

    # Getter et setter pour id
    def _getId(self):
        return self._id

    def _setId(self, nouvId):
        self._id = nouvId

    id = property(_getId, _setId)

    # Getter et setter pour mdp
    def _getMDP(self):
        return self._mdp

    def _setMDP(self, nouvMDP):
        self._mdp = nouvMDP

    email = property(_getMDP, _setMDP)

    # Getter et setter pour credits
    def _getCredits(self):
        return self._credits

    def _setCredits(self, nouvCredits):
        self._credits = nouvCredits

    # Getter et setter pour score_poker
    def _getScorePoker(self):
        return self._score_poker

    def _setScorePoker(self, nouvScorePoker):
        self._score_poker = nouvScorePoker

    credits = property(_getCredits, _setCredits)
