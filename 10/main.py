
if __name__ == '__main__':
    fin = open("input.txt")
    has_adapter = [True]
    length = 1
    for line in fin:
        num = int(line)
        if num >= length:
            has_adapter += [False] * (num - length + 1)
            length += num - length + 1
        has_adapter[num] = True
    has_adapter += [False, False, True]
    fin.close()

    # part 1
    count = [None, 0, 0, 0]
    prev = 0
    for i in range(1, len(has_adapter)):
        if has_adapter[i]:
            diff = i - prev
            count[diff] += 1
            prev = i
    print(count[1] * count[3])

    # part 2
    # f[N] = number of arrangements for jolt N
    f = [0] * len(has_adapter)
    f[0] = 1
    for i in range(1, len(has_adapter)):
        if has_adapter[i]:
            for j in range(i - 3, i):
                if j >= 0:
                    f[i] += f[j]
        else:
            f[i] = 0
    print(f[-1])