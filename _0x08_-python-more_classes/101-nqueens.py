#!/usr/bin/python3
import sys


class NQueensSolver:
    """
    Class representing an N Queens problem solver.
    """

    def __init__(self, N):
        """
        Initialize the NQueensSolver instance.

        Args:
            N (int): The number of queens and the size of the chessboard.
        """
        self.N = N
        self.board = [-1] * N
        self.solutions = []

    def solve(self):
        """
        Solve the N Queens problem and print the solutions.
        """
        self.backtrack(0)
        self.print_solutions()

    def is_safe(self, row, col):
        """
        Check if a position is safe for placing a queen.

        Args:
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if the position is safe, False otherwise.
        """
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - col == i - row or \
               self.board[i] - col == row - i:
                return False
        return True

    def backtrack(self, row):
        """
        Perform backtracking to solve the N Queens problem recursively.

        Args:
            row (int): The current row being considered.
        """
        if row == self.N:
            self.solutions.append(self.board[:])
            return
        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row] = col
                self.backtrack(row + 1)

    def print_solutions(self):
        """
        Print the found solutions in the required format.
        """
        for solution in self.solutions:
            chessboard = []
            for i in range(self.N):
                chessboard.append([i, solution[i]])
            print(chessboard)


if __name__ == '__main__':
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(N)
    solver.solve()
