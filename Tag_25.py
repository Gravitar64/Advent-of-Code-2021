from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as f:
        return {(x,y):c for y,row in enumerate(f.read().split("\n"))
                        for x,c in enumerate(row) if c != '.'}


def nextPos(x,y,c,w,h):
    if c == '>': return (x+1)%w, y
    else:        return x, (y+1)%h


def solve(puzzle):
    w,h = max([x for x,y in puzzle])+1, max([y for x,y in puzzle])+1
    oldState = set(puzzle)
    step = 0
    while True:
        step += 1
        nextGen = {}
        for pos,c in puzzle.items():
            if c != '>': 
                nextGen[pos] = c
                continue
            newPos = nextPos(*pos,c,w,h)
            if newPos in puzzle:
                nextGen[pos] = c
            else:
                nextGen[newPos] = c
        puzzle = nextGen
        nextGen = {}
        for pos,c in puzzle.items():
            if c != 'v': 
                nextGen[pos] = c
                continue
            newPos = nextPos(*pos,c,w,h)
            if newPos in puzzle:
                nextGen[pos] = c
            else:
                nextGen[newPos] = c             
        puzzle = nextGen
        if set(puzzle) == oldState: return step
        oldState = set(puzzle)

start = pfc()
print(solve(read_puzzle("Tag_25.txt")))
print(pfc() - start)