import board
import canvas
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
canvas = canvas.Canvas(board)

while not canvas.board.complete():
    canvas.draw()

canvas.cleanup()
signal.pause()