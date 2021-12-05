import re
from collections import defaultdict


def read_puzzle(file):
  with open(file) as f:
    return [list(map(int, re.findall('\d+', row))) for row in f]


def fill_diagram(x1, y1, x2, y2, diagram, onlyHorVer):
  if onlyHorVer and x1 != x2 and y1 != y2: return
  points_count = max(abs(x1-x2), abs(y1-y2))
  stepX, stepY = (x2-x1)//points_count, (y2-y1)//points_count
  for n in range(points_count+1):
    x, y = x1+n*stepX, y1+n*stepY
    diagram[(x, y)] += 1


def solve(puzzle):
  diagram1, diagram2 = defaultdict(int), defaultdict(int)
  for line in puzzle:
    fill_diagram(*line, diagram1, True)
    fill_diagram(*line, diagram2, False)

  return sum(x >= 2 for x in diagram1.values()), \
         sum(x >= 2 for x in diagram2.values())


print(solve(read_puzzle('Tag_05.txt')))