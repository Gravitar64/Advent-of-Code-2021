from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return {(x, y): int(n) for y, row in enumerate(f.readlines()) for x, n in enumerate(row.strip())}


def solve(puzzle):
  part1 = part2 = 0

  for step in range(100_000):
    for pos in puzzle:
      puzzle[pos] += 1

    while True:
      flashed = False
      for (x, y), value in puzzle.items():
        if value < 10: continue
        puzzle[(x, y)], flashed = 0, True
        if step < 100:
          part1 += 1
        for neighbor in ((x+1, y),   (x-1, y),   (x, y-1),   (x, y+1),
                         (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)):
          if neighbor not in puzzle or puzzle[neighbor] == 0: continue
          puzzle[neighbor] += 1
      if not flashed: break

    if sum(puzzle.values()) == 0:
      part2 = step+1
      break

  return part1, part2


start = pfc()
print(solve(read_puzzle('Tag_11.txt')))
print(pfc()-start)
