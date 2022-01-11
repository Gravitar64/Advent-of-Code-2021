from time import perf_counter as pfc


def read_puzzle(filename):
  with open(filename) as f:
    return [row.split() for row in f.read().split("\n")]


def get_relevant_adds(puzzle):
  div1, div26 = [], []
  for i in range(0, len(puzzle), 18):
    if puzzle[i + 4][2] == "1":
      div1.append(int(puzzle[i + 15][2]))
      div26.append(None)
    else:
      div1.append(None)
      div26.append(int(puzzle[i + 5][2]))
  return div1, div26


def get_model_no(div1, div26):
  part1, part2 = [0] * 14, [0] * 14
  stack = []
  for i, (a, b) in enumerate(zip(div1, div26)):
    if a:
      stack.append((i, a))
    else:
      ia, a = stack.pop()
      diff = a + b
      part1[ia] = min(9, 9 - diff)
      part1[i] = min(9, 9 + diff)
      part2[ia] = max(1, 1 - diff)
      part2[i] = max(1, 1 + diff)
  return part1, part2


def solve(puzzle, ):
  div1, div26 = get_relevant_adds(puzzle)
  part1, part2 = get_model_no(div1, div26)
  return int("".join(map(str, part1))), int("".join(map(str, part2)))


start = pfc()
print(solve(read_puzzle("Tag_24.txt")))
print(pfc() - start)
