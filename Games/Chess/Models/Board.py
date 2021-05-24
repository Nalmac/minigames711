from Games.Chess.Models import Square

class Board():
    def __init__(self) -> None:
        self.files = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.rows = [i for i in range(1, 9)]