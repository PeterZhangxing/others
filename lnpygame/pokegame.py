import random

class Card(object):

    def __init__(self,suit_id,rank_id):
        '''
        初始化一张扑克牌
        :param suit_id:牌的花色
        :param rank_id:牌的大小
        '''
        self.rank_id = rank_id
        self.suit_id = suit_id

        self.get_rank(rank_id)
        self.get_suit(suit_id)

        self.short_name = self.get_short_name()
        self.long_name = self.get_long_name()

    def get_rank(self,rank_id):
        if rank_id == 1:
            self.rank = "Ace"
            self.value = 1
        elif rank_id == 11:
            self.rank = "Jack"
            self.value = 10
        elif rank_id == 12:
            self.rank = "Queen"
            self.value = 10
        elif rank_id == 13:
            self.rank = "King"
            self.value = 10
        elif 2 <= rank_id <= 10:
            self.rank = str(rank_id)
            self.value = rank_id
        else:
            self.rank = "ErrorRank"
            self.value = -1

    def get_suit(self,suit_id):
        if suit_id == 1:
            self.suit = "Diamonds"
        elif suit_id == 2:
            self.suit = "Hearts"
        elif suit_id == 3:
            self.suit = "Spades"
        elif suit_id == 4:
            self.suit = "Clubs"

    def get_short_name(self):
        if self.rank == '10':
            sn = self.rank + self.suit[0]
        else:
            sn = self.rank[0] + self.suit[0]
        return sn

    def get_long_name(self):
        ln = self.rank + " of " + self.suit
        return ln

    def __str__(self):
        return self.long_name


def create_deck():
    '''
    生成52张扑克
    :return:
    '''
    deck = []
    for suit_id in range(1, 5):
        for rank_id in range(1, 14):
            deck.append(Card(suit_id, rank_id))
    return deck

def got_rand_poke(deck,num):
    '''
    从一副poke中随机获取指定张数的poke
    :param deck:
    :param num:
    :return:
    '''
    rand_poke = random.choices(deck,k=num)
    return rand_poke


if __name__ == '__main__':
    mypokes = create_deck()
    # print(mypokes)
    res = got_rand_poke(create_deck(),10)
    for i in res:
        print(i)