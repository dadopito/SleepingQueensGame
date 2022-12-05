from queens import *


class Player:
    def __init__(self, cards: List[Card], player_id: int):
        self.awoken_queens = QueenCollection()
        self.hand = Hand(player_id, cards)

    def play(self, cards: List[Position]):
        pass

    def getPlayerState(self) -> PlayerState:
        return PlayerState(self.hand.cards, self.awoken_queens)


class Hand:
    def __init__(self, player_id: int, cards: List[Card]):
        self.player_id = player_id
        self.cards = cards

    def pickCards(self, positions: List[HandPosition]) -> Optional[List[Card]]:
        pass

    def removePickedCardsAndRedraw(self) -> dict[HandPosition, Card]:
        pass

    def returnPickedCards(self):
        pass

    def hasCardOfType(self, card_type: CardType) -> HandPosition:
        pass

    def getCards(self) -> List[Card]:
        return self.cards


class EvaluateAttack:
    def __init__(self, defense_card: CardType):
        self.defense_card_type = defense_card

    def play(self, target_queen: Position, target_player_idx: int) -> bool:
        pass


class EvaluateNumberedCards:
    def __init__(self):
        pass

    def play(self, cards: List[Card]) -> bool:
        pass


class DrawingAndTrashPile:
    def __init__(self, cards: List[Card]):
        self.drawing_pile = cards
        self.discard_pile = []
        self.cards_to_be_discarded = []

    def discardAndDraw(self, discard: List[Card]) -> List[Card]:
        self.cards_to_be_discarded = discard
        #TODO potiahnem abo daco
        self.newTurn()

    def newTurn(self):
        pass

    def getCardsDiscardedThisTurn(self) -> List[Card]:
        pass
