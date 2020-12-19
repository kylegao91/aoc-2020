if __name__ == '__main__':
    rules = {}
    fin = open("input.txt")
    line = fin.readline().strip()
    while line:
        idx, rule = line.split(': ')
        if rule[0] == '"':
            rules[idx] = rule[1:-1]
        else:
            rules[idx] = [r.split(" ") for r in rule.split(" | ")]
        line = fin.readline().strip()

    def validate(st, rid):
        r = rules[rid]
        if isinstance(r, list):
            for possible_r in r:
                has_matched = 0
                matched = True
                for sub_rid in possible_r:
                    matched_len = validate(st[has_matched:], sub_rid)
                    if matched_len is not None:
                        has_matched += matched_len
                    else:
                        matched = False
                        break
                if matched:
                    return has_matched
            return None
        else:
            return 1 if st[0] == r else None

    count = 0
    for line in fin:
        line = line.strip()
        matched = validate(line, '0')
        if matched is not None and matched == len(line):
            count += 1
    print(count)

    fin.close()