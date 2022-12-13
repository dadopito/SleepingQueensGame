from data_types import Card
from typing import List
from random import shuffle

class DrawingAndTrashPile:
    def __init__(self, cards: List[Card]):
        self.drawing_pile = cards
        self._discard_pile = []
        self._cards_discarded_this_turn = []
        # self._cards_to_be_discarded = []

    def discardAndDraw(self, discard: List[Card]) -> List[Card]:
        # TODO
        # self._cards_to_be_discarded = discard
        for card in discard:
            # self._discard_pile.append(card)
            self._cards_discarded_this_turn.append(card)
        drawn_cards = []
        for card in range(len(discard)):
            drawn_cards.append(self.drawing_pile.pop())
        self.newTurn()
        return drawn_cards

    def newTurn(self):
        # TODO
        if len(self.drawing_pile) == 0:
            self.drawing_pile = self._discard_pile
            self._discard_pile = []
            shuffle(self.drawing_pile)
        for card in self._cards_discarded_this_turn:
            self._discard_pile.append(card)
        self._cards_discarded_this_turn = []


    def getCardsDiscardedThisTurn(self) -> List[Card]:
        return self._cards_discarded_this_turn
