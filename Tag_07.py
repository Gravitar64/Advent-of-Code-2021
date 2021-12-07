def read_puzzle(file):
  with open(file) as f:
    return sorted([int(x) for x in f.readline().split(',')])


def solve(puzzle):
  length = len(puzzle)
  mid = puzzle[length//2]
  part1 = sum(abs(x-mid) for x in puzzle)
  
  mean = sum(puzzle) // length
  gauss = lambda x: x * (x+1) // 2
  part2 = min(sum(gauss(abs(x-mean)) for x in puzzle),
              sum(gauss(abs(x-mean-1)) for x in puzzle))    
  
  return part1, part2  


print(solve(read_puzzle('Tag_07.txt')))