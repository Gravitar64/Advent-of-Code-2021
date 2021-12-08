#based on the idea of 4HbQ https://www.reddit.com/r/adventofcode/comments/rbj87a/2021_day_8_solutions/hnoyy04/?context=3

from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    patterns, outputs = [], []
    for row in f:
      a,b = row.split('|')
      patterns.append({len(x):set(x) for x in a.split()})
      outputs.append([set(x) for x in b.split()])
  return patterns, outputs    


def solve(patterns, outputs):
  part1 = sum(len(n) in {2, 4, 3, 7} for row in outputs for n in row)
  
  part2 = 0
  t = {(6,3,2):'0', (2,2,2):'1', (5,2,1):'2', (5,3,2):'3', (4,4,2):'4',  
       (5,3,1):'5', (6,3,1):'6', (3,2,2):'7', (7,4,2):'8', (6,4,2):'9'}
  
  for pattern, output in zip(patterns,outputs):
    part2 += int(''.join([
                 t[(len(s),len(s&pattern[4]),len(s&pattern[2]))]          
                 for s in output]))
  
  return part1, part2

start = pfc()
print(solve(*read_puzzle('Tag_08.txt')))
print(pfc()-start)

