DIR_TO_DEG = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270
}

STEP = {
    0: (0, 1),
    90: (1, 0),
    180: (0, -1),
    270: (-1, 0)
}

def advance(x, y, degree, cmd, num):
    new_x, new_y, new_deg = x, y, degree
    if cmd == 'L':
        new_deg = (degree - num) % 360
    elif cmd == 'R':
        new_deg = (degree + num) % 360
    elif cmd == 'F':
        new_x, new_y = x + STEP[degree][0] * num, y + STEP[degree][1] * num
    else:
        dir_deg = DIR_TO_DEG[cmd]
        new_x, new_y = x + STEP[dir_deg][0] * num, y + STEP[dir_deg][1] * num
    return new_x, new_y, new_deg
        

if __name__ == '__main__':
    degree = 90 # north is 0
    x, y = 0, 0

    fin = open("input.txt")
    for line in fin:
        cmd = line[0]
        num = int(line[1:])

        x, y, degree = advance(x, y, degree, cmd, num)
    fin.close()

    print(abs(x) + abs(y))