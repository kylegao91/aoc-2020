MAX_BIT = 36

def apply_mask(val, mask):
    i = 0
    remain = val
    bitarr = []
    for i in range(MAX_BIT):
        mask_bit = mask[-(i + 1)]
        if mask_bit == 'X':
            bit = 'X'
        else:
            bit = int(mask_bit) or (remain % 2)
        bitarr.append(str(bit))
        remain = remain // 2
    return bitarr

def permute(addr):
    if not addr:
        yield ""
    else:
        if addr[0] == 'X':
            for rest in permute(addr[1:]):
                yield '0' + rest
                yield '1' + rest
        else:
            for rest in permute(addr[1:]):
                yield addr[0] + rest

if __name__ == '__main__':
    fin = open("input.txt")

    masks = []
    cmd_list = []
    for line in fin:
        cmd, val = line.strip().split(" = ")
        if cmd == 'mask':
            masks.append(val)
        cmd_list.append((cmd, val))

    fin.close()

    mask_idx = - 1
    seen = set()
    result = 0
    for cmd, val in reversed(cmd_list):
        if cmd == 'mask':
            mask_idx -= 1
        else:
            val = int(val)
            mask = masks[mask_idx]
            addr = int(cmd[4:-1])
            addr = apply_mask(addr, mask)

            for x in permute(addr):
                if x not in seen:
                    seen.add(x)
                    result += val
    print(result)