from collections import defaultdict

if __name__ == '__main__':
    fin = open("input.txt")

    total = 0
    current = defaultdict(lambda : 0)
    size = 0
    for line in fin:
        line = line.strip()
        if not line:
            count = 0
            for ch in current:
                if current[ch] == size:
                    count += 1
            total += count
            current = defaultdict(lambda : 0)
            size = 0
        else:
            for ch in line:
                current[ch] += 1
            size += 1
    fin.close()
    count = 0
    for ch in current:
        if current[ch] == size:
            count += 1
    total += count
    print(total)
