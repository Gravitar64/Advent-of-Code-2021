def read_puzzle(file):
  with open(file) as f:
    return list(map(int, f))


def solve(puzzle):
  a = sum([b > a for a, b in zip(puzzle, puzzle[1:])])
  b = sum([sum(puzzle[i+1:i+4]) > sum(puzzle[i:i+3])
           for i in range(0, len(puzzle)-2)])
  return a, b


print(solve(read_puzzle('Tag_01.txt')))