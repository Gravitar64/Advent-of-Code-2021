from time import perf_counter as pfc
from collections import Counter


def read_puzzle(file):
  with open(file) as f:
    raw = f.read().split('\n')
    chars = Counter(raw[0])
    template = Counter(a+b for a, b in zip(raw[0],raw[0][1:]))
    insertions = {x[:2]: x[6] for x in raw[2:]}
  return template, insertions, chars


def solve(old_temp, insertions, chars, steps):
  for _ in range(steps):
    new_temp = Counter()
    for (a, b), value in old_temp.items():
      insert               = insertions[a+b]
      new_temp[a+insert]  += value
      new_temp[insert+b]  += value
      chars[insert]       += value
    old_temp = new_temp
  return max(chars.values()) - min(chars.values())


start = pfc()
print(solve(*read_puzzle('Tag_14.txt'), 10))
print(solve(*read_puzzle('Tag_14.txt'), 40))
print(pfc()-start)
