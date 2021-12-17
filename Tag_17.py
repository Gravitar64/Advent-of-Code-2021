from time import perf_counter as pfc
import re

def read_puzzle(file):
  with open(file) as f:
    return list(map(int, re.findall('-?\d+',f.read())))
    
def solve(minX, maxX, minY, maxY):
  part1 = part2 = 0
  for dy in range(minY,-minY):
    for dx in range(1,maxX+1):
      x = y = highest = 0
      vx, vy = dx, dy
      while x <= maxX and y >= minY:
        x,y,highest = x+vx, y+vy, max(highest,y)
        vx, vy = max(0, vx-1), vy - 1
        if minX <= x <= maxX and minY <= y <= maxY: 
          part1 = max(highest,part1)
          part2 += 1
          break
  return part1,part2





start = pfc()
print(solve(*read_puzzle('Tag_17.txt')))
print(pfc()-start)