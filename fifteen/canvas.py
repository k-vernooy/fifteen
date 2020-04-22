import . import board

class Canvas:
    def __init__(self, board):
        self.board = board

    def draw(self):
        """Draw the canvas to the terminal"""
        
        for value in board:
            print(value)