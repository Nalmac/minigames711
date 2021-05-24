from Games.Chess.Models.Square import Square

class Board():
    def __init__(self) -> None:
        self.files = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.rows = [i for i in range(1, 9)]
        self.squares = {}

        for i in self.files:
            self.squares[i] = {}
            for j in self.rows:
                self.squares[i][j] = Square(i + str(j))

        self.trait = 0