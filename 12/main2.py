STEP = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

# clockwise
ROTATE = {
    0: lambda x, y: (x, y),
    90: lambda x, y: (y, -x),
    180: lambda x, y: (-x, -y),
    270: lambda x, y: (-y, x)
}


if __name__ == '__main__':
    x, y = 0, 0
    wx, wy = 10, 1

    fin = open("input.txt")
    for line in fin:
        cmd = line[0]
        num = int(line[1:])

        if cmd == 'L': # counterclock
            wx, wy = ROTATE[360 - num](wx, wy)
        elif cmd == 'R': # clock
            wx, wy = ROTATE[num](wx, wy)
        elif cmd == 'F':
            x, y = x + wx * num, y + wy * num
        else:
            wx, wy = wx + STEP[cmd][0] * num, wy + STEP[cmd][1] * num
        print(x, y, wx, wy)
    fin.close()

    print(abs(x) + abs(y))