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
  t = {632:'0', 222:'1', 521:'2', 532:'3', 442:'4',  
       531:'5', 631:'6', 322:'7', 742:'8', 642:'9'}
  
  for pattern, output in zip(patterns,outputs):
    part2 += int(''.join(
                 [t[len(s)*100+len(s&pattern[4])*10+len(s&pattern[2])]          
                 for s in output]))
  
  return part1, part2

start = pfc()
print(solve(*read_puzzle('Tag_08.txt')))
print(pfc()-start)

