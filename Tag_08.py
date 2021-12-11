from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    patterns, outputs = [], []
    for row in f:
      left, right = row.split('|')
      patterns.append({len(x): set(x) for x in left.split()})
      outputs.append([set(x) for x in right.split()])
  return patterns, outputs


def gen_signatures():
  example = 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'.split()
  example = [set(x) for x in example]
  pattern = {len(x): x for x in example}
  return {get_signature(x, pattern): str(i) for i, x in enumerate(example)}


def get_signature(x, pattern):
  a, b, c, d = len(x), x & pattern[2], x & pattern[3], x & pattern[4]
  return a, len(b), len(c), len(d)


def solve(patterns, outputs):
  part1 = sum([len(n) in {2, 4, 3, 7} for row in outputs for n in row])
  part2 = 0
  signatures = gen_signatures()
  for pattern, output in zip(patterns, outputs):
    part2 += int(''.join(signatures[get_signature(x, pattern)] for x in output))
  return part1, part2


start = pfc()
print(solve(*read_puzzle('Tag_08.txt')))
print(pfc()-start)
