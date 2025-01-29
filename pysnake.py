import time
import curses

def game_loop(window):
    for i in range(10):
        window.addstr(f'O valor de i é: {i}')
        window.refresh()
        time.sleep(1)

if __name__ == '__main__':
    curses.wrapper(game_loop)
