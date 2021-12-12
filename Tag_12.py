from time import perf_counter as pfc
from collections import defaultdict


def read_puzzle(file):
  puzzle = defaultdict(list)
  with open(file) as f:
    for row in f.readlines():
      a, b = row.strip().split('-')
      puzzle[a].append(b)
      puzzle[b].append(a)
  return puzzle


def dfs(node, graph, seen, twice):
    paths = 0
    if node == 'end': return 1
    for dest in graph[node]:
        if dest.islower():
            if dest not in seen:
                paths += dfs(dest, graph, seen | {dest}, twice)
            elif twice and dest not in {'start', 'end'}:
                paths += dfs(dest, graph, seen | {dest}, False)
        else:
            paths += dfs(dest, graph, seen, twice)
    return paths


def solve(puzzle):
  part1 = dfs('start', puzzle, {'start'}, False)
  part2 = dfs('start', puzzle, {'start'}, True)
  return part1, part2


start = pfc()
print(solve(read_puzzle('Tag_12.txt')))
print(pfc()-start)
