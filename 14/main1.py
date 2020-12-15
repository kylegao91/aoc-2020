MAX_BIT = 36

def apply_mask(val, mask):
    i = 0
    res = 0
    power = 1
    remain = val
    for i in range(MAX_BIT):
        mask_bit = mask[-(i + 1)]
        if mask_bit == 'X':
            bit = remain % 2
        else:
            bit = int(mask_bit)
        res += bit * power
        remain = remain // 2
        power = power * 2
    return res

if __name__ == '__main__':
    fin = open("input.txt")

    mask = None
    mem = {}
    for line in fin:
        cmd, val = line.strip().split(" = ")
        if cmd == 'mask':
            mask = val
        else:
            idx = int(cmd[4:-1])
            mem[idx] = apply_mask(int(val), mask)

    fin.close()

    print(sum(mem.values()))