from time import perf_counter as pfc
from collections import Counter


def read_puzzle(file):
  with open(file) as f:
    template, insertions = f.read().split('\n\n')
    chars = Counter(template)
    template = Counter(a+b for a, b in zip(template, template[1:]))
    insertions = {x[:2]: x[6] for x in insertions.split('\n')}
  return template, insertions, chars


def solve(template, insertions, chars, steps):
  for _ in range(steps):
    t2 = Counter()
    for (a, b), value in template.items():
      insert         = insertions[a+b]
      t2[a+insert]  += value
      t2[insert+b]  += value
      chars[insert] += value
    template = t2
  return max(chars.values()) - min(chars.values())


start = pfc()
print(solve(*read_puzzle('Tag_14.txt'), 10))
print(solve(*read_puzzle('Tag_14.txt'), 40))
print(pfc()-start)
