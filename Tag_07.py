from time import perf_counter as pfc

def read_puzzle(file):
  with open(file) as f:
    return [int(x) for x in f.readline().split(',')]

def gauss(x):
  return x * (x+1) // 2


def solve(puzzle,part1):
  low, high = min(puzzle), max(puzzle)
  cheapest_possible_outcome = 99999999999999
  for position in range(low,high+1):
    if part1:
      outcome = sum(abs(position-x) for x in puzzle)
    else:
      outcome = sum(gauss(abs(position-x)) for x in puzzle)
    cheapest_possible_outcome = min(cheapest_possible_outcome, outcome)
  return cheapest_possible_outcome  


start = pfc()
print(solve(read_puzzle('Tag_07.txt'), True))
print(solve(read_puzzle('Tag_07.txt'), False))
print(pfc()-start)
