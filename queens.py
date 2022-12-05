from data_types import *


class QueenCollection:
    def __init__(self):
        self.queens_dict = dict()

    def addQueen(self, queen: Queen):
        self.queens_dict[Position] = queen # spojazdnit Positions

    def removeQueen(self, position: SleepingQueenPosition) -> Optional[Queen]:
        found_position = None

        for current_position, queen in self.queens_dict.items():
            if current_position == position: # position je class
                found_position = current_position

        if found_position is not None:
            return self.queens_dict.pop(found_position)

        return None

    def getQueens(self) -> dict[Position, Queen]:
        return self.queens_dict


class SleepingQueens(QueenCollection):
    def __init__(self):
        super().__init__()


class AwokenQueens(QueenCollection):
    def __init__(self):
        super().__init__()


class MoveQueen:
    def __init__(self):
        pass

    def play(self, target_queen: Position) -> bool:
        pass
