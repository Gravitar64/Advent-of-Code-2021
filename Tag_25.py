from time import perf_counter as pfc


def read_puzzle(filename):
    vs, hs = set(), set()
    with open(filename) as f:
        for y, row in enumerate(f.read().split("\n")):
            for x, c in enumerate(row):
                if c == "v":
                    vs.add((x, y))
                elif c == ">":
                    hs.add((x, y))
    return hs, vs


def nextPos(x, y, c, w, h):
    if c == ">":
        return (x + 1) % w, y
    else:
        return x, (y + 1) % h


def findStable(hs, vs, w, h, step = 0):
    while True:
        step += 1
        new_hs = set()
        for pos in hs:
            newPos = nextPos(*pos, ">", w, h)
            if newPos in hs or newPos in vs:
                new_hs.add(pos)
            else:
                new_hs.add(newPos)
        new_vs = set()
        for pos in vs:
            newPos = nextPos(*pos, "v", w, h)
            if newPos in vs or newPos in new_hs:
                new_vs.add(pos)
            else:
                new_vs.add(newPos)
        if vs == new_vs and hs == new_hs: return step
        hs, vs = new_hs, new_vs


def solve(hs, vs):
    all_pos = hs | vs
    w, h = map(max, zip(*all_pos))
    return findStable(hs, vs, w + 1, h + 1)


start = pfc()
print(solve(*read_puzzle("Tag_25.txt")))
print(pfc() - start)
