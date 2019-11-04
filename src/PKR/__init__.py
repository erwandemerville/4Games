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
    temp = t[i]
    t[i] = t[j]
    t[j] = temp

def nearAs(c):
    return (valueHauteur(c) >= 9) or (valueHauteur(c) <= 4)

def detectQuinteFlush(tab):
    Nperm = len(tab);i=0;N = len(tab)
    # Retirer les doublons
    while(i < N):
        if(valueHauteur(tab[i]) == valueHauteur(tab[i+1])):
            permuter2cartes(i+1,N-1,tab)
            N = N - 1
            triCards(tab,N)
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
    for i in range(len(tab)-2):
        if((valueHauteur(tab[i])==valueHauteur(tab[i+1]))and(valueHauteur(tab[i+1])==valueHauteur(tab[i+2]))):
            id_brelan = i
    if(id_brelan == -1):
        return False
    permuter2cartes(id_brelan,len(tab)-1,tab);permuter2cartes(id_brelan+1,len(tab)-2,tab);permuter2cartes(id_brelan+2,len(tab)-3,tab)
    N = N - 3
    for i in range(len(tab)-1):
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
    while(i < N):
        if(valueHauteur(tab[i]) == valueHauteur(tab[i+1])):
            temp = tab[i+1]
            tab[i+1] = tab[N-1]
            tab[N-1] = temp
            N = N - 1
            triCards(tab,N)
    for i in range(N-4):
        if((valueHauteur(tab[i]+1) == valueHauteur(tab[i+1])) and (valueHauteur(tab[i+1]+1) == valueHauteur(tab[i+2])) and (valueHauteur(tab[i+2]+1) == valueHauteur(tab[i+3])) and (valueHauteur(tab[i+3]+1) == valueHauteur(tab[i+4])) ):
            return True
    if((valueHauteur(tab[N-1])==13)and(valueHauteur(tab[1])==1)and(valueHauteur(tab[1])==2)and(valueHauteur(tab[2])==3)and(valueHauteur(tab[3])==4)):
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
            tb[nb_paire] = tab[i]
            tbb[nb_paire] = tab[i+1]
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
            for i in range(len(tab)):
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
    Nperm = len(tab);i=0;N = len(tab)
    # Enlever les doublons
    while(i < N):
        if(valueHauteur(tab[i]) == valueHauteur(tab[i+1])):
            permuter2cartes(i+1,N-1,tab)
            N = N - 1
            triCards(tab,N)
        else:
            i = i+1
    # Calcul de la valeur
    valueForQuinte = -1
    for i in range(N-4):
        if(valueHauteur(tab[i])+1==valueHauteur(tab[i+1])):
            if(valueHauteur(tab[i+1])+1==valueHauteur(tab[i+2])):
                if(valueHauteur(tab[i+2])+1==valueHauteur(tab[i+3])):
                    if(valueHauteur(tab[i+3])+1==valueHauteur(tab[i+4])):
                        valueForQuinte = tab[i+1]
    triCards(tab,Nperm)
    if(valueHauteur(tab[N-1])==13):
        if(valueHauteur(tab[0])==1):
            if(valueHauteur(tab[1])==2):
                if(valueHauteur(tab[2])==3):
                    if(valueHauteur(tab[3])==4):
                        if(valueForQuinte== -1):
                            return 1754
    return 1753 + valueHauteur(valueforQuinte)
def valueFlush(tab,m):
    triCards(tab)
    for i in range(len(tab)-4):
        if( (valueCardByColor(tab[i])==valueCardByColor(tab[i+1])) and (valueCardByColor(tab[i+1])==valueCardByColor(tab[i+2])) ):
            if( (valueCardByColor(tab[i+2])==valueCardByColor(tab[i+3])) and (valueCardByColor(tab[i+3])==valueCardByColor(tab[i+4])) ):
                if( (valueCardByColor(m[0])==valueCardByColor(m[1])) and (valueCardByColor(m[1])==valueCardByColor(tab[i])) ):
                    return 4
                elif(valueCardByColor(m[0])==valueCardByColor(tab[i])):
                    return valueHauteur(m[0]) + 1765
                elif(valueCardByColor(m[1])==valueCardByColor(tab[i])):
                    return valueHauteur(m[0]) + 1765
                return 1765
    triCards(tab)
    return 0
def valueFullHouse(tab):
    return 5
# Fonctions finales

#Détermine la valeur main avec des cartes communes
def valueHandByTable(m,tab):
    tbl = createTempTab(m,tab)
    if(detectQuinteFlush(tab)==2):
        return 4000
    elif(detectQuinteFlush(tab)==1):
        return -1
    elif(detectCarre(tab)):
        return -2
    elif(detectFullHouse(tab)):
        return -3
    elif(detectFlush(tab)):
        return valueFlush(tab,m)
    elif(detectQuinte(tab)):
        return valueQuinte(tab)
    elif(detectBrelan(tab)):
        return valueBrelans(tab,m)
    elif(detectPaire(tab)):
        return valuePaires(tab,m)
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
    
