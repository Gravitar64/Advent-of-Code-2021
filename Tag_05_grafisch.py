import pygame as pg
import re
from collections import Counter


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
  return diagram
  

screen = pg.display.set_mode((1000,1000))
clock = pg.time.Clock()
FPS = 1
d = solve(read_puzzle('Tag_05.txt'),False)

while True:
  clock.tick(FPS)
  for ereignis in pg.event.get():
    if ereignis.type == pg.QUIT: quit()
  screen.fill((0,0,0))
  for point,value in d.items():
    if value == 1: continue
    screen.set_at(point, '#00ff00')

  pg.display.flip()
