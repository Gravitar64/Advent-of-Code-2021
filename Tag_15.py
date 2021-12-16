from time import perf_counter as pfc
import heapq as hp


def read_puzzle(file):
  with open(file) as f:
    return {(x, y): int(n) for y, row in enumerate(f.read().split('\n')) for x, n in enumerate(row)}


def value(grid, x, y, w, h):
  c = grid[x % w, y % h] + x // w + y // h
  return c if c < 10 else c % 9


def bfs(grid, w, h, scale):
  queue, visited = [(0, 0, 0)], {(0, 0)}
  
  while queue:
    risk, x, y = hp.heappop(queue)
    if (x, y) == (w*scale-1, h*scale-1): return risk
    
    for neighb in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
      if neighb in visited: continue
      if 0 <= neighb[0] < w*scale and 0 <= neighb[1] < h*scale:
        newRisk = risk + value(grid, *neighb, w, h)
        visited.add(neighb)
        hp.heappush(queue, (newRisk, *neighb))


def solve(puzzle):
  maxX, maxY = map(max, zip(*puzzle))
  w, h = maxX+1, maxY+1
  part1 = bfs(puzzle, w, h, 1)
  part2 = bfs(puzzle, w, h, 5)
  return part1, part2


start = pfc()
print(solve(read_puzzle('Tag_15.txt')))
print(pfc()-start)