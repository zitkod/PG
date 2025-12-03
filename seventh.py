
from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        if self.color == "white":
            step = 1
        else:
            step = -1
        forward = (row + step, col)
        if self.is_position_on_board(forward):
            moves.append(forward)
        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [m for m in moves if self.is_position_on_board(m)]

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for dr, dc in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            r, c = row+dr, col+dc
            while self.is_position_on_board((r,c)):
                moves.append((r,c))
                r += dr
                c += dc
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            r, c = row+dr, col+dc
            while self.is_position_on_board((r,c)):
                moves.append((r,c))
                r += dr
                c += dc
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            r, c = row+dr, col+dc
            while self.is_position_on_board((r,c)):
                moves.append((r,c))
                r += dr
                c += dc
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        steps = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        moves = [(row+dr, col+dc) for dr,dc in steps]
        return [m for m in moves if self.is_position_on_board(m)]

    def __str__(self):
        return f'King({self.color}) at position {self.position}'
