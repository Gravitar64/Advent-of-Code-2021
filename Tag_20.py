from time import perf_counter as pfc
from itertools import product


def read_puzzle(filename):
  with open(filename) as f:
    algo, _, *picture = f.read().split('\n')
    algo = [str('.#'.index(c)) for c in algo]
    picture = {(x, y): str('.#'.index(c)) for y, row in enumerate(picture)
               for x, c in enumerate(row)}
    return algo, picture


def solve(algo, picture, loops):
  square = list(product(range(-1, 2), repeat=2))
  centres = lambda a: {(x+dx, y+dy) for x, y in a for dy, dx in square}

  def enhance(x, y, i):
    dual = [picture.get((x+dx, y+dy), '01'[i % 2]) for dy, dx in square]
    return algo[int(''.join(dual), 2)]

  for i in range(loops):
    picture = {(x, y): enhance(x, y, i) for x, y in centres(picture)}

  return list(picture.values()).count('1')


start = pfc()
print(solve(*read_puzzle('Tag_20.txt'), 2))
print(solve(*read_puzzle('Tag_20.txt'), 50))
print(pfc()-start)
