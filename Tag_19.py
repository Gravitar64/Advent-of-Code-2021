from time import perf_counter as pfc
import re
from itertools import combinations, product
from collections import Counter


def read_puzzle(filename):
  with open(filename) as f:
    return [[tuple(int(x) for x in re.findall('-?\d+', row))
            for row in scanner.split('\n')[1:]]
            for scanner in f.read().split('\n\n')]


def search_alignment(scanner1, scanner2):
  aligned, delta = [], []
  dp = dpp = None
  
  for dim in range(3):
    x = [pos[dim] for pos in scanner1]
    
    for d, s in [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]:
      if d == dp or d == dpp: continue
      t = [pos[d]*s for pos in scanner2]
      w = [b-a for a, b in product(x, t)]
      num, count = Counter(w).most_common()[0]
      if count >= 12: break
    
    if count < 12: return None
    dpp, dp = dp, d
    aligned.append([v - num for v in t])
    delta.append(num)
  
  return list(zip(*aligned)), delta


def manhDist(pos1, pos2):
  return sum(abs(b-a) for a,b in zip(pos1,pos2))


def solve(puzzle):
  first, *rest = puzzle
  chache, beacons, scannerPos = [first], set(), [[0,0,0]]
  
  while chache:
    scanner1 = chache.pop()
    for scanner2 in rest:
      if (r := search_alignment(scanner1, scanner2)):
        aligned, delta = r
        scannerPos.append(delta)
        chache.append(aligned)
        rest.remove(scanner2)
    beacons.update(scanner1)
  
  part1 = len(beacons)
  part2 = max(manhDist(p1,p2) for p1, p2 in combinations(scannerPos,2))
  return part1, part2            


start = pfc()
print(solve(read_puzzle('Tag_19.txt')))
print(pfc()-start)