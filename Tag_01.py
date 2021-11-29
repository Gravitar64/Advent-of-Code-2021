from time import perf_counter as pfc

def puzzle_einlesen(datei):
  with open(datei) as f:
    return [int(x) for x in f]

def löse(puzzle):
  pass
     


puzzle = puzzle_einlesen('Tag_01.txt')
start = pfc()
print(löse(puzzle),pfc()-start)
