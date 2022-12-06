from data_types import HandPosition, Card, CardType
from typing import List, Optional

class Hand:
    def __init__(self, player_id: int, cards: List[Card]):
        self._player_id = player_id
        self._cards = cards
        self._picked_cards = []

    def pickCards(self, positions: List[HandPosition]) -> Optional[List[Card]]:
        for position in positions:
            self._picked_cards.append(self._cards[position.getCardIndex()])
        if self._picked_cards:
            return self._picked_cards
        return None
    def removePickedCardsAndRedraw(self) -> List[Card]:
        if self._picked_cards:
            ...
            drawn_cards = []
            return drawn_cards

    def returnPickedCards(self):
        return self._picked_cards

    def hasCardOfType(self, card_type: CardType) -> HandPosition:
        for index, card in enumerate(self._cards):
            if card.card_type == card_type:
                return HandPosition(index, self._player_id)

    def getCards(self) -> List[Card]:
        return self._cards