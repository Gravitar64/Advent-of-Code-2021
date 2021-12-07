from time import perf_counter as pfc

def read_puzzle(file):
  with open(file) as f:
    return list(map(f.read().count, '012345678'))


def solve(puzzle, days):
  for _ in range(days):
    puzzle = puzzle[1:] + puzzle[:1]
    puzzle[6] += puzzle[8]
  return sum(puzzle)


start=pfc()
print(solve(read_puzzle('Tag_06.txt'), 80))
print(pfc()-start)
start=pfc()
print(solve(read_puzzle('Tag_06.txt'), 256))
print(pfc()-start)
