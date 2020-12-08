import re
from collections import defaultdict, deque

COLOR = r"[a-z]+ [a-z]+"
NUMBER = r"[1-9][0-9]*"
BAG = fr"({NUMBER}) ({COLOR}) bags?"

PATTERN = re.compile(BAG)

if __name__ == '__main__':
    fin = open("input.txt")
    links = defaultdict(dict)
    rlinks = defaultdict(dict)
    for line in fin:
        line = line.strip()[:-1] # minus .
        color, bags = line.split(" bags contain ")
        if bags != "no other bags":
            matches = PATTERN.finditer(bags)
            for m in matches:
                number = int(m.group(1))
                contained = m.group(2)
                links[color][contained] = number
                rlinks[contained][color] = number
    fin.close()

    count = 0
    q = deque(["shiny gold"])
    visited = set(q)
    while q:
        head = q.popleft()
        for color in rlinks[head]:
            if color not in visited:
                q.append(color)
                visited.add(color)
                count += 1
    print(count)

    def contain_bags(root):
        contains = links[root]
        if not contains:
            return 0
        else:
            total = 0 
            for color in contains:
                total += contains[color] + contains[color] * contain_bags(color)
            return total
    print(contain_bags("shiny gold"))
