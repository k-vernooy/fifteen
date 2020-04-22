from random import shuffle, randint
import curses


def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


class Board:
    """Represents a grid of blocks with an empty spot"""
    
    def __init__(self, x, y):
        # size the board
        self.height = y
        self.width = x
        self.board = list(range(1, x * y + 1))

        # set the empty to last index of board
        self.empty = x * y - 1
        
        self.colors = {}
        # initialize curses
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)


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


    def get_string(self, val):
        """Returns list of strings that make a block with a number"""
        strings = []
        strings.append("▗▄▄▄▖");
        # strings.append(str(val))
        
        if self.empty + 1 == val:
            strings.append("▐███▌")
        else:
            middle = ""
            i = 0
            while i < 5:
                if i == 3 - len(str(val)):
                    i += len(str(val))
                    middle += str(val)
                else:
                    if i == 0:
                        middle += "▐"
                    elif i == 4:
                        middle += "▌"
                    else:
                        middle += "█"

                    i += 1
            strings.append(middle)

        strings.append("▝▀▀▀▘");
        return strings


    def draw(self):
        """Draw the board to the terminal"""

        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, -1, curses.COLOR_RED)
        
        for i in range(0, self.height):
            for j in range(0, self.width):
                index = i * self.width + j
                square = self.get_string(self.board[index])

                y = i * 3
                x = j * 5
                m = 0

                for string in square:
                    l = 0
                    for letter in string:
                        if represents_int(letter):
                            self.stdscr.addstr(y + m, x + l, letter, curses.color_pair(2))
                        else:
                            self.stdscr.addstr(y + m, x + l, letter, curses.color_pair(1))
                        l += 1
                    m += 1


        ch = self.stdscr.getch()
        
        if ch == curses.KEY_UP:
            self.move(1)
        elif ch == curses.KEY_RIGHT:
            self.move(2)
        elif ch == curses.KEY_DOWN:
            self.move(3)
        else:
            self.move(4)


    def cleanup(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()