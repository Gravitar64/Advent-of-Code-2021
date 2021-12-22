from time import perf_counter as pfc
import re
from itertools import product


def read_puzzle(filename):
  with open(filename) as f:
    return [(x[1],list(map(int,re.findall('-?\d+',x)))) for x in f.readlines()]


def build_grid(puzzle,grid,part1):
  for i,(switch, coord) in enumerate(puzzle):
    
    print(f'Line {i}')
    if part1 and (max(coord) > 50 or min(coord) < -50): continue
    xf,xt,yf,yt,zf,zt = coord
    for cubic in product(range(xf,xt+1), range(yf,yt+1), range(zf,zt+1)):
      if switch == 'n':
        grid.add(cubic)
      else:
        grid.discard(cubic)
  return grid        



def solve(puzzle,part1=True):
  grid = set()
  grid=build_grid(puzzle,grid,part1)
  return len(grid)  
  

start = pfc()
print(solve(read_puzzle('Tag_22.txt')))
print(solve(read_puzzle('Tag_22.txt'),False))
print(pfc()-start)
