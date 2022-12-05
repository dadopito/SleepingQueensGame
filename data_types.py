from typing import *


# all cards: 12 queens, 8 kings, 4 knights, 4 sleeping potions,
# 3 magic wands, 3 dragons, 4 of each number 1 through 10
class Queen:
    def __init__(self, value: int):
        self.type = "Queen"
        self.points = value

    def getPoints(self) -> int:
        return self.points


class CardType:
    card_type_array = ["Number", "King", "Knight", "SleepingPotion",
                       "Dragon", "MagicWand"]

    def __init__(self, number: int):
        self.card_type = self.card_type_array[number]


class Card:
    def __init__(self, number: int, value: int):
        self.type = CardType(number)
        self.value = value


class Position:
    def __init__(self, card_index):
        self.card_index = card_index

    def getCardIndex(self) -> int:
        return self.card_index


class SleepingQueenPosition(Position):
    def __init__(self, card_index):
        super().__init__(card_index)


class AwokenQueenPosition(Position):
    def __init__(self, card_index: int):
        super().__init__(card_index)

    def getPlayerIndex(self) -> int:
        pass


class HandPosition(Position):
    def __init__(self, card_index: int):
        super().__init__(card_index)

    def getPlayerIndex(self) -> int:
        pass


class GameState:
    def __init__(self, number_of_players: int, on_turn: int, sleeping_queens: Set[SleepingQueenPosition],
                 cards: dict[HandPosition, Optional[Card]], awoken_queens: dict[AwokenQueenPosition, Queen],
                 cards_discarded_last_turn: List[Card]):
        self.number_of_players = number_of_players
        self.on_turn = on_turn
        self.sleeping_queens = sleeping_queens
        self.cards = cards
        self.awoken_queens = awoken_queens
        self.cards_discarded_last_turn = cards_discarded_last_turn


class PlayerState:
    def __init__(self, cards: dict[int, Optional[Card]], awoken_queens: dict[int, Queen]):
        self.cards = cards
        self.awoken_queens = awoken_queens
