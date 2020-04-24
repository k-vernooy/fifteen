import board
import sys
import signal
import curses
from time import sleep, process_time
from threading import Thread

def signal_handler(sig, frame):
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    sys.exit(0)


def mainloop():
    delay = 0.01
    time = 0
    b = board.Board(4, 4)
    b.draw()

    while not b.complete():
        ch = b.stdscr.getch()
        if ch == curses.KEY_UP:
            b.move(1)
        elif ch == curses.KEY_RIGHT:
            b.move(2)
        elif ch == curses.KEY_DOWN:
            b.move(3)
        elif ch == curses.KEY_LEFT:
            b.move(4)

        if ch != -1:
            b.draw()

        b.stdscr.addstr(14,0,str(round(time * 1000) / 1000))
        sleep(delay)
        time += delay


    b.stdscr.addstr(12,0,"\ngame over! press any key to exit, or r to restart")
    b.stdscr.nodelay(0)

    ch = b.stdscr.getch()
    
    if ch == 114:
        mainloop()

    b.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
mainloop()
signal.pause()
