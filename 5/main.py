def to_num(st, zero, one):
    binary = "".join(['1' if ch == one else '0' for ch in st])
    return int(binary, 2)

if __name__ == '__main__':
    fin = open("input.txt")

    max_id = 0
    min_id = 1000
    seen = set()
    for line in fin:
        line = line.strip()
        row = line[:7]
        row_num = to_num(row, 'F', 'B')
        col = line[7:]
        col_num = to_num(col, 'L', 'R')

        seat_id = row_num * 8 + col_num
        seen.add(seat_id)
        max_id = max(max_id, seat_id)
        min_id = min(min_id, seat_id)
    for seat_id in range(min_id, max_id):
        if seat_id not in seen:
            print(seat_id)

    fin.close()
