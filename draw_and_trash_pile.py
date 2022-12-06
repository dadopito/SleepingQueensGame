from data_types import Card
from typing import List


class DrawingAndTrashPile:
    def __init__(self, cards: List[Card]):
        self.drawing_pile = cards
        self._discard_pile = []
        self._cards_discarded_this_round = []
        self._cards_to_be_discarded = []

    def discardAndDraw(self, discard: List[Card]) -> List[Card]:
        self._cards_to_be_discarded = discard
        #TODO draw cards or sth
        self.newTurn()

    def newTurn(self):
        pass

    def getCardsDiscardedThisTurn(self) -> List[Card]:
        return self._cards_discarded_this_round
