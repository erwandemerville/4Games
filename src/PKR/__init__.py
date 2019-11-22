import math
# Fonctions réalisés par BendoTv en 2019

def createTempTab(m,table):
    resultat = table.copy()
    resultat.append(m[0]);resultat.append(m[1])
    triCards(resultat)
    return resultat

#Retourne une valeur comprise entre 1 et 13
def valueHauteur(c):
    val = c-100*round(c/100)
    if(val == 1):
        return 13
    else:
        return val - 1

def valueCardByColor(c):
    if(math.trunc(c/100)>= 0 and math.trunc(c/100)<= 3):
        return math.trunc(c/100)
    else:
        return -1

def nbColorInTab(tab,color):
    nb = 0
    for i in tab:
        if(valueCardByColor(i) == color):
            nb = nb + 1
    return nb

def compareCarte(c1,c2):
    return valueHauteur(c1) - valueHauteur(c2)

def isCardInTab(c,tab):
    for i in tab:
        if(c==i):
            return True
    return False

def isCardInHand(c,hand):
    return isCardInTab(c,hand)

def countingNbCardInHand(tab,N,m):
    nb = 0
    for i in range(N):
        if((m[0]==tab[i]) or (m[1]==tab[i])):
            nb = nb + 1
    return nb

def posCardInTab(c,tab):
    for i in range(len(tab)):
        if(isEgal(c,tab[i])):
            return i
    return -1

def permuter2cartes(i,j,t):
    if(len(t)> i or len(t)>j):
        temp = t[i]
        t[i] = t[j]
        t[j] = temp

def nearAs(c):
    return (valueHauteur(c) >= 9) or (valueHauteur(c) <= 4)

def detectQuinteFlush(tab):
    triCards(tab)
    Nperm = len(tab);i=0;N = len(tab);color_dominate = -1
    if(nbColorInTab(tab,1)>=5):
        color_dominate = 1
    elif(nbColorInTab(tab,2)>=5):
        color_dominate = 2
    elif(nbColorInTab(tab,3)>=5):
        color_dominate = 3
    elif(nbColorInTab(tab,0)>=5):
        color_dominate = 0
    else:
        return 0
    # Retirer les cartes n'ayant pas la même couleur 5 fois
    while(i < N):
        if(valueCardByColor(tab[i]) != color_dominate):
            permuter2cartes(i,N-1,tab)
            N = N - 1
            triCards(tab,N)
        else:
            i = i + 1
    for i in range(N-4):
        if((valueHauteur(tab[i])+1 == valueHauteur(tab[i+1])) and (valueCardByColor(tab[i]) == valueCardByColor(tab[i+1])) and nearAs(tab[i]) and nearAs(tab[i+1])):
            if( (valueHauteur(tab[i+1])+1 == valueHauteur(tab[i+2])) and (valueCardByColor(tab[i+1]) == valueCardByColor(tab[i+2])) and nearAs(tab[i+2]) ):
                if( (valueHauteur(tab[i+2])+1 == valueHauteur(tab[i+3])) and (valueCardByColor(tab[i+2]) == valueCardByColor(tab[i+3])) and nearAs(tab[i+3]) ):
                    if( (valueHauteur(tab[i+3])+1 == valueHauteur(tab[i+4])) and (valueCardByColor(tab[i+3]) == valueCardByColor(tab[i+4])) and nearAs(tab[i+4]) ):
                        if( valueHauteur(tab[i+4]) == 4 ):
                            return 1
                        else:
                            return 2
        if((valueHauteur(tab[i])+1 == valueHauteur(tab[i+1])) and (valueCardByColor(tab[i]) == valueCardByColor(tab[i+1])) ):
            if( (valueHauteur(tab[i+1])+1 == valueHauteur(tab[i+2])) and (valueCardByColor(tab[i+1]) == valueCardByColor(tab[i+2]))  ):
                if( (valueHauteur(tab[i+2])+1 == valueHauteur(tab[i+3])) and (valueCardByColor(tab[i+2]) == valueCardByColor(tab[i+3]))  ):
                    if( (valueHauteur(tab[i+3])+1 == valueHauteur(tab[i+4])) and (valueCardByColor(tab[i+3]) == valueCardByColor(tab[i+4])) ):
                        return 1
    if( (valueHauteur(tab[N-1])==13) and (valueHauteur(tab[0])==1) and (valueHauteur(tab[1])==2) and (valueHauteur(tab[2])==3) and (valueHauteur(tab[3])==4) ):
        if( (valueCardByColor(tab[N-1]) == valueCardByColor(tab[0])) and (valueCardByColor(tab[0]) == valueCardByColor(tab[1])) ):
            if( (valueCardByColor(tab[1]) == valueCardByColor(tab[2])) and (valueCardByColor(tab[2]) == valueCardByColor(tab[3])) ):
                return 1
    triCards(tab)
    return 0

