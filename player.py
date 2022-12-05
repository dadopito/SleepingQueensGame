from queens import *


class Player:
    def __init__(self):
        pass

    def play(self, cards: List[Position]):
        pass

    def getPlayerState(self) -> PlayerState:
        pass


class Hand:
    def __init__(self, player_id):
        self.player_id: int = player_id

    def pickCards(self, positions: List[HandPosition]) -> Optional[List[Card]]:
        pass

    def removePickedCardsAndRedraw(self) -> dict[HandPosition, Card]:
        pass

    def returnPickedCards(self):
        pass

    def hasCardOfType(self, type: CardType) -> HandPosition:
        pass

    def getCards(self) -> List[Card]:
        pass


class EvaluateAttack:
    def __init__(self, defense_card: CardType):
        self.defense_card_type = defense_card

    def play(self, target_queen: Position, target_player_idx: int) -> bool:
        pass


class EvaluateNumberedCards:
    def __init__(self):
        pass

    def play(self, cards: List[Cards]) -> bool:
        pass


class DrawingAndTrashPile:
    def __init__(self):
        pass

    def discardAndDraw(self, discard: List[Card]) -> List[Card]:
        pass

    def newTurn(self):
        pass

    def getCardsDiscardedThisTurn(self) -> List[Card]:
        pass
