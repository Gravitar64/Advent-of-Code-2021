import re
from collections import Counter
from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return [[int(n) for n in re.findall('\d+', row)] for row in f]


def solve(puzzle, part1):
  diagram = Counter()
  for x1, y1, x2, y2 in puzzle:
    if part1 and x1 != x2 and y1 != y2: continue 
    points = max(abs(x1-x2), abs(y1-y2))
    stepX, stepY = (x2-x1)//points, (y2-y1)//points
    diagram.update([(x1 + n * stepX, y1 + n * stepY) for n in range(points+1)])
  return sum(x > 1 for x in diagram.values())  
  

start=pfc()
print(solve(read_puzzle('Tag_05.txt'), True))
print(pfc()-start)
start=pfc()
print(solve(read_puzzle('Tag_05.txt'),False))
print(pfc()-start)