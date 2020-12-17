from operator import add
import itertools

STEPS = [-1, 0, 1]
DIM = 4

if __name__ == '__main__':
    space = set()
    fin = open("input.txt")
    for y, line in enumerate(fin):
        for x, state in enumerate(line.strip()):
            if state == '#':
                space.add((x, y, *([0] * (DIM - 2))))
    fin.readline()

    for _ in range(6):
        neighbor_count = {}
        for pos in space:
            for diff in itertools.product(*([STEPS] * DIM)):
                if not all([d == 0 for d in diff]):
                    new_pos = tuple(map(add, pos, diff))
                    if not new_pos in neighbor_count:
                        neighbor_count[new_pos] = 0
                    neighbor_count[new_pos] += 1

        next_space = set()
        for pos in space | set(neighbor_count.keys()):
            num_active_neighbors = neighbor_count.get(pos, 0)
            if pos in space:
                if num_active_neighbors in [2, 3]:
                    next_space.add(pos)
            else:
                if num_active_neighbors == 3:
                    next_space.add(pos)
        space = next_space
    print(len(space))