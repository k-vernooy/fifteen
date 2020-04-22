class Board:
    def __init__(self, x, y):
        self.board = range(x * y - 1)


    def move():


    def shuffle():
        """Randomly suffles the board"""


    def complete():
        """Gets whether or not the current game is complete"""

        for i in range(0, x * y - 1):
            if board[i] != i:
                return false
        
        return true