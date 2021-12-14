from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    dots, folds = f.read().split('\n\n')
    dots = {tuple(map(int, row.strip().split(','))) for row in dots.split('\n')}
    folds = [(s[11] == 'y', int(s[13:])) for s in folds.split('\n')]
    return dots, folds


def fold(dim, value, dots):
  folded = {dot for dot in dots if dot[dim] < value}
  for x, y in dots-folded:
    folded.add((x, 2*value-y) if dim else (2*value-x, y))
  return folded


def solve(dots, folds):
  print(len(fold(*folds[0], dots)))
  
  for dim, value in folds:
    dots = fold(dim, value, dots)

  maxX, maxY = map(max, zip(*dots))
  for y in range(maxY+1):
    for x in range(maxX+1):
      print('▓' if (x, y) in dots else ' ', end='')
    print()


start = pfc()
solve(*read_puzzle('Tag_13.txt'))
print(pfc()-start)
