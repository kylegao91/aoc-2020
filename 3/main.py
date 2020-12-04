
if __name__ == '__main__':
    fin = open("input.txt")
    f = []
    for line in fin:
        f.append(line.strip())

    n = len(f)
    m = len(f[0])

    def solve(x, y):
        i = 0
        j = 0
        count = 0
        while i < n:
            if f[i][j] == '#':
                count += 1
            j = (j + x) % m
            i += y
        return count

    res = 1
    for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        count = solve(x, y)
        print(count)
        res *= count
    print(res)

