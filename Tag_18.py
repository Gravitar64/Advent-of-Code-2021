from time import perf_counter as pfc
from functools import reduce
from itertools import permutations


def read_puzzle(filename):
  with open(filename) as f:
    return f.readlines()


def gen_flatlist(puzzle):
  flatlist = []
  for line in puzzle:
    flatline, depth = [], 0
    for c in line:
      if c == '[':       depth += 1
      elif c == ']':     depth -= 1
      elif c.isdigit():  flatline.append([int(c), depth])
    flatlist.append(flatline)
  return flatlist


def explode(x):
  for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(x, x[1:])):
    if depth1 < 5 or depth1 != depth2: continue
    if i > 0:          x[i-1][0] += num1
    if i < len(x)-2:   x[i+2][0] += num2
    x = x[:i] + [[0, depth1-1]] + x[i+2:]
    return True, x
  return False, x


def split(x):
  for i, (num, depth) in enumerate(x):
    if num < 10:  continue
    down = num // 2
    up = num - down
    x = x[:i] + [[down, depth+1]] + [[up, depth+1]] + x[i+1:]
    return True, x
  return False, x


def add(a, b):
  x = [[entry[0], entry[1]+1] for entry in a + b]
  while True:
    change, x = explode(x)
    if change:  continue
    change, x = split(x)
    if not change: break
  return x


def magnitude(x):
  while len(x) > 1:
    for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(x, x[1:])):
      if depth1 != depth2: continue
      val = num1 * 3 + num2 * 2
      x = x[:i]+[[val, depth1-1]]+x[i+2:]
      break
  return x[0][0]


def solve(puzzle):
  flatlist = gen_flatlist(puzzle)
  part1 = magnitude(reduce(add, flatlist))
  part2 = max(magnitude(add(a, b)) for a, b in permutations(flatlist, 2))
  return part1, part2


start = pfc()
print(solve(read_puzzle('Tag_18.txt')))
print(pfc()-start)
