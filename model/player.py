from card import card_name_to_score

class Player:
    
    def __init__(self, id):
        self.id = id
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_score(self):
        score = 0
        aces_count = 0
        for card in self.cards:
            if card.name != "ACE":
                score += card_name_to_score[card.name]
            else:
                aces_count += 1
        while (aces_count > 0):
            if (score + 11 < 21):
                score += 11
            else:
                score += 1
            aces_count -= 1
        return score