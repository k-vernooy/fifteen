import board
import sys
import signal
import curses


def signal_handler(sig, frame):
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    sys.exit(0)

def mainloop():
    signal.signal(signal.SIGINT, signal_handler)
    b = board.Board(4, 4)

    while not b.complete():
        b.draw()

    b.stdscr.addstr(12,0,"\ngame over! press any key to exit, or r to restart")
    ch = b.draw()
    
    if ch == 114:
        mainloop()

    b.cleanup()
    sys.exit(0)
    signal.pause()

mainloop()