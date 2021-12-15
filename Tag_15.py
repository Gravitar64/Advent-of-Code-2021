from time import perf_counter as pfc
import heapq as hp


def read_puzzle(file):
  with open(file) as f:
    return {(x, y): int(n) for y, row in enumerate(f.read().split('\n')) for x, n in enumerate(row)}


def dijkstra(grid, target, start=(0, 0), risk=0):
  queue, minRisk = [(risk, start)], {start: risk}
  
  while queue:
    risk, (x, y) = hp.heappop(queue)
    if (x, y) == target: return risk

    for neighb in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
      if neighb not in grid or neighb in minRisk: continue
      newRisk = risk + grid[neighb]
      if newRisk < minRisk.get(neighb, 999999):
        minRisk[neighb] = newRisk
        hp.heappush(queue, (newRisk, neighb))


def solve(puzzle):
  maxX, maxY = map(max, zip(*puzzle))
  part1 = dijkstra(puzzle, (maxX, maxY))

  puzzle2 = {}
  for j in range(5):
    for i in range(5):
      for (x, y), value in puzzle.items():
        newXY = (x + (maxX+1) * i, y + (maxY+1) * j)
        newVal = value + i + j
        puzzle2[newXY] = newVal if newVal < 10 else newVal % 9

  maxX, maxY = map(max, zip(*puzzle2))
  part2 = dijkstra(puzzle2, (maxX, maxY))
  
  return part1, part2


start = pfc()
print(solve(read_puzzle('Tag_15.txt')))
print(pfc()-start)
