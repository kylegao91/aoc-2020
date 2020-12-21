import itertools
from collections import deque

NAME = ['top', 'right', 'bottom', 'left']
SIDE = [(0, 1), (1, 0), (0, -1), (-1, 0)]

MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]
PATTERN = []
for i, row in enumerate(MONSTER):
    for j, ch in enumerate(row):
        if ch == '#':
            PATTERN.append((i, j))


class Tile:

    def __init__(self, tid, tile):
        self.tid = tid
        if tile is None:
            self.tile = []
            for _ in range(10):
                self.tile.append(['X'] * 10)
        else:
            self.tile = tile
        self.sides = self.get_sides()

        self._length = len(self.tile[0])
        self._matches = [list() for _ in range(4)]
        self._num_matches = 0

    def __str__(self):
        st = f"{self.tid}\n"
        for row in self.tile:
            st = st + "".join(row) + "\n"
        return st

    @property
    def num_matches(self):
        return self._num_matches

    def adj_tiles(self):
        for side_idx, side_matches in enumerate(self._matches):
            if len(side_matches) > 1:
                print(f"Tile has more than 1 matches: {self.tid}")
            for side_idx_o, tile, flip in side_matches:
                yield side_idx, side_idx_o, tile, flip

    def get_sides(self):
        top = list(reversed(self.tile[0]))
        bottom = self.tile[-1]
        left = []
        right = []
        for row in self.tile:
            left.append(row[0])
            right.append(row[-1])
        right.reverse()
        return [top, right, bottom, left]

    def take_side(self, side_idx):
        self._matches[side_idx] = []

    def add_match(self, side_idx, side_idx_o, t, flip):
        self._matches[side_idx].append((side_idx_o, t, flip))
        self._num_matches += 1
    
    def matches(self, t):
        for side_idx, side in enumerate(self.sides):
            for side_idx_o, side_o in enumerate(t.sides):
                if side == list(reversed(side_o)):
                    self.add_match(side_idx, side_idx_o, t, False)
                elif side == side_o:
                    self.add_match(side_idx, side_idx_o, t, True)

    def horizontal_flip(self):
        # print(f"Horizontally flip {self.tid}")
        self.sides[3], self.sides[1] = self.sides[1], self.sides[3]
        self._matches[3], self._matches[1] = self._matches[1], self._matches[3]
        for row in self.tile:
            row.reverse()
        for side_idx in range(4):
            modified_matches = []
            for side_idx_o, t, flip in self._matches[side_idx]:
                modified_matches.append((side_idx_o, t, not flip))
            self._matches[side_idx] = modified_matches

            for side_idx_o, t, flip in self._matches[side_idx]:
                modified_matches = []
                for m in t._matches[side_idx_o]:
                    if m[1].tid == self.tid:
                        if m[0] in [1, 3]:
                            modified_matches.append(((m[0] - 2) % 4, self, not flip))
                        else:
                            modified_matches.append((m[0], self, not flip))
                    else:
                        modified_matches.append(m)
                

    def vertical_flip(self):
        # print(f"Vertically flip {self.tid}")
        self.sides[0], self.sides[2] = self.sides[2], self.sides[0]
        self._matches[0], self._matches[2] = self._matches[2], self._matches[0]
        self.tile.reverse()
        for side_idx in range(4):
            modified_matches = []
            for side_idx_o, t, flip in self._matches[side_idx]:
                modified_matches.append((side_idx_o, t, not flip))
            self._matches[side_idx] = modified_matches

            for side_idx_o, t, flip in self._matches[side_idx]:
                modified_matches = []
                for m in t._matches[side_idx_o]:
                    if m[1].tid == self.tid:
                        if m[0] in [0, 2]:
                            modified_matches.append(((m[0] - 2) % 4, self, not flip))
                        else:
                            modified_matches.append((m[0], self, not flip))
                    else:
                        modified_matches.append(m)

    def rotate(self, step):
        # print(f"Rotate {self.tid} by {step}")
        self.sides = self.sides[4-step:] + self.sides[:4-step]
        self._matches = self._matches[4-step:] + self._matches[:4-step]

        rotated = []
        for _ in range(self._length):
            rotated.append([None] * self._length)
        
        for x in range(self._length):
            for y in range(self._length):
                i, j = self._transform(x, y, step)
                rotated[i][j] = self.tile[x][y]
        self.tile = rotated

        for side_idx in range(4):
            for side_idx_o, t, flip in self._matches[side_idx]:
                modified_matches = []
                for m in t._matches[side_idx_o]:
                    if m[1].tid == self.tid:
                        modified_matches.append(((m[0] + step) % 4, self, flip))
                    else:
                        modified_matches.append(m)

    def count_pattern(self, pattern):
        all_matched = set()
        non_pattern_count = 0
        for i in range(self._length):
            for j in range(self._length):
                matched = set()
                for px, py in pattern:
                    x, y = i + px, j + py
                    if 0 <= x < self._length and 0 <= y < self._length and self.tile[x][y] == '#' and (x, y) not in all_matched:
                        matched.add((x, y))
                if len(matched) == len(pattern):
                    all_matched.update(matched)
                if (i, j) not in all_matched and self.tile[i][j] == '#':
                    non_pattern_count += 1
        return len(all_matched), non_pattern_count

    def _transform(self, x, y, step):
        if step == 0:
            return x, y
        elif step == 1:
            return y, self._length - x - 1
        elif step == 2:
            return self._length - x - 1, self._length - y - 1
        elif step == 3:
            return self._length - y - 1, x

