from random import shuffle
from draw_and_trash_pile import DrawingAndTrashPile
from player import Player
from data_types import *
from queens import QueenCollection


class GameFinishedStrategy:
    def isFinished(self) -> Optional[int]:
        pass


class Game(GameFinishedStrategy):
    def __init__(self, number_of_players: int):
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

        # TODO number of players and their IDs through GameAdaptor
        self.players = []
        for i in range(number_of_players):
            self.players.append(Player(cards[:5], i+1))
            del cards[:5]

        self.drawing_and_trash_pile = DrawingAndTrashPile(cards)

    def isFinished(self) -> Optional[int]:
        all_queens_awoken = False
        if len(self.sleeping_queens.getQueens()) == 0:
            all_queens_awoken = True

        if 2 <= len(self.players) <= 3:
            total_points = 50
            total_queens = 5
        else: # 4-5 players in the game
            total_points = 40
            total_queens = 4

        winner_player_id = None
        max_player_id = None # player with maximum points if all queens were awoken
        max_player_points = 0
        for player in self.players:
            awoken_queens_collection = player.getPlayerState().awoken_queens.getQueens()
            player_points = 0
            player_queens = 0
            for queen in awoken_queens_collection:
                player_points += queen.getPoints()
                player_queens += 1
            if player_queens >= total_queens or player_points >= total_points:
                winner_player_id = player.player_id
            if max_player_points < player_points:
                max_player_points = player_points
                max_player_id = player.player_id

        if all_queens_awoken:
            return max_player_id
        if winner_player_id is not None:
            return winner_player_id
        return None

    def play(self, player_id: int, cards: List[Position]) -> Optional[GameState]:
        # TODO
        return GameState()


class GameObserver:
    def notify(self, message: str):
        pass


class GameObservable:
    def __init__(self):
        self._observers = dict()

    def add(self, observer: GameObserver):
        if self._observers.get(observer) is None:
            self._observers[observer] = -1

    def addPlayer(self, player_id: int, observer: GameObserver):
        if self._observers.get(observer) is None:
            self._observers[observer] = -1
        for registered_player in self._observers.values():
            if registered_player == player_id:
                return
        self._observers[observer] = player_id

    def remove(self, observer: GameObserver):
        if self._observers.get(observer) is not None:
            self._observers.pop(observer)

    def notifyAll(self, message: GameState):
        # TODO adjust string format
        string = "Sleeping Queens:\nNumber of players: " + str(message.number_of_players) + \
                 "\nSleeping Queens: " + repr(message.sleeping_queens) + "\nOn turn now is Player with id: " + \
                 str(message.on_turn)
        for observer, player_id in self._observers.items():
            observer.notify(string)



class GamePlayerInterface:
    """Player on turn inputs his move"""
    def play(self, player: str, cards: str) -> str:
        pass

class OtherComponent(GameObserver):
    pass

class GameAdaptor:
    def __init__(self, players: List):
        self.player_map = dict()
        self.players = []
        self.game_observable = GameObservable()
        for i, player in enumerate(players):
            self.player_map[player] = i+1
            self.game_observable.addPlayer(i+1, OtherComponent())

        self.game = Game(len(self.player_map))

    def play(self, player: str, cards: str) -> str:
        if self.player_map.get(player) is None:
            return ""
        # TODO

