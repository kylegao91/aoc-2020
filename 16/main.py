if __name__ == '__main__':
    fields = []
    my_ticket = []
    fin = open("input.txt")
    line = fin.readline().strip()
    while line:
        name, ranges = line.split(": ")
        first, second = ranges.split(" or ")
        fields.append((
            name, 
            *[int(n) for n in first.split("-")],
            *[int(n) for n in second.split("-")],
        ))
        line = fin.readline().strip()
    print(fields)

    fin.readline()
    my_ticket = [int(n) for n in fin.readline().strip().split(",")]

    fin.readline()
    fin.readline()

    tickets = []
    part1_result = 0
    for line in fin:
        nums = []
        valid = True
        for n in line.strip().split(","):
            num = int(n)
            nums.append(num)
            no_match = True
            for f in fields:
                if (f[1] <= num <= f[2]) or (f[3] <= num <= f[4]):
                    no_match = False
                    break
            if no_match:
                part1_result += num
                valid = False
        if valid:
            tickets.append(nums)
    fin.close()
    print(part1_result)

    valid_fields = []
    all_fields = set(range(len(fields)))
    for col in range(len(fields)):
        invalid_fields = set()
        for ticket in tickets:
            for fid, f in enumerate(fields):
                num = ticket[col]
                if not ((f[1] <= num <= f[2]) or (f[3] <= num <= f[4])):
                    invalid_fields.add(fid)
        valid_fields.append((col, all_fields - invalid_fields))
    sorted_valid_fields = sorted(valid_fields, key=lambda s: len(s[1]))
    
    part2_result = 1
    taken = set()
    for col, possible_fields in sorted_valid_fields:
        possible_fids = list(possible_fields - taken)
        assert len(possible_fids) == 1
        fid = possible_fids[0]
        taken.update(possible_fields)
        if fields[fid][0].startswith("departure"):
            part2_result *= my_ticket[col]
    print(part2_result)