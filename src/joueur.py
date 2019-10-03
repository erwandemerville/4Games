class Joueur:
    """Classe définissant un joueur caractérisé par :
    - un pseudo
    - une date de naissance
    - un id
    - un email
    - un mot de passe
    - des crédits (pour le poker)"""

    _nbJoueurs = 0
    def __init__(self, pseudo, dateNaissance, email, mdp):
        #Constructeur de la classe Joueur
        self._pseudo = pseudo
        self._dateNaissance = dateNaissance
        self._id = Joueur._nbJoueurs
        Joueur._nbJoueurs += 1
        self._email = email
        self._mdp = mdp
        self._credits = 1000

   #Getteur et setter pour pseudo
    def _getPseudo(self):
        return self._pseudo
    def _setPseudo(self, nouvPseudo):
        self._pseudo = nouvPseudo
    pseudo = property(_getPseudo, _setPseudo)

    #Getter et setter pour dateNaissance
    def _getDateNaissance(self):
        return self._dateNaissance
    def _setDateNaissance(self, nouvdateNaissance):
        self._dateNaissance = nouvdateNaissance
    dateNaissance = property(_getDateNaissance, _setDateNaissance)

    #Getter et setter pour id
    def _getId(self):
        return self._id
    def _setId(self, nouvId):
        self._id = nouvId
    id = property(_getId, _setId)

    #Getter et setter pour email
    def _getEmail(self):
        return self._email
    def _setEmail(self, nouvEmail):
        self._email = nouvEmail
    email = property(_getEmail, _setEmail)

    #Getter et setter pout mdp
    def _getMdp(self):
        return self._mdp
    def _setMdp(self, nouvMdp):
        self._mdp = nouvMdp
    mdp = property(_getMdp, _setMdp)

    #Getter et setter pour credits
    def _getCredits(self):
        return self._credits
    def _setCredits(self, nouvCredits):
        self._credits = nouvCredits
    credits = property(_getCredits, _setCredits)



