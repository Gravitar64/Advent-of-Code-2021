from time import perf_counter as pfc



def read_puzzle(file):
  with open(file) as f:
    return {(x,y):int(n) for y,row in enumerate(f.read().split('\n')) for x,n in enumerate(row)}

def neighbor(x,y,graph):
  best = 99
  for neighb in ((x+1,y), (x,y+1)):
    score = 0
    if neighb not in graph: continue
    nx, ny = neighb
    for n2 in ((nx+1,ny), (nx,ny+1)):
      if n2 not in graph: continue
      score += graph[n2]
    if score < best:
      best = score
      best_neighb = neighb
  return best_neighb
    


best,path = 999999, [(0,0)]
def dfs(node, graph, target, risk=0):
  global best
  if node == target: return risk
  neighb = neighbor(*node, graph)
  path.append(neighb)
  erg = dfs(neighb, graph, target, risk + graph[neighb])
  return erg  


def solve(puzzle):
  maxX, maxY = map(max,zip(*puzzle))
  part1 = dfs((0,0), puzzle, (maxX, maxY))
  return path
  


start = pfc()
print(solve(read_puzzle('Tag_15.txt')))
print(pfc()-start)