def detectCarre(tab):
    for i in range(len(tab)-3):
        if((valueHauteur(tab[i]) == valueHauteur(tab[i+1])) and (valueHauteur(tab[i+1]) == valueHauteur(tab[i+2])) and (valueHauteur(tab[i+2]) == valueHauteur(tab[i+3])) ):
            return True
    return False

def detectFullHouse(tab):
    Nperm = len(tab);N = len(tab)
    id_brelan = -1
    for i in range(N-2):
        if((valueHauteur(tab[i])==valueHauteur(tab[i+1]))and(valueHauteur(tab[i+1])==valueHauteur(tab[i+2]))):
            id_brelan = i
    if(id_brelan == -1):
        return False
    permuter2cartes(id_brelan,len(tab)-1,tab);permuter2cartes(id_brelan+1,len(tab)-2,tab);permuter2cartes(id_brelan+2,len(tab)-3,tab)
    N = N - 3
    for i in range(N-1):
        if(valueHauteur(tab[i]) == valueHauteur(tab[i+1])):
            return True
    triCards(tab)
    return False

def detectFlush(tab):
    triCardsByColor(tab)
    for i in range(len(tab)-4):
        if((valueCardByColor(tab[i]) == valueCardByColor(tab[i+1])) and (valueCardByColor(tab[i+1]) == valueCardByColor(tab[i+2])) and (valueCardByColor(tab[i+2]) == valueCardByColor(tab[i+3])) and (valueCardByColor(tab[i+3]) == valueCardByColor(tab[i+4]))):
            return True
    triCards(tab)
    return False

def detectQuinte(tab):
    Nperm = len(tab);i=0;N=len(tab)
    # Enlever les doublons
    while(i+1 < N):
        if(valueHauteur(tab[i]) == valueHauteur(tab[i+1])):
            permuter2cartes(i+1,N-1,tab)
            N = N - 1
            triCards(tab,N)
        else:
            i = i + 1
    for i in range(N-4):
        if(valueHauteur(tab[i])+1 == valueHauteur(tab[i+1])):
           if(valueHauteur(tab[i+1])+1 == valueHauteur(tab[i+2])):
               if(valueHauteur(tab[i+2])+1 == valueHauteur(tab[i+3])):
                   if(valueHauteur(tab[i+3])+1 == valueHauteur(tab[i+4])):
                       return True
    if(valueHauteur(tab[N-1])==13):
       if(valueHauteur(tab[0])==1):
           if(valueHauteur(tab[1])==2):
               if(valueHauteur(tab[2])==3):
                   if(valueHauteur(tab[3])==4):
                    return True
    triCards(tab,Nperm)
    return False

def detectBrelan(tab):
    for i in range(len(tab)-2):
        if( (valueHauteur(tab[i])==valueHauteur(tab[i+1])) and (valueHauteur(tab[i+1])==valueHauteur(tab[i+2])) ):
            return True
    return False
def nbBrelan(tab):
    value = 0
    for i in range(len(tab)-2):
        if( (valueHauteur(tab[i])==valueHauteur(tab[i+1])) and (valueHauteur(tab[i+1])==valueHauteur(tab[i+2])) ):
            value = value + 1
    return value
def detectPaire(tab):
    for i in range(len(tab)-1):
        if(valueHauteur(tab[i])==valueHauteur(tab[i+1])):
            return True
    return False


def comparatorCards(c):
    return valueHauteur(c)
def triCards(tab,indice_max = -1):
    if(indice_max < 2):
        tab.sort(key=comparatorCards)
    else:
        tabNotSort = []
        while(len(tab) > indice_max):
            tabNotSort.append(tab[len(tab)-1])
            tab.pop(len(tab)-1)
        tabNotSort.reverse()
        tab.sort(key=comparatorCards)
        for element in tabNotSort:
            tab.append(element)
def triCardsByColor(tab):
    tab.sort(key=valueCardByColor)

##Déterminer la valeur :

def valueHauteurs(m):
    return 14 + valueHauteur(m[0]) + valueHauteur(m[1])
def valuePair(m):
    return (valueHauteur(m[0])+3)*10
def valuePairCard(c):
    return (valueHauteur(c)+3)*10
