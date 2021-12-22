# based on an idea from Boojum, reddit
# https://www.reddit.com/r/adventofcode/comments/rlxhmg/2021_day_22_solutions/hpizza8/

from time import perf_counter as pfc
from collections import Counter
import re


def read_puzzle(filename):
  with open(filename) as f:
    return [(1 if x[1] == 'n' else -1, tuple(map(int, re.findall('-?\d+', x))))
            for x in f.readlines()]


def size(x0, x1, y0, y1, z0, z1):
  return (x1 - x0+1) * (y1-y0+1) * (z1-z0+1)


def intersect(x0, x1, y0, y1, z0, z1, x2, x3, y2, y3, z2, z3):
  ix0, ix1 = max(x0, x2), min(x1, x3)
  iy0, iy1 = max(y0, y2), min(y1, y3)
  iz0, iz1 = max(z0, z2), min(z1, z3)
  if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
    return ix0, ix1, iy0, iy1, iz0, iz1 


def store_cube_volumes(puzzle, part1, cubes=Counter()):
  for sign1, volume1 in puzzle:
    if part1 and (max(volume1) > 50 or min(volume1) < -50): continue
    
    newCubes = Counter()
    for volume2, sign2 in cubes.items():
      if (inter := intersect(*volume1, *volume2)):
        newCubes[inter] -= sign2
        if newCubes[inter] == 0: del newCubes[inter]
    if sign1 == 1:
      cubes[volume1] += sign1
    cubes.update(newCubes)
  
  return cubes


def solve(puzzle, part1=True):
  cubes = store_cube_volumes(puzzle, part1)
  return sum(size(*volume) * sign for volume, sign in cubes.items())


start = pfc()
print(solve(read_puzzle('Tag_22.txt')))
print(solve(read_puzzle('Tag_22.txt'), False))
print(pfc()-start)
