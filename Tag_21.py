from time import perf_counter as pfc
from functools import lru_cache


def read_puzzle(filename):
  with open(filename) as f:
    return [int(x[-2:]) for x in f.readlines()]


def part_1(p1, p2, sc1=0, sc2=0, i=0):
  if sc2 > 999: return 3*i*sc1
  p1 = (p1 + 9*i+6) % 10 or 10
  return part_1(p2, p1, sc2, sc1+p1, i+1)


@lru_cache(maxsize=None)
def part_2(p1, p2, sc1=0, sc2=0):
  if sc2 > 20: return 0, 1
  wins = 0, 0
  for roll_sum, freq in (3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1):
    new_pos = (p1 + roll_sum) % 10 or 10
    new_score = sc1 + new_pos
    p2w, p1w = part_2(p2, new_pos, sc2, new_score)
    wins = wins[0] + p1w*freq, wins[1] + p2w*freq
  return wins


def solve(puzzle):
  return part_1(*puzzle), max(part_2(*puzzle))


start = pfc()
print(solve(read_puzzle('Tag_21.txt')))
print(pfc()-start)
