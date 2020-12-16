N = 30000000

if __name__ == '__main__':
    fin = open("input.txt")
    start_nums = [int(n) for n in fin.readline().strip().split(",")]
    fin.close()

    len_start = len(start_nums)

    last_seen = dict()
    for idx, num in enumerate(start_nums[:-1]):
        last_seen[num] = idx

    current = start_nums[-1]
    for i in range(N - len_start):
        if i % 1000000 == 0:
            print(i)
        idx = i + len_start - 1
        if current in last_seen:
            next = idx - last_seen[current]
        else:
            next = 0
        last_seen[current] = idx
        current = next
    print(current)