from random import shuffle

from player import Player, DrawingAndTrashPile
from queens import *
from data_types import *

class Game:
    def __init__(self, number_of_players, on_turn, sleeping_queens, cards, awoken_queens, cards_discarded_last_turn):
        self.game_state = GameState(number_of_players, on_turn, sleeping_queens, cards, awoken_queens,
                                    cards_discarded_last_turn)

        self.sleeping_queens = QueenCollection()
        queens_points = [5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 20]
        shuffle(queens_points)
        for queen_points in queens_points:
            self.sleeping_queens.addQueen(Queen(queen_points))

        cards = []
        for i in range(8):
            cards.append(Card(CardType.King, -1))
        for i in range(4):
            cards.append(Card(CardType.Knight, -1))
        for i in range(4):
            cards.append(Card(CardType.SleepingPotion, -1))
        for i in range(3):
            cards.append(Card(CardType.MagicWand, -1))
        for i in range(3):
            cards.append(Card(CardType.Dragon, -1))
        for i in range(1, 11):
            for j in range(4):
                cards.append(Card(CardType.Number, i))

        shuffle(cards)

        # TODO doriesit pocet hracov
        self.players = []
        for i in range(4):
            self.players.append(Player(cards[:5], i)) # TODO doriesit player_id
            del cards[:5]

        # cards = drawing pile
        self.drawing_and_trash_pile = DrawingAndTrashPile(cards)

        # a zavolat play na zahranie prveho kola...

    def play(self, player_id: int, cards: List[Position]) -> Optional[GameState]:
        pass


class GameAdaptor:
    pass


class GameObservable:
    def __init__(self):
        pass

    def add(self, observer: ObserverInterface):  # GameObserver??
        pass

    def addPlayer(self, player_id: int, observer: ObserverInterface):
        pass

    def remove(self, observer: ObserverInterface):
        pass

    def notifyAll(self, message: GameState):
        pass


class GamePlayerInterface:
    def __init__(self):
        pass

    def play(self, player: str, cards: str) -> str:
        pass


class GameObserver:
    def __init__(self):
        pass

    def notify(self, message: str):
        pass
