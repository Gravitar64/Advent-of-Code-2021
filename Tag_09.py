from time import perf_counter as pfc
import math


def read_puzzle(file):
  with open(file) as f:
    return {(x, y): int(n) for y, row in enumerate(f.readlines())
            for x, n in enumerate(row.strip()) if n != '9'}


def is_low_point(x,y, value, puzzle):
  for neighbor in ((x-1,y), (x+1,y), (x,y+1), (x,y-1)):
    if value > puzzle.get(neighbor, 9): break
  else:
    return True


def bassin(queue, visited, puzzle):
  while queue:
    x,y = queue.pop(0)
    for neighbor in ((x-1,y), (x+1,y), (x,y+1), (x,y-1)):
      value = puzzle.get(neighbor, 9)
      if value == 9 or neighbor in visited or puzzle[(x,y)] > value: continue
      visited.add(neighbor)
      queue.append(neighbor)
  return len(visited)


def solve(puzzle):
  part1, part2 = 0, []
  for pos, value in puzzle.items():
    if not is_low_point(*pos, value, puzzle): continue
    part1 += value+1
    part2.append(bassin([pos], {pos}, puzzle))
  return part1, math.prod(sorted(part2)[-3:])


start = pfc()
print(solve(read_puzzle('Tag_09.txt')))
print(pfc()-start)