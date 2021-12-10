from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return [x.strip() for x in f.readlines()]


def solve(puzzle):
  pairs  = {a: b for a, b in zip('([{<', ')]}>')}
  points = {a: b for a, b in zip(')]}>', [3, 57, 1197, 25137])}

  part1, part2 = 0, []
  for row in puzzle:
    stack, score = [], 0
    for c in row:
      if c in pairs:
        stack.append(pairs[c])
      elif stack.pop() != c:
        part1 += points[c]
        break
    else:
      for c in reversed(stack):
        score = score * 5 + ' )]}>'.index(c)
      part2.append(score)
  return part1, sorted(part2)[len(part2)//2]


start = pfc()
print(solve(read_puzzle('Tag_10.txt')))
print(pfc()-start)