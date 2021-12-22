# based on an idea from Boojum, reddit
# https://www.reddit.com/r/adventofcode/comments/rlxhmg/2021_day_22_solutions/hpizza8/

from time import perf_counter as pfc
from collections import Counter
import re


def read_puzzle(filename):
  with open(filename) as f:
    return [(1 if x[1] == 'n' else -1, tuple(map(int, re.findall('-?\d+', x))))
            for x in f.readlines()]


def store_cube_volumes(puzzle, cubes, part1):
  for sign, volume in puzzle:
    if part1 and (max(volume) > 50 or min(volume) < -50): continue
    newCubes = Counter()
    x0, x1, y0, y1, z0, z1 = volume
    for (ex0, ex1, ey0, ey1, ez0, ez1), esign in cubes.items():
      ix0, ix1 = max(x0, ex0), min(x1, ex1)
      iy0, iy1 = max(y0, ey0), min(y1, ey1)
      iz0, iz1 = max(z0, ez0), min(z1, ez1)
      if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
        newCubes[(ix0, ix1, iy0, iy1, iz0, iz1)] -= esign
    if sign > 0:
      newCubes[volume] += sign
    cubes.update(newCubes)
  return cubes


def solve(puzzle, part1=True):
  cubes = Counter()
  cubes = store_cube_volumes(puzzle, cubes, part1)
  print(len(cubes))
  return sum((x1 - x0+1) * (y1-y0+1) * (z1-z0+1) * sign
             for (x0, x1, y0, y1, z0, z1), sign in cubes.items())


start = pfc()
print(solve(read_puzzle('Tag_22.txt')))
print(solve(read_puzzle('Tag_22.txt'), False))
print(pfc()-start)
