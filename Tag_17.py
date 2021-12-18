from time import perf_counter as pfc
import re
import math
from itertools import product


def read_puzzle(file):
  with open(file) as f:
    return list(map(int, re.findall('-?\d+', f.read())))


def solve(minX, maxX, minY, maxY):
  part1 = -minY * (-minY-1) // 2  # gauss

  def gauss_inv(n):
    return 0.5 * (math.sqrt(8*n+1)-1)

  def sum_partial(m, n):
    return n*(n+1)/2 - m*(m+1)/2

  def gen_interval(a, b):
    return range(math.ceil(a), math.floor(b)+1)

  def ys(t, ymin, ymax):
    return gen_interval(1/t*(ymin + (t**2/2 - t/2)), 1/t*(ymax + (t**2/2 - t/2)))

  def xs(t, xmin, xmax):
    st = sum_partial(0, t)
    if st > xmax:
      return gen_interval(gauss_inv(xmin), gauss_inv(xmax))
    elif st < xmin:
      return gen_interval(xmin/t - st/t + t, xmax/t - st/t + t)
    else:
      return gen_interval(gauss_inv(xmin), xmax/t - st/t + t)


  valid_vels = set()
  for t in range(1, 200):
    for (x, y) in product(xs(t, minX, maxX), ys(t, minY, maxY)):
      valid_vels.add((x, y))
  part2 = len(valid_vels)

  return part1, part2


start = pfc()
print(solve(*read_puzzle('Tag_17.txt')))
print(pfc()-start)
