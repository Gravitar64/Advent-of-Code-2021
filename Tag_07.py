from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return sorted([int(x) for x in f.readline().split(',')])


def solve(puzzle,part1):
  length = len(puzzle)
  mid = puzzle[length//2]
  if part1: return sum(abs(x-mid) for x in puzzle)
  
  mean = sum(puzzle) // length
  gauss = lambda x: x * (x+1) // 2
  return sum(gauss(abs(x-mean)) for x in puzzle)  


start = pfc()
print(solve(read_puzzle('Tag_07.txt'), True))
print(solve(read_puzzle('Tag_07.txt'), False))
print(pfc()-start)
