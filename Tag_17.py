from time import perf_counter as pfc
import re


def read_puzzle(file):
  with open(file) as f:
    return list(map(int, re.findall('-?\d+', f.read())))


def solve(minX, maxX, minY, maxY):
  part1 = -minY * (-minY-1) // 2 # gauss

  part2 = 0
  for dy in range(minY, -minY):
    #lowBound for dx = gauss inverse of minX (lowest possible velX to reach minX)
    for dx in range(int(((8*minX+1)**0.5-1)/2), maxX+1): 
      x = y = 0
      vx, vy = dx, dy
      while vx != 0 and x <= maxX and y >= minY: 
        x, y = x+vx, y+vy
        vx, vy = max(0, vx-1), vy - 1
        if minX <= x <= maxX and minY <= y <= maxY:
          part2 += 1
          break

  return part1, part2


start = pfc()
print(solve(*read_puzzle('Tag_17.txt')))
print(pfc()-start)
