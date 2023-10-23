from enum import Enum
from random import shuffle
from player import Player
from card import card_name_to_score, Card

class State(Enum):
    BET = 1,
    DEAL = 2,
    RES = 3

DEALER_LIMIT = 17

class Game:

    def __init__(self, id, player_id, dealer_id):
        self.id = id
        self.deck = shuffle([Card(i,j) for i in card_name_to_score.keys() for j in range(4)])
        self.bank = 0
        self.state = State.BET
        self.player = Player(player_id)
        self.dealer = Player(dealer_id)
        self.winner = None
    
    def make_bet(self, amount):
        # TODO: check state
        self.bank += amount

    def begin(self):
        if (self.state != State.BET):
            raise RuntimeError("Illegal game state")
        self.player.add_card(self.deck.pop())
        self.player.add_card(self.deck.pop())
        self.state = State.DEAL

    def hit_me(self):
        self.player.add_card(self.deck.pop())

    def enough(self):
        dealer_sum = 0
        while(dealer_sum < DEALER_LIMIT):
            card = self.deck.pop()
            dealer_sum += card[0]
            self.dealer.add_card(card)
        self.state = State.RES
        self.winner = self.check_winner()
        
    def check_winner(self):
        player_score = self.player.get_score()
        dealer_score = self.dealer.get_score()
        if (player_score > 21):
            return self.dealer
        if (dealer_score > 21):
            return self.player
        if (player_score > dealer_score):
            return self.player
        return self.dealer