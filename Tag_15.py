from time import perf_counter as pfc



def read_puzzle(file):
  with open(file) as f:
    return {(x,y):int(n) for y,row in enumerate(f.read().split('\n')) for x,n in enumerate(row)}

def neighbors(x,y,graph):
  n = []
  for neighb in ((x+1,y), (x,y+1)):
    if neighb not in graph: continue
    n.append((graph[neighb], neighb))
  n = sorted(n)
  return [x[1] for x in n]  
    


best = 999999
def dfs(node, graph, visited, target, risk=0):
  global best
  if node == target: return risk
  for neighb in neighbors(*node, graph):
    if neighb in visited: continue
    erg = dfs(neighb, graph, visited | {neighb}, target, risk + graph[neighb])
    if erg < best:
      best = erg
      print(best)  
  return best  


def solve(puzzle):
  maxX, maxY = map(max,zip(*puzzle))
  return dfs((0,0), puzzle, {(0,0)}, (maxX, maxY))
  


start = pfc()
print(solve(read_puzzle('Tag_15.txt')))
print(pfc()-start)
