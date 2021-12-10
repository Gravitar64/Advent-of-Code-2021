from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return [x.strip() for x in f.readlines()]


def solve(puzzle):
  pairs = {a: b for a, b in zip('([{<', ')]}>')}
  points = {a: b for a, b in zip(')]}>', [(3, 1), (57, 2), (1197, 3), (25137, 4)])}

  part1, part2 = 0, []
  for row in puzzle:
    stack = []
    for c in row:
      if c in pairs:
        stack.append(pairs[c])
      elif stack.pop() != c:
        part1 += points[c][0]
        break
    else:
      total_score = 0
      for c in reversed(stack):
        total_score = total_score*5+points[c][1]
      part2.append(total_score)
  return part1, sorted(part2)[len(part2)//2]


start = pfc()
print(solve(read_puzzle('Tag_10.txt')))
print(pfc()-start)