import random

suits = ["♥","♦","♠","♣"]
ranks = ["K","Q","J","10","9","8","7","6","5","4","3","2","A"]
values = {"K" : 10,"Q" : 10,"J" : 10,"10" : 10,
         "9" : 9,"8" : 8, "7" : 7,"6" : 6,"5" : 5,
         "4" : 4,"3" : 3,"2" : 2,"A" : 11
         }

class Card:
    def __init__(self, suit, rank):
        self.rank = ranks
        self.suit = suits
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.hand = []
        self.ace = 0

    def add_card(self, card):
        self.hand.append(card)
        self.value += card.value
        if card.rank == 'A':
            self.ace += 1

    def adjust_ace(self):
        while self.value > 21 and self.ace > 0:
            self.value -= 10
            self.ace -= 1
        
    def show_hand(self, show_all = False):
        if self.name == "Dealer" and not show_all:
            print("庄家的牌：[Hidden]",self.hand[1])
        else:
            print(f"{self.name}的手牌：",', '.join(str(card) for card in self.hand))
            print(f"手牌点数：{self.value}")

class BlaceJack():
    deck = Deck()
    deck.shuffle()

    player = Player("Player")
    dealer = Player("Dealer")

    for _ in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())

    player.show_hand()
    dealer.show_hand()

    while player.value < 21:
        action = input("要牌 or 停牌？（h/s）：").lower()
        if action == 'h':
            player.add_card(deck.deal())
            player.adjust_ace()
            player.show_hand()
        elif action == 's':
            break
        else:
            print("Invalid input!")

    if player.value < 21:
        while dealer.value < 17:
            dealer.add_card(deck.deal())
            dealer.adjust_ace()

    dealer.show_hand(show_all = True)
    player.show_hand()

    if player.value > 21:
        print("庄家胜！")
    elif dealer.value > 21:
        print("玩家胜！")
    elif player.value > dealer.value:
        print("玩家胜！")
    else :
        print("庄家胜！")

BlackJack()
#让我从零敲肯定不太行，这个是学了一遍后自己敲的
