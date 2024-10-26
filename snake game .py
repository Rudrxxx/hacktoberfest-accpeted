import curses
from random import randint

curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.timeout(100)

snake_x = 15
snake_y = 10
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]
food = [randint(1, 18), randint(1, 58)]
win.addch(food[0], food[1], '*')

key = curses.KEY_RIGHT
score = 0

while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    if key == curses.KEY_DOWN:
        new_head = [snake[0][0] + 1, snake[0][1]]
    elif key == curses.KEY_UP:
        new_head = [snake[0][0] - 1, snake[0][1]]
    elif key == curses.KEY_LEFT:
        new_head = [snake[0][0], snake[0][1] - 1]
    elif key == curses.KEY_RIGHT:
        new_head = [snake[0][0], snake[0][1] + 1]

    snake.insert(0, new_head)
    if (
        new_head[0] == 0 or
        new_head[0] == 19 or
        new_head[1] == 0 or
        new_head[1] == 59 or
        new_head in snake[1:]
    ):
        curses.endwin()
        print(f"Game Over! Your score was: {score}")
        break

    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [randint(1, 18), randint(1, 58)]
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], '*')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(snake[0][0], snake[0][1], '#')
