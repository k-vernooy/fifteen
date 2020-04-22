from board import Board
import curses


class Canvas:
    def __init__(self, board):
        # save the board
        self.board = board
        
        # initialize curses
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)


    def draw(self):
        """Draw the canvas to the terminal"""
        self.stdscr.addstr(0, 0, "test")
        index = 0

        for string in self.board.to_string():
            self.stdscr.addstr(index, 0, string)
            index += 1

        self.stdscr.getch()

    def cleanup(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
