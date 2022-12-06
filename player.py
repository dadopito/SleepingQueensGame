from typing import *
from data_types import CardType, Card, HandPosition, Position, AwokenQueenPosition, SleepingQueenPosition
from hand import Hand
from queens import QueenCollection


class PlayerState:
    def __init__(self, cards: List, awoken_queens: QueenCollection):
        self.cards = cards
        self.awoken_queens = awoken_queens


class Player:
    def __init__(self, cards: List[Card], player_id: int):
        self.awoken_queens = QueenCollection()
        self.hand = Hand(player_id, cards)
        self.player_id = player_id

    def play(self, cards: List[HandPosition], target_queen: None | SleepingQueenPosition | AwokenQueenPosition = None):
        # select cards to be played
        picked_cards = self.hand.pickCards(cards)

        if picked_cards is None:
            # do nothing?
            ...
        elif picked_cards[0].card_type == CardType.Number:
            # Number cards
            if self.evaluateNumberedCards(picked_cards):
                # go to Hand and play the move
                self.hand.removePickedCardsAndRedraw()
            else:
                # can't do exchange with selected cards
                ...
        else:
            # Special cards; picked_cards should contain only one card
            if picked_cards[0].card_type == CardType.King:
                if target_queen is not None:
                    self.moveQueen(target_queen)
            elif picked_cards[0].card_type == CardType.Knight:
                pass
            elif picked_cards[0].card_type == CardType.SleepingPotion:
                pass
            elif picked_cards[0].card_type == CardType.Dragon:
                pass
            elif picked_cards[0].card_type == CardType.MagicWand:
                pass

    def evaluateNumberedCards(self, cards: List[Card]) -> bool:
        number_of_cards = len(cards)
        if number_of_cards == 1:
            return True
        elif number_of_cards == 2:
            if cards[0].card_type.name == cards[1].card_type.name and cards[0].value == cards[1].value:
                return True
        else:
            value_array = []
            for index in range(len(cards)):
                value_array.append(cards[index].value)
            maximum_value = max(value_array)
            value_array.remove(maximum_value)
            if sum(value_array) == maximum_value:
                return True
        return False

    def getPlayerState(self) -> PlayerState:
        return PlayerState(self.hand.getCards(), self.awoken_queens)

    def evaluateAttack(self, defense_card: CardType, target_queen: Position, target_player_idx: int) -> bool:
        pass

    def moveQueen(self, target_queen: Position) -> bool:
        pass


# class EvaluateAttack:
#     def __init__(self, defense_card: CardType):
#         self.defense_card_type = defense_card
#
#     def play(self, target_queen: Position, target_player_idx: int) -> bool:
#         pass


# class EvaluateNumberedCards:
#     def play(self, cards: List[Card]) -> bool:
#         pass