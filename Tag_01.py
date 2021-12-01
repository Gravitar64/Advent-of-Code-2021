from time import perf_counter as pfc


def puzzle_einlesen(datei):
  with open(datei) as f:
    return [int(x) for x in f]


def löse(puzzle):
  a = sum([b > a for a, b in zip(puzzle, puzzle[1:])])
  b = sum([sum(puzzle[i+1:i+4]) > sum(puzzle[i:i+3])
           for i in range(0, len(puzzle)-2)])
  return a, b


puzzle = puzzle_einlesen('Tag_01.txt')
start = pfc()
print(löse(puzzle), pfc()-start)
