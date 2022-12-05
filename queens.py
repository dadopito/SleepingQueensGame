from data_types import *
from data_types import SleepingQueenPosition


class QueenCollection:
    def __init__(self):
        self.queens_array = []
        for i in range(12):
            self.queens_array.append(None)
    def addQueen(self, queen: Queen):
        for index in range(12):
            if self.queens_array[index] is None:
                self.queens_array[index] = queen

    def removeQueen(self, position: SleepingQueenPosition) -> Optional[Queen]:
        queen = self.queens_array[position.getCardIndex()]
        if queen is not None:
            self.queens_array[position.getCardIndex()] = None
            return queen
        return None

    def getQueens(self) -> List:
        return self.queens_array


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
