import board
import sys
import signal
import curses


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
board = board.Board(int(sys.argv[1]), int(sys.argv[2]))

while not board.complete():
    board.draw()

board.cleanup()
signal.pause()