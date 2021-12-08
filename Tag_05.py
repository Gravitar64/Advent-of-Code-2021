import re
from collections import Counter
from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return [[int(n) for n in re.findall('\d+', row)] for row in f]


def solve(puzzle):
  diagram1,diagram2 = Counter(), Counter()
  for x1, y1, x2, y2 in puzzle:
    points = max(abs(x1-x2), abs(y1-y2))
    stepX, stepY = (x2-x1)//points, (y2-y1)//points
    if x1 == x2 or  y1 == y2:
      diagram1.update([(x1 + n * stepX, y1 + n * stepY) for n in range(points+1)]) 
    diagram2.update([(x1 + n * stepX, y1 + n * stepY) for n in range(points+1)]) 
  return (sum(x > 1 for x in diagram1.values()),  
          sum(x > 1 for x in diagram2.values()))

start=pfc()
print(solve(read_puzzle('Tag_05.txt')))
print(pfc()-start)