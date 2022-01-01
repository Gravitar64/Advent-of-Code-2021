# Geniale Lösung von GrAndAG77 mit numpy
# https://www.reddit.com/r/adventofcode/comments/ro2uav/2021_day_25_solutions/hpwntr6/?context=3

from time import perf_counter as pfc
import numpy as np


def read_puzzle(filename):
    with open(filename) as f:
        return np.array(list(map(list, f.read().strip().split())))


def solve(puzzle):
    moved = [True]
    while any(moved[-2:]):
        for c, axis in ((">", 1), ("v", 0)):
            allowed_moves = (np.roll(puzzle, -1, axis) == ".") & (puzzle == c)
            moved.append(np.any(allowed_moves))
            puzzle[allowed_moves] = "."
            puzzle[np.roll(allowed_moves, 1, axis)] = c
    return len(moved) // 2


start = pfc()
print(solve(read_puzzle("Tag_25.txt")))
print(pfc() - start)