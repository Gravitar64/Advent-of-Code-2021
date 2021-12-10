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
  return {get_sign(x, pattern): str(i) for i, x in enumerate(example)}


def get_sign(x, pattern):
  return len(x), len(x & pattern[2]), len(x & pattern[3]), len(x & pattern[4])


def solve(patterns, outputs):
  part1 = sum(len(n) in {2, 4, 3, 7} for row in outputs for n in row)

  part2, signatures = 0, gen_signatures()
  for pattern, output in zip(patterns, outputs):
    part2 += int(''.join(signatures[get_sign(s, pattern)] for s in output))
  return part1, part2


start = pfc()
print(solve(*read_puzzle('Tag_08.txt')))
print(pfc()-start)
