from itertools import islice
from collections import deque

def get_score(s):
    return sum([(idx + 1) * card for idx, card in enumerate(reversed(s))])

def play(s1, s2, recursive=False, score=False):
    seen_hands = set()
    while s1 and s2:
        seen_hands.add(tuple(list(s1) + ["|"] + list(s2)))
        top1, top2 = s1.popleft(), s2.popleft()
        if recursive and len(s1) >= top1 and len(s2) >= top2:
            winner, _ = play(deque(islice(s1, 0, top1)), deque(islice(s2, 0, top2)), recursive=True)
        else:
            winner = 0 if top1 > top2 else 1

        tops = [top1, top2]
        [s1, s2][winner] += [tops[winner], tops[1 - winner]]
        if tuple(list(s1) + ["|"] + list(s2)) in seen_hands:
            return 0, None

    winner = 0 if s1 else 1
    if score:
        res = get_score(s1) if s1 else get_score(s2)
    else:
        res = None
    return winner, res

if __name__ == '__main__':
    s1 = deque()
    s2 = deque()
    fin = open("input.txt")
    current_s = None
    for line in fin:
        line = line.strip()
        if line == 'Player 1:':
            current_s = s1
        elif line == 'Player 2:':
            current_s = s2
        elif line:
            current_s.append(int(line))
    fin.close()

    # Part 1
    _, res = play(s1.copy(), s2.copy(), score=True)
    print(res)

    # Part 2
    _, res = play(s1.copy(), s2.copy(), recursive=True, score=True)
    print(res)