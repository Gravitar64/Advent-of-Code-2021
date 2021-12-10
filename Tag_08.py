#based on the idea of 4HbQ https://www.reddit.com/r/adventofcode/comments/rbj87a/2021_day_8_solutions/hnoyy04/?context=3

from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    patterns, outputs = [], []
    for row in f:
      left, right= row.split('|')
      patterns.append({len(x):set(x) for x in left.split() if len(x) in {2,4}})
      outputs.append([set(x) for x in right.split()])
  return patterns, outputs    


def solve(patterns, outputs):
  part1 = sum(len(n) in {2, 4, 3, 7} for row in outputs for n in row)
  
  part2 = 0
  t = {(6,2,3):'0', (2,2,2):'1', (5,1,2):'2', (5,2,3):'3', (4,2,4):'4',  
       (5,1,3):'5', (6,1,3):'6', (3,2,2):'7', (7,2,4):'8', (6,2,4):'9'}
  
  for pattern, output in zip(patterns,outputs):
    part2 += int(''.join(t[(len(s), len(s&pattern[2]), len(s&pattern[4]))] 
                         for s in output))
  return part1, part2

def gen_t():
  example = 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'.split()
  pattern = {len(x):set(x) for x in example}
  for x in example:
    x = set(x)
    print(len(x), len(x&pattern[2]), len(x&pattern[3]), len(x&pattern[4]))




start = pfc()
print(solve(*read_puzzle('Tag_08.txt')))
print(pfc()-start)

gen_t()