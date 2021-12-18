# Sourcecode by Benedikt Werner https://github.com/benediktwerner/AdventOfCode/blob/master/2021/day18/sol.py
# Dient als Anschauungsbeispiel für eine rekursive Lösung in 3,72 Sekunden 

from time import perf_counter as pfc
import itertools, math
from functools import reduce


def read_puzzle(file):
  with open(file) as f:
    return list(map(eval, f.read().splitlines()))


def add_left(x, n):
  if n is None: return x
  if isinstance(x, int): return x + n
  return [add_left(x[0], n), x[1]]


def add_right(x, n):
  if n is None:  return x
  if isinstance(x, int):  return x + n
  return [x[0], add_right(x[1], n)]


def explode(x, n=4):
  if isinstance(x, int): return False, None, x, None
  if n == 0: return True, x[0], 0, x[1]
  
  a, b = x
  exp, left, a, right = explode(a, n - 1)
  if exp:  return True, left, [a, add_left(b, right)], None
  
  exp, left, b, right = explode(b, n - 1)
  if exp:  return True, None, [add_right(a, left), b], right
  
  return False, None, x, None


def split(x):
  if isinstance(x, int):
    if x >= 10: return True, [x // 2, math.ceil(x / 2)]
    return False, x
  a, b = x
  change, a = split(a)
  if change: return True, [a, b]
  change, b = split(b)
  return change, [a, b]


def add(a, b):
  x = [a, b]
  while True:
    change, _, x, _ = explode(x)
    if change: continue
    change, x = split(x)
    if not change: break
  return x


def magnitude(x):
  if isinstance(x, int): return x
  return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


def solve(puzzle):
  part1 = magnitude(reduce(add, puzzle))
  part2 = max(magnitude(add(a, b)) for a, b in itertools.permutations(puzzle, 2))
  return part1, part2


start = pfc()
print(solve(read_puzzle('Tag_18.txt')))
print(pfc()-start)
