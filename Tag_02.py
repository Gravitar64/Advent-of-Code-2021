def read_puzzle(file):
  with open(file) as f:
    return [(row.split()[0], int(row.split()[1])) for row in f]


def solve(puzzle):
  horizontal = depth = aim = 0
  for direction, x in puzzle:
    if direction == 'forward':
      horizontal += x
      depth += aim * x
    else:
      aim += x if direction == 'down' else -x
  return horizontal * aim, horizontal * depth


print(solve(read_puzzle('Tag_02.txt')))