class Image:

    def __init__(self):
        self.tiles = dict()
        self._tids = set()
        self._min_x = 1000000
        self._max_x = 0 
        self._min_y = 1000000
        self._max_y = 0

    def __str__(self):
        img = self.to_tiles() 
        st = "\n".join([" ".join([str(t.tid) for t in row]) for row in img])
        st += "\n"
        img = self.to_pixels()
        st += "\n".join(["".join(row) for row in img])
        return st

    def to_tiles(self):
        img = []
        for y in range(self._max_y, self._min_y - 1, -1):
            row = []
            for x in range(self._min_x, self._max_x + 1):
                if (x, y) in self.tiles:
                    row.append(self.tiles[(x, y)])
                else:
                    row.append(Tile('XXXX', None))
            img.append(row)
        return img

    def to_pixels(self):
        tiles = self.to_tiles()
        th = len(tiles[0][0].tile) - 2
        tw = len(tiles[0][0].tile[0]) - 2
        h = len(tiles) * th
        w = len(tiles[0]) * tw
        img = []
        for _ in range(h):
            img.append([" "] * w)
        for ti, t_row in enumerate(tiles):
            for tj, t in enumerate(t_row):
                for pi, p_row in enumerate(t.tile[1:-1]):
                    for pj, p in enumerate(p_row[1:-1]):
                        x = ti * th + pi
                        y = tj * tw + pj
                        img[x][y] = p
        return img 

    def add(self, x: int, y: int, tile: Tile):
        assert (x, y) not in self.tiles
        self.tiles[(x, y)] = tile
        self._tids.add(tile.tid)
        self._min_x = min(self._min_x, x)
        self._max_x = max(self._max_x, x)
        self._min_y = min(self._min_y, y)
        self._max_y = max(self._max_y, y)

    def contains(self, tile: Tile) -> bool:
        return tile.tid in self._tids

    def corners(self):
        return [
            self.tiles[(self._min_x, self._min_y)],
            self.tiles[(self._min_x, self._max_y)],
            self.tiles[(self._max_x, self._min_y)],
            self.tiles[(self._max_x, self._max_y)]
        ]


if __name__ == '__main__':
    tiles = []
    fin = open("input.txt")
    current_tid = None
    current_tile = []
    for line in fin:
        line = line.strip()
        if not line:
            tiles.append(Tile(current_tid, current_tile))
            current_tile = []
            continue
        if line.startswith("Tile"):
            current_tid = int(line[5:-1])
        else:
            current_tile.append([ch for ch in line])
    if current_tile:
        tiles.append(Tile(current_tid, current_tile))
    fin.close()

    for ti, tj in itertools.product(tiles, tiles):
        if ti.tid != tj.tid:
            ti.matches(tj)

    corner_tile = next(t for t in tiles if t.num_matches == 2)
    # print(f"Start with {corner_tile.tid}")

    img = Image()
    img.add(0, 0, corner_tile)

    queue = deque([(0, 0, corner_tile)])

    while queue:
        # print(queue)
        x, y, tile = queue.popleft()
        for side_idx_i, side_idx_j, adj_tile, flip in tile.adj_tiles():
            # print(f"Tile {tile.tid}'s {NAME[side_idx_i]} side matches tile {adj_tile.tid}'s {'flipped ' if flip else ''}{NAME[side_idx_j]} side")
            if not img.contains(adj_tile):
                # target is (side_idx_i - 2) % 4
                # start  is side_idx_j 
                # rotate clockwise by ((target - start) % 4) * 90
                rotate_step = (((side_idx_i - 2) % 4) - side_idx_j) % 4
                adj_tile.rotate(rotate_step)
                if flip:
                    if side_idx_i % 2 == 0:
                        adj_tile.horizontal_flip()
                    else:
                        adj_tile.vertical_flip()

                new_x = x + SIDE[side_idx_i][0]
                new_y = y + SIDE[side_idx_i][1]
                img.add(new_x, new_y, adj_tile)
                queue.append((new_x, new_y, adj_tile))
    img_tile = Tile(None, img.to_pixels())
    print(img_tile)

    # Part 1
    res = 1
    for t in img.corners():
        res *= t.tid
    print(res)

    # Part 2
    for flip in [False, True]:
        for rotate_step in range(4):
            t = Tile(None, img_tile.tile)
            if flip:
                t.horizontal_flip()
            t.rotate(rotate_step)
            pattern_count, non_pattern_count = t.count_pattern(PATTERN)
            if pattern_count:
                print(non_pattern_count)
                exit()
        