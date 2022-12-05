from player import *


class Game:
    def __init__(self, number_of_players, on_turn, sleeping_queens, cards, awoken_queens, cards_discarded_last_turn):
        self.game_state = GameState(number_of_players, on_turn, sleeping_queens, cards, awoken_queens,
                                    cards_discarded_last_turn)

        self.sleeping_queens = SleepingQueens()  # 4x 5pts; 4x 10pts; 3x 15pts; 1x 20pts
        self.awoken_queens = AwokenQueens()
        # inicializovat ostatne karty do array? a este ich premiesat a rozdat hracom
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
