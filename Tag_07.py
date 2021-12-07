def read_puzzle(file):
  with open(file) as f:
    return sorted([int(x) for x in f.readline().split(',')])


def solve(puzzle):
  #part1
  length = len(puzzle)
  mid = puzzle[length//2]
  part1 = sum(abs(x-mid) for x in puzzle)
  
  #part2
  mean = sum(puzzle) // length
  gauss = lambda x: x * (x+1) // 2
  return part1, sum(gauss(abs(x-mean)) for x in puzzle)  


print(solve(read_puzzle('Tag_07.txt')))