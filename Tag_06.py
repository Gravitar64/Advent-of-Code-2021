from time import perf_counter as pfc
from collections import deque


def read_puzzle(file):
  with open(file) as f:
    return map(int, f.readline().split(','))


def solve(puzzle, days):
  counts = deque([0]*9)
  for count in puzzle:
    counts[count] += 1
  for _ in range(days):
    counts.rotate(-1)
    counts[6] += counts[8]
  return sum(counts)

start = pfc()
print(solve(read_puzzle('Tag_06.txt'), 80))
print(solve(read_puzzle('Tag_06.txt'), 256))
print(f'Solved in {pfc()-start:.6f} sec.')