SUM = 2020

def two_sum(data, goal):
    for x in data:
        if (goal- x) in data:
            return x, goal - x

if __name__ == '__main__':
    data = [int(line) for line in open("input.txt")]

    # part 1
    x, y = two_sum(set(data), SUM)
    print(x * y)

    # part 2
    for i, x in enumerate(data):
        if SUM - x > 0:
            rest = set(data[:i] + data[i + 1:])
            res = two_sum(rest, SUM - x)
            if res is not None:
                y, z = res
                print(x * y * z)
                break
