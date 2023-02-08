name = input("Enter your name: ")
input("Press enter to continue.")

import curses
from curses import wrapper
from random_word import RandomWords
import time

r = RandomWords()

global wpm 
def start_screens(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"Welcome to speed typing test!")
    stdscr.addstr(2,0,"Press any key to continue.",curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()

def display(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(2,0,f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if correct_char != char:
            color = curses.color_pair(2)
        
        stdscr.addstr(0 ,i ,char, color)
        
def get_random_words(length: int = 15) -> list[str]:
    # Fetch random words using the random-word package
    return " ".join([r.get_random_word() for _ in range(length)])

def wpm_test(stdscr):
    target_text = get_random_words()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_end = max(time.time() - start_time, 1)
        
        wpm = round((len(current_text) / (time_end/60))/5)

        stdscr.clear()
        display(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        joined_text = "".join(current_text)
        if joined_text == (target_text):
            stdscr.nodelay(False)
            break

        try: 
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

        global pk
        pk = wpm
        
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screens(stdscr)

    while True:
    
        wpm_test(stdscr)
        stdscr.clear()
        
        stdscr.addstr(f"\n*********** Score {pk} Wpm ************* ", curses.color_pair(3))
        stdscr.addstr(2,0,f"Congratuations you completed the test.\n", curses.color_pair(1))
        stdscr.addstr("\n\nPress any key to continue or 'Esc' to escape.\n\n")

        key1 = stdscr.getkey()
        if ord(key1) == 27:
            stdscr.addstr(f"Thank you {name}.", curses.color_pair(3))
            stdscr.getkey()
            break

wrapper(main)