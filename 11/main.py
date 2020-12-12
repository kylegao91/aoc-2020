from copy import deepcopy

STEP_X = [0, 0, 1, 1, 1, -1, -1, -1]
STEP_Y = [-1, 1, 0, -1, 1, 0, -1, 1]
STEPS = list(zip(STEP_X, STEP_Y))

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'

NUM_ROWS = 0
NUM_COLS = 0


def count_occupied(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == OCCUPIED:
                count += 1
    return count

def print_seats(seats):
    for row in seats:
        print("".join(row))
    print()
    input()

def _advance(current_state, threshold, see_far=False):
    next_state = [[None] * NUM_COLS for _ in range(NUM_ROWS)]
    move = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if current_state[i][j] == FLOOR:
                next_state[i][j] = FLOOR
                continue

            num_neighbors = 0
            visible = 0
            for dx, dy in STEPS:
                x, y = i + dx, j + dy
                if (0 <= x < NUM_ROWS) and (0 <= y < NUM_COLS) and current_state[x][y] == OCCUPIED:
                    num_neighbors += 1
                while see_far and (0 <= x < NUM_ROWS) and (0 <= y < NUM_COLS):
                    if current_state[x][y] == OCCUPIED:
                        visible += 1
                        break
                    elif current_state[x][y] == EMPTY:
                        break
                    x, y = x + dx, y + dy
            if current_state[i][j] == EMPTY and visible == 0:
                next_state[i][j] = OCCUPIED
                move += 1
            elif current_state[i][j] == OCCUPIED and visible >= threshold: 
                next_state[i][j] = EMPTY
                move += 1
            else:
                next_state[i][j] = current_state[i][j]
    return next_state, move

def solve(init_state, threshold, see_far=False):
    current_state = deepcopy(init_state)

    while True:
        next_state, move = _advance(current_state, threshold, see_far)
        if move == 0:
            break
        current_state = next_state
    return current_state

if __name__ == '__main__':
    fin = open("input.txt")
    init_state = []
    for line in fin:
        init_state.append([ch for ch in line.strip()])
    fin.close()

    NUM_ROWS = len(init_state)
    NUM_COLS = len(init_state[0])

    print(count_occupied(solve(init_state, 4)))
    print(count_occupied(solve(init_state, 5, True)))