def valuePaires(tab,m):
    tb = []; tbb = [];nb_paire = 0
    for i in range(len(tab)-1):
        if(valueHauteur(tab[i])==valueHauteur(tab[i+1])):
            tb.append(tab[i])
            tbb.append(tab[i+1])
            nb_paire = nb_paire + 1
    triCards(tb);triCards(tbb)
    if(nb_paire > 1):
        ttemp = []
        if(nb_paire == 2):
            ttemp.append(tb[0]);ttemp.append(tb[1]);ttemp.append(tbb[0]);ttemp.append(tbb[1])
        elif(nb_paire == 3):
            ttemp.append(tb[1]);ttemp.append(tb[2]);ttemp.append(tbb[1]);ttemp.append(tbb[2])
        # Calcul de la main
        if(countingNbCardInHand(ttemp,4,m)==0):
            return valuePairCard(tb[0]) + valuePairCard(tb[1]) + valueHauteurs(m) + 161
        elif(countingNbCardInHand(ttemp,4,m)==2):
            return valuePairCard(tb[0]) + valuePairCard(tb[1]) + 161
        elif(countingNbCardInHand(ttemp,4,m)==1):
            card_in_hand = 0
            for i in range(len(ttemp)):
                if(ttemp[i] == m[0]):
                    card_in_hand = m[0]
                elif(ttemp[i] == m[1]):
                    card_in_hand = m[1]
            return valuePairCard(tb[0]) + valuePairCard(tb[1]) + valueHauteurs(m) + 161 - 14 - valueHauteur(card_in_hand)
    else:
        if( (isCardInHand(tb[0],m)) and (isCardInHand(tbb[0],m)) ):
            return valuePairCard(tb[0])
        elif( not(isCardInHand(tb[0],m)) and not(isCardInHand(tbb[0],m)) ):
            return valuePairCard(tb[0]) + valueHauteurs(m)
        elif( (isCardInHand(tb[0],m)) and not(isCardInHand(tbb[0],m)) ):
            return valuePairCard(tb[0]) + valueHauteurs(m) - valueHauteur(tb[0]) - 14
        elif( not(isCardInHand(tb[0],m)) and (isCardInHand(tbb[0],m)) ):
            return valuePairCard(tbb[0]) + valueHauteurs(m) - valueHauteur(tbb[0]) - 14
    return 0

def valueBrelan(c):
    return valuePairCard(c)*10 + 110
def valueBrelans(tab,m):
    tb = []
    for i in range(len(tab)-2):
        if( (valueHauteur(tab[i]) == valueHauteur(tab[i+1])) and (valueHauteur(tab[i+1]) == valueHauteur(tab[i+2])) ):
            tb.append(tab[i]);tb.append(tab[i+1]);tb.append(tab[i+2])
    # Vérifier si les cartes de la main forment un brelan
    if( (isCardInTab(m[0],tb)) and (isCardInTab(m[1],tb)) ):
        return valueBrelan(tb[0])
    elif( not(isCardInTab(m[0],tb)) and not(isCardInTab(m[1],tb)) ):
        return valueBrelan(tb[0]) + valueHauteurs(m)
    elif( (isCardInTab(m[0],tb)) and not(isCardInTab(m[1],tb)) ):
        return valueBrelan(tb[0]) + valueHauteur(m[1])
    elif( not(isCardInTab(m[0],tb)) and (isCardInTab(m[1],tb)) ):
        return valueBrelan(tb[0]) + valueHauteur(m[0])
    return 0
def valueQuinte(tab):
    triCards(tab)
    Nperm = len(tab);i=0;N = len(tab)
    # Enlever les doublons
    while(i+1 < N):
        if(valueHauteur(tab[i]) == valueHauteur(tab[i+1])):
            permuter2cartes(i+1,N-1,tab)
            N = N - 1
            triCards(tab,N)
        else:
            i = i + 1
    # Calcul de la valeur
    valueForQuinte = -1
    for i in range(N-4):
        if(valueHauteur(tab[i])+1==valueHauteur(tab[i+1])):
            if(valueHauteur(tab[i+1])+1==valueHauteur(tab[i+2])):
                if(valueHauteur(tab[i+2])+1==valueHauteur(tab[i+3])):
                    if(valueHauteur(tab[i+3])+1==valueHauteur(tab[i+4])):
                        valueForQuinte = tab[i+1]
    if(valueHauteur(tab[N-1])==13):
        if(valueHauteur(tab[0])==1):
            if(valueHauteur(tab[1])==2):
                if(valueHauteur(tab[2])==3):
                    if(valueHauteur(tab[3])==4):
                        if(valueForQuinte == -1):
                            return 1754
    return 1753 + valueHauteur(valueForQuinte)
