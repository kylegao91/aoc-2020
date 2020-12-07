COLOR_SET = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def year(st, mini, maxi):
    try:
        return len(st) == 4 and mini <= int(st) <= maxi
    except:
        return False

def height(st):
    try:
        num = st[:-2]
        unit = st[-2:]
        if unit == 'cm':
            return 150 <= int(num) <= 193
        elif unit == 'in':
            return 59 <= int(num) <= 76
        else:
            raise ValueError()
    except:
        return False

def rgb(st):
    if len(st) == 7 and st[0] == '#':
        for i in range(1, 4):
            val = st[(2*i-1):(2*i+1)]
            try:
                int('0x' + val, 16)
            except:
                return False
        return True
    else:
        return False

def color(st):
    return st in COLOR_SET

def pid(st):
    return len(st) == 9 and all(['0' <= c <= '9' for c in st])

REQUIRED= {
    "byr": lambda val: year(val, 1920, 2002),
    "iyr": lambda val: year(val, 2010, 2020),
    "eyr": lambda val: year(val, 2020, 2030),
    "hgt": lambda val: height(val),
    "hcl": lambda val: rgb(val),
    "ecl": lambda val: color(val),
    "pid": lambda val: pid(val)
}

def validate(fields):
    print(fields)
    values = {}
    for f in fields:
        key, val = f.split(":")
        values[key] = val
    for k in REQUIRED:
        if k not in values or not REQUIRED[k](values[k]):
            print(f"Failed on: {k}:{val}")
            return False
    return True

if __name__ == '__main__':
    fin = open("input.txt")

    current = []
    count = 0
    for line in fin:
        line = line.strip()
        if not line:
            if validate(current):
                count += 1
            current = []
        else:
            current += line.split(" ")
    if validate(current):
        count += 1

    fin.close()
    print(count)
