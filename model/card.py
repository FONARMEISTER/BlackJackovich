

card_name_to_score = {
    "2"     : 2,
    "3"     : 3,
    "4"     : 4,
    "5"     : 5,
    "6"     : 6,
    "7"     : 7,
    "8"     : 8,
    "9"     : 9,
    "10"    : 10,
    "JACK"  : 10,
    "QUEEN" : 10,
    "KING"  : 10,
    "ACE"   : 11
}

class Card:

    def __init__(self, name, suit):
        self.name = name
        self.suit = suit

    def get_score(self):
        return card_name_to_score[self.name]