def valueFlush(tab,m):
    triCardsByColor(tab)
    for i in range(len(tab)-4):
        if( (valueCardByColor(tab[i])==valueCardByColor(tab[i+1])) and (valueCardByColor(tab[i+1])==valueCardByColor(tab[i+2])) ):
            if( (valueCardByColor(tab[i+2])==valueCardByColor(tab[i+3])) and (valueCardByColor(tab[i+3])==valueCardByColor(tab[i+4])) ):
                if( (valueCardByColor(m[0])==valueCardByColor(m[1])) and (valueCardByColor(m[1])==valueCardByColor(tab[i])) ):
                    return valueHauteurs(m) + 1765
                elif(valueCardByColor(m[0])==valueCardByColor(tab[i])):
                    return valueHauteur(m[0]) + 1765
                elif(valueCardByColor(m[1])==valueCardByColor(tab[i])):
                    return valueHauteur(m[0]) + 1765
                return 1765
    triCards(tab)
    return 1765
def valueFullHouse(tab):
    tb = [-1,-1,-1];id_brelan = -1;N = len(tab)
    # Trouver le meilleur brelan
    for i in range(len(tab)-2):
        if( (valueHauteur(tab[i])==valueHauteur(tab[i+1])) and (valueHauteur(tab[i+1])==valueHauteur(tab[i+2])) ):
            tb[0] = tab[i];tb[1] = tab[i+1];tb[2] = tab[i+2];id_brelan = i
    resultatfinal = valueBrelan(tb[0])
    # Déplacer le brelan dans la partie plus traitée
    permuter2cartes(id_brelan,len(tab)-1,tab);permuter2cartes(id_brelan+1,len(tab)-2,tab);permuter2cartes(id_brelan+2,len(tab)-3,tab)
    # Détecter la meilleur paire
    for i in range(N-4):
        if(valueHauteur(tab[i])==valueHauteur(tab[i+1])):
            tb[0] = tab[i]
            tb[1] = tab[i+1]
    return resultatfinal + valuePairCard(tb[0]) + 1710
def valueCarre(tab,m):
    tb = [-1,-1,-1,-1]
    for i in range(len(tab)-4):
        if( (valueHauteur(tab[i])==valueHauteur(tab[i+1])) and (valueHauteur(tab[i+1])==valueHauteur(tab[i+2])) ):
            if( valueHauteur(tab[i+2])==valueHauteur(tab[i+3]) ):
                tb[0] = tab[i];tb[1] = tab[i+1];tb[2] = tab[i+2];tb[3] = tab[i+3]
    # Vérifier si les cartes de la main forment un brelan
    if(isCardInTab(m[0],tab) and isCardInTab(m[1],tab)):
        return valueHauteur(tb[0]) + 14 + 3579
    elif(not(isCardInTab(m[0],tab)) and not(isCardInTab(m[1],tab))):
        if(valueHauteur(m[0]) > valueHauteur(m[1])):
            return valueHauteur(tb[0]) + 14 + 3579 + valueHauteur(m[0])
        return valueHauteur(tb[0]) + 14 + 3579 + valueHauteur(m[1])
            
    elif(not(isCardInTab(m[0],tab)) and (isCardInTab(m[1],tab))):
        return valueHauteur(tb[0]) + 14 + 3579 + valueHauteur(m[1])
    elif((isCardInTab(m[0],tab)) and not(isCardInTab(m[1],tab))):
        return valueHauteur(tb[0]) + 14 + 3579 + valueHauteur(m[0])
    return 0
def valueQuinteflush(tab):
    triCards(tab)
    Nperm = len(tab);i=0;N = len(tab);color_dominate = -1
    if(nbColorInTab(tab,1)>=5):
        color_dominate = 1
    elif(nbColorInTab(tab,2)>=5):
        color_dominate = 2
    elif(nbColorInTab(tab,3)>=5):
        color_dominate = 3
    elif(nbColorInTab(tab,0)>=5):
        color_dominate = 0
    else:
        return 0
    # Retirer les cartes n'ayant pas la même couleur 5 fois
    while(i < N):
        if(valueCardByColor(tab[i]) != color_dominate):
            permuter2cartes(i,N-1,tab)
            N = N - 1
            triCards(tab,N)
        else:
            i = i + 1
    valueause = -1
    for i in range(N-4):
        if( (valueHauteur(tab[i])+1==valueHauteur(tab[i+1])) and (valueCardByColor(tab[i])==valueCardByColor(tab[i+1])) ):
            if( (valueHauteur(tab[i+1])+1==valueHauteur(tab[i+2])) and (valueCardByColor(tab[i+1])==valueCardByColor(tab[i+2])) ):
                if( (valueHauteur(tab[i+2])+1==valueHauteur(tab[i+3])) and (valueCardByColor(tab[i+2])==valueCardByColor(tab[i+3])) ):
                    if( (valueHauteur(tab[i+3])+1==valueHauteur(tab[i+4])) and (valueCardByColor(tab[i+3])==valueCardByColor(tab[i+4])) ):
                        valueause = tab[i+1]
    if((valueHauteur(tab[N-1])==13) and valueause == -1):
        if(valueHauteur(tab[0])==1):
            if(valueHauteur(tab[1])==2):
                if(valueHauteur(tab[2])==3):
                    if(valueHauteur(tab[3])==4):
                        valueause = tab[0]
    triCards(tab,Nperm)
    return 3619 + valueHauteur(valueause)
