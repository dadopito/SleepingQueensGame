from enum import Enum
from typing import *


class Queen:
    def __init__(self, value: int):
        self._points = value

    def getPoints(self) -> int:
        return self._points


class CardType(Enum):
    Number = 1
    King = 2
    Knight = 3
    SleepingPotion = 4
    Dragon = 5
    MagicWand = 6


class Card:
    def __init__(self, card_type: CardType, value: int):
        self.card_type = card_type
        self.value = value


class Position:
    def __init__(self, card_index: int):
        self._card_index = card_index

    def getCardIndex(self) -> int:
        return self._card_index


class SleepingQueenPosition(Position):
    def __init__(self, card_index):
        super().__init__(card_index)


class AwokenQueenPosition(Position):
    def __init__(self, card_index: int, player_id: int):
        super().__init__(card_index)
        self._player_id = player_id

    def getPlayerIndex(self) -> int:
        return self._player_id


class HandPosition(Position):
    def __init__(self, card_index: int, player_id: int):
        super().__init__(card_index)
        self._player_id = player_id

    def getPlayerIndex(self) -> int:
        return self._player_id


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
