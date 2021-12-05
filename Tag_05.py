import re
from collections import defaultdict


def read_puzzle(file):
  with open(file) as f:
    return [[int(coord) for coord in re.findall('\d+', row)] for row in f]


def solve(puzzle):
  diagram1, diagram2 = defaultdict(int), defaultdict(int)
  
  for x1, y1, x2, y2 in puzzle:
    points_count = max(abs(x1-x2), abs(y1-y2))
    stepX, stepY = (x2-x1)//points_count, (y2-y1)//points_count
    
    for n in range(points_count+1):
      x, y = x1 + n * stepX, y1 + n * stepY
      diagram2[(x, y)] += 1
      if x1 == x2 or y1 == y2:
        diagram1[(x, y)] += 1
  
  return sum(x > 1 for x in diagram1.values()), \
         sum(x > 1 for x in diagram2.values())


print(solve(read_puzzle('Tag_05.txt')))