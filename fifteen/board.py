from random import shuffle, randint


class Board:
    """Represents a grid of blocks with an empty spot"""
    
    def __init__(self, x, y):
        # size the board
        self.height = y
        self.width = x
        self.board = list(range(1, x * y + 1))

        # set the empty to last index of board
        self.empty = x * y - 1

    def move(self, dir):
        """Switch the position of a block with `empty`"""
        # index of value to move
        check = None
        
        if dir == 1:
            # move up
            if (self.empty + self.width <= len(self.board)):
                check = self.empty + self.width
        elif dir == 2:
            # move right
            if self.empty % self.width != 0:
                check = self.empty - 1
                print (check)
        elif dir == 3:
            # move down
            if self.empty - self.width >= 0:
                check = self.empty - self.width
        else:
            # move left
            if self.empty % self.width != self.width - 1:
                check = self.empty + 1

        if check != None:
            self.board[self.empty] = self.board[check]
            self.empty = check

    def shuffle(self):
        """Randomly suffles the board"""
        shuffle(board)
        randint(0, self.height * self.width)

    def complete(self):
        """Gets whether or not the current game is complete"""

        for i in range(0, self.width * self.height - 1):
            if self.board[i] != i:
                return False
        
        return True

    def to_string(self):
        strings = []

        for i in range(self.height):
            string = ""
            for j in range(self.width):
                if self.empty != i * self.width + j:
                    string += str(self.board[i * self.width + j])
                else:
                    string += " "
                string += ", "
            strings.append(string)

        return strings