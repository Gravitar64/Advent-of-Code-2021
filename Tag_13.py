from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    dots, folds = f.read().split('\n\n')
    dots = {tuple(map(int, row.strip().split(',')))
            for row in dots.split('\n')}
    folds = [(s[11], int(s[13:])) for s in folds.split('\n')]
    return dots, folds


def fold(dimension, value, dots):
  folded = {(x, y) for x, y in dots if eval(dimension) < value}
  for x, y in dots-folded:
    newPos = (x, value-(y-value)) if dimension == 'y' else (value-(x-value), y)
    folded.add(newPos)
  return folded


def solve(dots, folds, part1=True):
  if part1:
    print(len(fold(*folds[0], dots)))
    return

  for dimension, value in folds:
    dots = fold(dimension, value, dots)

  for y in range(max(y for _, y in dots)+1):
    print()
    for x in range(max(x for x, _ in dots)+1):
      print('#', end='') if (x, y) in dots else print(' ', end='')
  print()


start = pfc()
solve(*read_puzzle('Tag_13.txt'))
solve(*read_puzzle('Tag_13.txt'), False)
print(pfc()-start)
