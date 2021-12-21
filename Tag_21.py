from time import perf_counter as pfc
from functools import lru_cache
from collections import Counter
from itertools import product


def read_puzzle(filename):
  with open(filename) as f:
    return [[int(x[-2:]), 0] for x in f.readlines()]


def rolling_dice(puzzle):
  dice, rolled = 0, 0
  while True:
    for player, (pos, score) in enumerate(puzzle):
      rolls = 0
      for _ in range(3):
        dice = dice % 100 + 1
        rolls += dice
      rolled += 3
      pos = (pos + rolls - 1) % 10 + 1
      score += pos
      puzzle[player][0] = pos
      puzzle[player][1] = score
      if score > 999:
        return player, rolled


def part_2(p1, p2):
  dice_freq = Counter(sum(p) for p in product(range(1, 4), repeat=3))

  @lru_cache(maxsize=None)
  def count_universes(p1, p2, sc1=0, sc2=0):
    if sc1 >= 21: return (1, 0)
    if sc2 >= 21: return (0, 1)
    wins = (0, 0)
    for roll_sum, freq in dice_freq.items():
      new_pos = (p1 + roll_sum - 1) % 10 + 1
      new_score = sc1 + new_pos
      p2w, p1w = count_universes(p2, new_pos, sc2, new_score)
      wins = (wins[0] + p1w*freq, wins[1] + p2w*freq)
    return wins

  return max(count_universes(p1, p2))


def solve(puzzle):
  win_player, rolled = rolling_dice(puzzle)
  part1 = puzzle[not win_player][1] * rolled

  puzzle = read_puzzle('Tag_21.txt')
  part2 = part_2(puzzle[0][0], puzzle[1][0])

  return part1, part2


start = pfc()
print(solve(read_puzzle('Tag_21.txt')))
print(pfc()-start)
