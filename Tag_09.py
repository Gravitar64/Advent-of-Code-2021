from time import perf_counter as pfc
import math


def read_puzzle(file):
  with open(file) as f:
    return {(x, y): int(n) for y, row in enumerate(f.readlines())
            for x, n in enumerate(row.strip())}


def neighbors(x, y):
  for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    yield (x+dx, y+dy)


def is_low_point(pos, value, puzzle):
  for neighbor in neighbors(*pos):
    if puzzle.get(neighbor, 9) <= value: break
  else:
    return True


def bassin(node, puzzle):
  queue, visited = [node], {node}
  while queue:
    pos = queue.pop(0)
    for neighbor in neighbors(*pos):
      value = puzzle.get(neighbor, 9)
      if value == 9 or neighbor in visited or value <= puzzle[pos]: continue
      visited.add(neighbor)
      queue.append(neighbor)
  return len(visited)


def solve(puzzle):
  part1, part2 = 0, []
  
  for pos, value in puzzle.items():
    if not is_low_point(pos, value, puzzle): continue
    part1 += value+1
    part2.append(bassin(pos, puzzle))

  return part1, math.prod(sorted(part2)[-3:])


start = pfc()
print(solve(read_puzzle('Tag_09.txt')))
print(pfc()-start)