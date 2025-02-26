import random
import curses
from curses import textpad

def create_food(snake, box):
    '''Function to create Food'''

    food = None
    while food is None:
        food = [random.randint(box[0][0]+1, box[1][0]-1),
        random.randint(box[0][1]+1, box[1][1]-1)]

        if food in snake:
            food = None

    return food


def print_score(stdscr, score):
    '''Function to print score'''

    screen_height, screen_width = stdscr.getmaxyx()
    score_text = "score.{}".format(score)
    stdscr.addstr(0, screen_width//2 - len(score_text)//2, score_text)
    stdscr.refresh()


def main(stdscr):

    curses.curs_set(0)  # deactivate curser blinking
    stdscr.nodelay(1)  # getch() is non blocking
    stdscr.timeout(150) # how much time to wait for user response in ms

    # fetching screen height and width
    screen_height, screen_width = stdscr.getmaxyx()

    box = [[3,3], [screen_height-3, screen_width-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    """Initialising snake"""
    snake = [[screen_height//2, screen_width//2+1], [screen_height//2, screen_width//2], [screen_height//2, screen_width//2-1]]
    direction = curses.KEY_RIGHT

    for y, x in snake:
        stdscr.addstr(y, x, '#')

    food = create_food(snake, box)
    stdscr.addstr(food[0], food[1], '*')

    score = 0
    print_score(stdscr, score)

    """defining movements"""
    while 1:
        key = stdscr.getch()
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key

        head = snake[0]
        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1] #y, x axis
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
        if direction == curses.KEY_UP:
            new_head = [head[0]-1, head[1]]
        if direction == curses.KEY_DOWN:
            new_head = [head[0]+1, head[1]]

        snake.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], '#')


        if snake[0] == food:
            food = create_food(snake, box)
            stdscr.addstr(food[0], food[1], '*')

            score += 1
            print_score(stdscr, score)
        else:
            stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1] in [box[0][1], box[1][1]] or
            snake[0] in snake[1:]
        ):
            msg = "GameOver!"
            stdscr.addstr(screen_height//2, screen_width//2-len(msg)//2, msg)
            stdscr.nodelay(0)
            stdscr.getch()
            break

        stdscr.refresh()

    stdscr.getch()
curses.wrapper(main)