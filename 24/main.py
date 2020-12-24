# Let the distance from the center to middle of edge be 1
# Scale y-axis by sqrt(3)
STEP = {
    'e': (2, 0),
    'ne': (1, 1.5),
    'se': (1, -1.5),
    'w': (-2, 0),
    'nw': (-1, 1.5),
    'sw': (-1, -1.5),
}

def tokenize(st):
    i = 0
    while i < len(st):
        if st[i] in ['s', 'n']:
            yield st[i:i+2]
            i += 2
        else:
            yield st[i]
            i += 1

if __name__ == '__main__':
    fin = open("input.txt")
    black = set()
    for line in fin:
        x, y = 0, 0
        for tok in tokenize(line.strip()):
            dx, dy = STEP[tok]
            x, y = x +dx, y + dy
        pos = (x, y)
        if pos in black:
            black.remove(pos)
        else:
            black.add(pos)
    print(len(black))
    fin.close()

    for _ in range(100):
        black_count = {}
        next_black = set()
        for x, y in black:
            for dx, dy in STEP.values():
                pos = (x + dx, y + dy)
                if pos not in black_count:
                    black_count[pos] = 0
                black_count[pos] += 1
        for pos in black:
            count = black_count.get(pos, 0)
            if not (count == 0 or count > 2):
                next_black.add(pos)
        for pos, count in black_count.items():
            if pos not in black and count == 2:
                next_black.add(pos)
        black = next_black
    print(len(black))