# Fonction de tests
def testValueHand():
    # Vérifie qu'une paire < double paire
    assert(valueHand([102,103],[207,307,309,312,11]) < valueHand([102,103],[207,307,302,312,11]))
    assert(valueHand([102,103],[207,307,309,312,11]) < valueHand([102,103],[203,307,302,312,11]))
    # Vérifie qu'une double paire < brelan
    assert(valueHand([102,103],[203,307,302,312,11]) < valueHand([102,103],[202,307,302,312,11]))
    assert(valueHand([102,103],[203,307,302,312,11]) < valueHand([3,103],[203,307,302,312,11]))
    # Vérifie qu'un brelan < quinte
    assert(valueHand([102,103],[202,307,302,312,11]) < valueHand([102,103],[205,304,2,301,11]))
    assert(valueHand([3,103],[203,307,302,312,11]) < valueHand([8,109],[201,303,310,312,11]))
    # Vérifie qu'une quinte < flush
    assert(valueHand([102,103],[205,304,2,301,11]) < valueHand([102,109],[105,104,113,301,311]))
    assert(valueHand([8,109],[201,303,310,312,11]) < valueHand([208,209],[201,303,202,309,211]))
    # Vérifie qu'un flush < full house
    assert(valueHand([102,109],[105,104,113,301,311]) < valueHand([102,309],[102,9,209,301,311]))
    assert(valueHand([208,209],[201,303,202,309,211]) < valueHand([208,8],[201,303,301,101,211]))
    # Vérifie qu'un full house < carre
    assert(valueHand([102,309],[102,9,209,301,311]) < valueHand([109,309],[102,9,209,301,311]))
    assert(valueHand([208,8],[201,303,301,101,211]) < valueHand([208,1],[201,303,301,101,213]))
    # Vérifie qu'un carré < quinte flush
    assert(valueHand([109,309],[102,9,209,301,311]) < valueHand([102,103],[105,104,2,101,11]))
    assert(valueHand([208,1],[201,303,301,101,213]) < valueHand([8,9],[201,303,10,12,11]))
    # Vérifie qu'une quinte flush < quinte flush royale
    assert(valueHand([102,103],[105,104,2,101,11]) < valueHand([113,112],[111,110,2,101,11]))
    assert(valueHand([8,409],[201,303,10,12,11]) < valueHand([1,13],[201,303,10,12,11]))
    # Vérifie que les quinte flush royales valent 4000
    for i in range(4):
        assert(valueHand([13+100*i,12+100*i],[11+100*i,10+100*i,102,1+100*i,406]))
# Fonctions finales

#Détermine la valeur main avec des cartes communes
def valueHandByTable(m,tab):
    tbl = createTempTab(m,tab)
    nb_quinteflush = detectQuinteFlush(tbl)
    if(nb_quinteflush==2):
        return 4000
    elif(nb_quinteflush==1):
        return valueQuinteflush(tbl)
    elif(detectCarre(tbl)):
        return valueCarre(tbl,m)
    elif(detectFullHouse(tbl)):
        return valueFullHouse(tbl)
    elif(detectFlush(tbl)):
        return valueFlush(tbl,m) 
    elif(detectQuinte(tbl)):
        return valueQuinte(tbl)
    elif(detectBrelan(tbl)):
        return valueBrelans(tbl,m)
    elif(detectPaire(tbl)):
        return valuePaires(tbl,m)
    else:
        return valueHauteurs(m)

def valueHand(m,tab):
    if(len(tab)<= 0):
        if(valueHauteur(m[0]) == valueHauteur(m[1])):
            return valuePair(m)
        else:
            return 14 + valueHauteur(m[0]) + valueHauteur(m[1])
    else:
        return valueHandByTable(m,tab)

testValueHand()
