"""
! CE CODE EST BASÉ SUR UN PROGRAMME EXISTANT !
Voici le github d'où est issu le code initial : https://github.com/actruce/Pygame/tree/master/TexasHoldemMultiPlay
Dossier "TexasHoldemMultiPlay".

Voir le fichier Jeu.py pour toutes les explications.

"""


class Result:
    def __init__(self, result_name, score, high_rank, high_suit, hands, kicker=None):
        self.result_name = result_name
        self.score = score
        self.high_rank = high_rank
        self.high_suit = high_suit
        self.hands = hands
        self.kicker = kicker

    def __str__(self):
        result_str = self.result_name + ', (' + str(self.high_suit) + ', ' + str(self.high_rank) + ')'
        result_str = result_str + '\n' + '\n'
        for card in self.hands:
            result_str = result_str + str(card) + '\n'
        return result_str


class PokerHelper:
    ROYAL_STRAIGHT_FLUSH = ['Quinte Flush Royale', 10000]
    BACK_STRAIGHT_FLUSH = ['Quinte Flush Backdoor', 5000]
    STRAIGHT_FLUSH = ['Quinte Flush', 3000]
    FOUR_CARDS = ['Carré', 2000]
    FULL_HOUSE = ['Full', 1000]
    FLUSH = ['Couleur', 800]

    MOUNTAIN = ['Mountain', 500]
    BACK_STRAIGHT = ['Quinte Backdoor', 450]
    STRAIGHT = ['Quinte', 400]

    TRIPLE = ['Brelan', 300]
    TWO_PAIR = ['Double Paire', 200]
    SINGLE_PAIR = ['Une Paire', 100]

    HIGH_CARD = ['Carte haute', 10]

    def __init__(self):
        pass

    # This is for python 3.0 porting
    @staticmethod
    def cmp_to_key(mycmp):
        # 'Convert a cmp= function into a key= function'
        class K:
            def __init__(self, obj, *args):
                self.obj = obj

            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0

            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0

            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0

            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0

            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0

            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0

        return K

    @staticmethod
    def CompareTwoPlayerHands(p1, p2):
        r1 = p1.resultat_manche
        r2 = p2.resultat_manche

        if r1.score > r2.score:
            return 1
        elif r1.score == r2.score:
            print("\n-------- Compare Two Players Cards ------------")
            print(p1.nom)
            for card in r1.hands:
                print(card)
            print('\n')
            print(p2.nom)
            for card in r2.hands:
                print(card)

            if (r1.result_name == PokerHelper.ROYAL_STRAIGHT_FLUSH[0]) or (
                    r1.result_name == PokerHelper.BACK_STRAIGHT_FLUSH[0]):
                return PokerHelper.CompareSuit(r1.high_suit, r2.high_suit)
            elif r1.result_name == PokerHelper.STRAIGHT_FLUSH[0]:
                return PokerHelper.CompareRankSuit(r1, r2)
            elif r1.result_name == PokerHelper.FOUR_CARDS[0]:
                return PokerHelper.CompareRankKicker(r1, r2)
            elif r1.result_name == PokerHelper.FULL_HOUSE[0]:  # Special Function
                return PokerHelper.CompareFullHouseHands(r1.hands, r2.hands)
            elif r1.result_name == PokerHelper.FLUSH[0]:
                return PokerHelper.CompareRankSuit(r1, r2)
            elif (r1.result_name == PokerHelper.MOUNTAIN[0]) or (r1.result_name == PokerHelper.BACK_STRAIGHT[0]):
                return 0
            elif r1.result_name == PokerHelper.STRAIGHT[0]:
                return PokerHelper.CompareRankSuit(r1, r2)
            elif (r1.result_name == PokerHelper.TRIPLE[0]) or (r1.result_name == PokerHelper.SINGLE_PAIR[0]) or (
                    r1.result_name == PokerHelper.HIGH_CARD[0]):
                print('TRIPLE, SINGLE, HIGH')
                return PokerHelper.CompareRankKicker(r1, r2)
            elif r1.result_name == PokerHelper.TWO_PAIR[0]:  # Special Function
                print('TWO PAIR')
                return PokerHelper.CompareTwoPair(r1, r2)
            else:
                print('Something Wrong')

        else:
            print('score less than')
            return -1

    @staticmethod
    def CompareRank(r1, r2):
        if r1 == 0:
            r1 = 100

        if r2 == 0:
            r2 = 100

        if r1 > r2:
            return 1
        elif r1 == r2:
            return 0
        else:
            return -1

    @staticmethod
    def CompareRankSuit(r1, r2):
        r1_rank = r1.high_rank
        r2_rank = r2.high_rank

        r1_suit = r1.high_suit
        r2_suit = r2.high_suit

        if r1_rank == 0:
            r1_rank = 100

        if r2_rank == 0:
            r2_rank = 100

        if r1_rank > r2_rank:
            return 1
        elif r1_rank == r2_rank:
            if r1_suit < r2_suit:
                return 1
            elif r1_suit == r2_suit:
                return 0
            else:
                return -1
        else:
            return -1

    @staticmethod
    def CompareSuit(s1, s2):
        if s1 < s2:
            return 1
        elif s1 == s2:
            return 0
        else:
            return -1

    @staticmethod
    def CompareRankKicker(r1, r2):
        r1_rank = r1.high_rank
        r2_rank = r2.high_rank

        r1_kicker = sorted(r1.kicker, key=lambda x: x.valeur)
        r2_kicker = sorted(r2.kicker, key=lambda x: x.valeur)

        if r1_rank == 0:
            r1_rank = 100

        if r2_rank == 0:
            r2_rank = 100

        kicker_same = True
        if r1_rank > r2_rank:
            print('r1_rank (' + str(r1_rank) + ') > r2_rank (' + str(r2_rank) + ')')
            return 1
        elif r1_rank == r2_rank:
            if len(r1_kicker) != len(r2_kicker):
                print('Abnormal')
                for card in r1_kicker:
                    print(card)
                for card in r2_kicker:
                    print(card)

                return -2  # Abnormal Case!

            for i in range(len(r1_kicker) - 1, -1, -1):
                if r1_kicker[i].valeur > r2_kicker[i].valeur:
                    kicker_same = False
                    print('kicker ' + str(i + 1) + 'th r1 > r2')
                    return 1
                elif r1_kicker[i].valeur == r2_kicker[i].valeur:
                    continue
                else:
                    kicker_same = False
                    print('kicker ' + str(i + 1) + 'th r1 < r2')
                    return -1
            if kicker_same:
                print('all kickers are same')
                return 0
        else:
            print('r1_rank (' + str(r1_rank) + ') < r2_rank (' + str(r2_rank) + ')')
            return -1

    @staticmethod
    def CompareFullHouseHands(h1, h2):
        h1_sorted = sorted(h1, key=lambda x: x.valeur)
        h2_sorted = sorted(h2, key=lambda x: x.valeur)

        h1_triple_rank = 0
        h1_pair_rank = 0

        h2_triple_rank = 0
        h2_pair_rank = 0

        first_card_cnt = 0
        second_card_cnt = 0
        bIsFirstCard = True

        # h1
        for i in range(len(h1_sorted)):
            if i == 0:
                h1_triple_rank = h1_sorted[i].valeur
            if h1_triple_rank != h1_sorted[i].valeur:
                h1_pair_rank = h1_sorted[i].valeur
                bIsFirstCard = False

            if bIsFirstCard:
                first_card_cnt += 1
            else:
                second_card_cnt += 1

        if first_card_cnt < 3:  # Swap
            tmp_pair_rank = h1_triple_rank
            h1_triple_rank = h1_pair_rank
            h1_pair_rank = tmp_pair_rank

        # h2
        for i in range(len(h2_sorted)):
            if i == 0:
                h2_triple_rank = h2_sorted[i].valeur
            if h2_triple_rank != h2_sorted[i].valeur:
                h2_pair_rank = h2_sorted[i].valeur
                bIsFirstCard = False

            if bIsFirstCard:
                first_card_cnt += 1
            else:
                second_card_cnt += 1

        if first_card_cnt < 3:  # Swap
            tmp_pair_rank = h2_triple_rank
            h2_triple_rank = h2_pair_rank
            h2_pair_rank = tmp_pair_rank

        # Let's compare
        if h1_triple_rank == 0:
            h1_triple_rank = 100

        if h2_triple_rank == 0:
            h2_triple_rank = 100

        if h1_pair_rank == 0:
            h1_pair_rank = 100

        if h2_pair_rank == 0:
            h2_pair_rank = 100

        if h1_triple_rank > h2_triple_rank:
            return 1
        elif h1_triple_rank == h2_triple_rank:
            if h1_pair_rank > h2_pair_rank:
                return 1
            elif h1_pair_rank == h2_pair_rank:
                return 0
            else:
                return -1
        else:
            return -1

    @staticmethod
    def CompareTwoPair(r1, r2):
        h1_sorted = sorted(r1.hands, key=lambda x: x.valeur)
        h2_sorted = sorted(r2.hands, key=lambda x: x.valeur)

        r1_kicker = sorted(r1.kicker, key=lambda x: x.valeur)
        r2_kicker = sorted(r2.kicker, key=lambda x: x.valeur)

        h1_first_pair_rank = 0
        h1_second_pair_rank = 0

        h2_first_pair_rank = 0
        h2_second_pair_rank = 0

        bIsFirstCard = True

        # h1
        for i in range(len(h1_sorted)):
            if i == 0:
                h1_first_pair_rank = h1_sorted[i].valeur
            if h1_first_pair_rank != h1_sorted[i].valeur:
                h1_second_pair_rank = h1_sorted[i].valeur
        # h2
        for i in range(len(h2_sorted)):
            if i == 0:
                h2_first_pair_rank = h2_sorted[i].valeur
            if h2_first_pair_rank != h2_sorted[i].valeur:
                h2_second_pair_rank = h2_sorted[i].valeur

        # Let's compare
        if h1_first_pair_rank == 0:
            h1_first_pair_rank = 100

        if h1_second_pair_rank == 0:
            h1_second_pair_rank = 100

        if h1_first_pair_rank < h1_second_pair_rank:
            tmp_pair_rank = h1_second_pair_rank
            h1_second_pair_rank = h1_first_pair_rank
            h1_first_pair_rank = tmp_pair_rank

        if h2_first_pair_rank == 0:
            h2_first_pair_rank = 100

        if h2_second_pair_rank == 0:
            h2_second_pair_rank = 100

        if h2_first_pair_rank < h2_second_pair_rank:
            tmp_pair_rank = h2_second_pair_rank
            h2_second_pair_rank = h2_first_pair_rank
            h2_first_pair_rank = tmp_pair_rank

        print('h1_first_rank: ' + str(h1_first_pair_rank) + ', h1_second_pair_rank: ' + str(h1_second_pair_rank))
        print('h2_first_rank: ' + str(h2_first_pair_rank) + ', h2_second_pair_rank: ' + str(h2_second_pair_rank))

        if h1_first_pair_rank > h2_first_pair_rank:
            print('h1_first_pair_rank (' + str(h1_first_pair_rank) + ') > h2_first_pair_rank (' + str(
                h2_first_pair_rank) + ')')
            return 1
        elif h1_first_pair_rank == h2_first_pair_rank:
            if h1_second_pair_rank > h2_second_pair_rank:
                print('h1_second_pair_rank (' + str(h1_second_pair_rank) + ') > h2_second_pair_rank (' + str(
                    h2_second_pair_rank) + ')')
                return 1
            elif h1_second_pair_rank == h2_second_pair_rank:
                if len(r1.kicker) != len(r2.kicker):
                    print('Something Wrong')
                    return -2
                else:
                    if r1_kicker[0].valeur > r2_kicker[0].valeur:
                        print('r1 kicker rank (' + str(r1_kicker[0].valeur) + ') > r2 kicker rank (' + str(
                            r2_kicker[0].valeur) + ')')
                        return 1
                    elif r1_kicker[0].valeur == r2_kicker[0].valeur:
                        return 0
                    else:
                        return -1
            else:
                print('h1_second_pair_rank (' + str(h1_second_pair_rank) + ') < h2_second_pair_rank (' + str(
                    h2_second_pair_rank) + ')')
                return -1
        else:
            return -1

    @staticmethod
    def GetBestChoise(cards):
        straight_list = []
        flush_list = []
        straight_flush_list = []
        multi_bin_list = {}
        result = None

        straight_list = PokerHelper.GetStraightCards(cards)
        flush_list = PokerHelper.GetFlushCards(cards)
        multi_bin_list = PokerHelper.GetMultiBins(cards)

        if straight_list is not None:
            straight_flush_list = PokerHelper.GetFlushCards(straight_list)
            if straight_flush_list is not None:
                # Check "Straight-Flush"
                sorted_result = sorted(straight_flush_list, key=lambda x: x.symbole)

                # Royal-Straight-Flush!!!
                if sorted_result[len(sorted_result) - 1].valeur == 12 \
                        and sorted_result[0].valeur == 0:

                    # Becareful Here
                    if len(sorted_result) > 5:
                        for card in sorted_result:
                            if card.valeur <= 8:
                                sorted_result.pop()

                    result = Result(PokerHelper.ROYAL_STRAIGHT_FLUSH[0],
                                    PokerHelper.ROYAL_STRAIGHT_FLUSH[1],
                                    0,
                                    sorted_result[0].symbole,
                                    sorted_result)
                    return result

                # Back-Straight-Flush!!!
                elif sorted_result[0].valeur == 0:
                    # Becareful Here
                    if len(sorted_result) > 5:
                        for card in sorted_result:
                            if card.valeur >= 5:
                                sorted_result.pop()

                    result = Result(PokerHelper.BACK_STRAIGHT_FLUSH[0],
                                    PokerHelper.BACK_STRAIGHT_FLUSH[1],
                                    0,
                                    sorted_result[0].symbole,
                                    sorted_result)

                    return result

                # Straight-Flush
                else:
                    # Becareful Here
                    new_list = []
                    if len(sorted_result) > 5:
                        for i in range(len(sorted_result) - 1, len(sorted_result) - 5, -1):
                            new_list.append(sorted_result[i])
                    else:
                        new_list = sorted_result[:]

                    result = Result(PokerHelper.STRAIGHT_FLUSH[0],
                                    PokerHelper.STRAIGHT_FLUSH[1],
                                    new_list[len(new_list) - 1].valeur,
                                    new_list[0].symbole,
                                    new_list)

                    return result

        # Check Four-Cards
        for item in multi_bin_list.values():
            if len(item) >= 4:
                result = Result(PokerHelper.FOUR_CARDS[0],
                                PokerHelper.FOUR_CARDS[1],
                                item[0].valeur,
                                item[0].symbole,
                                item,
                                PokerHelper.GetKicker(item, cards, 1))
                return result

        # Check Full-House
        triple_list = []
        pair_list = []

        for item in multi_bin_list.values():
            if len(item) >= 3:
                for card in item:
                    triple_list.append(card)
            elif len(item) >= 2:
                for card in item:
                    pair_list.append(card)

        pair_list = sorted(pair_list, key=lambda x: x.valeur)

        if len(triple_list) > 0 and len(pair_list) > 0:
            safe_triple_list = []

            if triple_list[0].valeur == 0:
                safe_triple_list = triple_list[0:3:1]
            else:
                safe_triple_list = triple_list[len(triple_list) - 3: len(triple_list):1]

            new_list = safe_triple_list + pair_list[len(pair_list) - 2: len(pair_list):1]

            result = Result(PokerHelper.FULL_HOUSE[0],
                            PokerHelper.FULL_HOUSE[1],
                            safe_triple_list[0].valeur,
                            safe_triple_list[0].symbole,
                            new_list)

            return result

        if flush_list is not None:
            # Check normal Flush
            sorted_result = sorted(flush_list, key=lambda x: x.valeur)

            # Becareful Here
            new_list = []
            if len(sorted_result) > 5:
                for i in range(len(sorted_result) - 1, len(sorted_result) - 5, -1):
                    new_list.append(sorted_result[i])
            else:
                new_list = sorted_result[:]

            result = Result(PokerHelper.FLUSH[0],
                            PokerHelper.FLUSH[1],
                            new_list[len(new_list) - 1].valeur,
                            new_list[0].symbole,
                            new_list)
            return result

        if straight_list is not None:
            # Check normal Straight
            sorted_result = sorted(straight_list, key=lambda x: x.valeur)
            distinct_straight_list = PokerHelper.GetDistinctStraightCards(sorted_result)
            exact5_straight_list = PokerHelper.GetExact5_StraightCards(distinct_straight_list)

            # Moutain
            if sorted_result[len(sorted_result) - 1].valeur == 12 \
                    and sorted_result[0].valeur == 0:
                result = Result(PokerHelper.MOUNTAIN[0],
                                PokerHelper.MOUNTAIN[1],
                                exact5_straight_list[0].valeur,
                                exact5_straight_list[0].symbole,
                                exact5_straight_list)  # return only distinct straight hands
                return result

            # Back-Straight!!!
            elif sorted_result[0].valeur == 0:
                result = Result(PokerHelper.BACK_STRAIGHT[0],
                                PokerHelper.BACK_STRAIGHT[1],
                                exact5_straight_list[0].valeur,
                                exact5_straight_list[0].symbole,
                                exact5_straight_list)  # return only distinct straight hands
                return result
            # normal Straight
            else:
                result = Result(PokerHelper.STRAIGHT[0],
                                PokerHelper.STRAIGHT[1],
                                exact5_straight_list[len(exact5_straight_list) - 1].valeur,
                                exact5_straight_list[len(exact5_straight_list) - 1].symbole,
                                exact5_straight_list)  # return only distinct straight hands
                return result

        # Triple & Two-Pair & One-Pair
        triple_list = []
        pair_list = []

        for item in multi_bin_list.values():
            if len(item) >= 3:
                for card in item:
                    triple_list.append(card)
            elif len(item) >= 2:
                for card in item:
                    pair_list.append(card)

        pair_list = sorted(pair_list, key=lambda x: x.valeur)

        if len(triple_list) > 0:
            if triple_list[0].valeur == 0:
                safe_triple_list = triple_list[0:3:1]
            else:
                safe_triple_list = triple_list[len(triple_list) - 3: len(triple_list):1]

            result = Result(PokerHelper.TRIPLE[0],
                            PokerHelper.TRIPLE[1],
                            safe_triple_list[0].valeur,
                            safe_triple_list[0].symbole,
                            safe_triple_list,
                            PokerHelper.GetKicker(safe_triple_list, cards, 2))
            return result
        elif len(pair_list) >= 4:

            high_pair_list = []
            if pair_list[0].valeur == 0:
                high_pair_list = pair_list[0:2:1]
            else:
                high_pair_list = pair_list[len(pair_list) - 2: len(pair_list):1]

            safe_pair_list = PokerHelper.GetDistinctTwoPairs(pair_list)
            result = Result(PokerHelper.TWO_PAIR[0],
                            PokerHelper.TWO_PAIR[1],
                            high_pair_list[len(high_pair_list) - 1].valeur,
                            high_pair_list[len(high_pair_list) - 1].symbole,
                            safe_pair_list,
                            PokerHelper.GetKicker(safe_pair_list, cards, 1))
            return result
        elif len(pair_list) == 2:

            result = Result(PokerHelper.SINGLE_PAIR[0],
                            PokerHelper.SINGLE_PAIR[1],
                            pair_list[len(pair_list) - 1].valeur,
                            pair_list[len(pair_list) - 1].symbole,
                            pair_list,
                            PokerHelper.GetKicker(pair_list, cards, 3))
            return result

        # Check High-Card

        sorted_result = sorted(cards, key=lambda x: x.valeur)

        suit_high = 0
        rank_high = 0

        if sorted_result[0].valeur == 0:
            suit_high = sorted_result[0].symbole
            rank_high = 0
        else:
            suit_high = sorted_result[len(sorted_result) - 1].symbole
            rank_high = sorted_result[len(sorted_result) - 1].valeur

        # high_card = [Card(suit_high, rank_high)]
        result_hand = []
        for card in cards:
            if card.valeur == rank_high and card.symbole == suit_high:
                result_hand.append(card)

        result = Result(PokerHelper.HIGH_CARD[0],
                        PokerHelper.HIGH_CARD[1],
                        suit_high,
                        rank_high,
                        result_hand,
                        PokerHelper.GetKicker(result_hand, cards, 4))

        return result

    @staticmethod
    def GetKicker(hands, cards, kicker_cnt):
        kicker = []
        sorted_cards = sorted(cards, key=lambda x: x.valeur)

        # Ace has the highest priority
        if sorted_cards[0].valeur == 0:
            for hand_card in hands:
                if sorted_cards[0].valeur != hand_card.valeur \
                        and sorted_cards[0].symbole != hand_card.symbole:
                    if len(kicker) < kicker_cnt:
                        kicker.append(sorted_cards[0])

        for i in range(len(sorted_cards) - 1, -1, -1):
            if len(kicker) < kicker_cnt:
                # add a card not belonged in the hands as a kicker
                bContained = False
                for hand_card in hands:
                    if sorted_cards[i].valeur == hand_card.valeur \
                            and sorted_cards[i].symbole == hand_card.symbole:
                        bContained = True

                if bContained == False:
                    kicker.append(sorted_cards[i])

        return kicker

    @staticmethod
    def GetDistinctStraightCards(newlist):
        sorted_result = sorted(newlist, key=lambda x: x.valeur)

        result_list = []

        for card in sorted_result:
            dup_cnt = 0

            if len(result_list) == 0:
                result_list.append(card)
            else:
                for selected_card in result_list:
                    if card.valeur == selected_card.valeur:
                        dup_cnt += 1

                if dup_cnt == 0:
                    result_list.append(card)
        return result_list

    @staticmethod
    def GetDistinctTwoPairs(hands):
        sorted_result = sorted(hands, key=lambda x: x.valeur)
        result_list = []

        for card in sorted_result:
            if card.valeur == 0:
                result_list.append(card)

        for i in range(len(sorted_result) - 1, -1, -1):
            if (len(result_list) < 4):
                result_list.append(sorted_result[i])

        return result_list

    @staticmethod
    def GetStraightCards(newlist):
        sorted_list = sorted(newlist, key=lambda x: x.valeur)

        # Check Straight
        bStraight = False
        straight_list = []
        for i in range(len(sorted_list)):
            current_suit_no = sorted_list[i].valeur
            straight_list = []
            straight_list.append(sorted_list[i])

            for j in range(i + 1, len(sorted_list)):
                if sorted_list[j].valeur == current_suit_no + 1:
                    current_suit_no += 1
                    straight_list.append(sorted_list[j])
                # add duplicate cards
                elif sorted_list[j].valeur == current_suit_no:
                    straight_list.append(sorted_list[j])
                # Very Important Here
                if sorted_list[j].valeur == 12 and sorted_list[j - 1].valeur == 11:
                    # add aces for Back Straight
                    idx = 0
                    while 1:
                        if sorted_list[idx].valeur == 0:
                            if sorted_list[idx] not in straight_list:
                                straight_list.append(sorted_list[idx])
                            idx += 1
                        else:
                            break

            # Get the distint list
            distinct_straight_cnt = 0
            dup_cnt = 0
            for i in range(len(straight_list)):
                distinct_straight_cnt += 1
                suit_no = straight_list[i].valeur
                for j in range(i + 1, len(straight_list)):
                    if suit_no == straight_list[j].valeur:
                        dup_cnt += 1
                    else:
                        break

            if len(straight_list) - dup_cnt >= 5:
                bStraight = True
                PokerHelper.PrintCards(straight_list)
                return straight_list

        return None

    @staticmethod
    def GetExact5_StraightCards(newlist):
        sorted_list = sorted(newlist, key=lambda x: x.valeur)
        result_list = []

        # check mountain
        if sorted_list[0].valeur == 0 and sorted_list[len(sorted_list) - 1].valeur == 12:
            result_list.append(sorted_list[0])

            for i in range(len(sorted_list) - 4, len(sorted_list), 1):
                result_list.append(sorted_list[i])

            return result_list

        else:
            for card in sorted_list:
                bContained = False

                for selected_card in result_list:
                    if card.valeur == selected_card.valeur:
                        bContained = True

                if bContained == False and len(result_list) < 5:
                    result_list.append(card)

            return result_list

    @staticmethod
    def GetFlushCards(newlist):
        sorted_list = sorted(newlist, key=lambda x: x.symbole)
        # PokerHelper.PrintCards(sorted_list)  # print sorted list

        spade_cnt = 0
        diamond_cnt = 0
        heart_cnt = 0
        club_cnt = 0

        for card in sorted_list:
            current_rank = card.symbole
            if current_rank == 0:
                spade_cnt += 1
            elif current_rank == 1:
                diamond_cnt += 1
            elif current_rank == 2:
                heart_cnt += 1
            elif current_rank == 3:
                club_cnt += 1

        collect_rank = 0
        bFlush = False

        # Flust - Spades
        if spade_cnt >= 5:
            collect_rank = 0
            bFlush = True
        elif diamond_cnt >= 5:
            collect_rank = 1
            bFlush = True
        elif heart_cnt >= 5:
            collect_rank = 2
            bFlush = True
        elif club_cnt >= 5:
            collect_rank = 3
            bFlush = True

        flush_list = []
        if bFlush:
            for card in sorted_list:
                if card.symbole == collect_rank:
                    flush_list.append(card)

            PokerHelper.PrintCards(flush_list)

            return flush_list
        else:
            return None

    @staticmethod
    def GetMultiBins(newlist):
        sorted_list = sorted(newlist, key=lambda x: x.valeur)

        multi_bin_array = {x: [] for x in range(13)}

        # put the card into the right bin
        for card in sorted_list:
            suit_no = card.valeur
            list(multi_bin_array.values())[suit_no].append(card)

        return multi_bin_array

    @staticmethod
    def PrintCards(card_list):
        for card in card_list:
            print(card)
