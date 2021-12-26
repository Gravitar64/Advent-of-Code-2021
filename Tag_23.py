from time import perf_counter as pfc

#Ideen
#1. kann ein amphipod aus der hallway in seinen Raum wechseln
#2. kann ein amphipod seinen raum in die hallway verlassen

def read_puzzle(filename):
  with open(filename) as f:
    return {(x,y):c for y,row in enumerate(f.read().split('\n')) for x,c in enumerate(row) if c not in'# '}

def room_solved(room, puzzle,targetsI):
  return all(puzzle[(room,y)] == targetsI[room] for y in range(1,3))

def can_leave_room(room, puzzle, targetsI):
  if room_solved(room, puzzle, targetsI): return False
  if puzzle[(room,2)] in 'ABCD': return (room,2)
  if puzzle[(room,3)] in 'ABCD' and puzzle[(room,3)] != targetsI[room]: return (room,3)

def can_enter_room(x,puzzle,targets):
  amphi = puzzle[(x,1)]
  room = targets[amphi]
  if all(puzzle[(room,y)] == '.' for y in range(2,4)): return room,3
  if puzzle[(room,3)] == amphi and puzzle[(room,2)] == '.': return room,2


def blocked(x1,x2,puzzle):
  step = 1 if x1 < x2 else -1
  return any(puzzle[v,1] != '.' for v in range(x1+step,x2+step,step))

def get_possible_hallway_pos(x,_,hallway,puzzle):
  for x2 in hallway:
    if puzzle[(x2,1)] != '.': continue
    if blocked(x,x2,puzzle): continue
    yield (x2,1)  

def distance(x1,y1,x2,y2):
  return abs(x2-x1)+abs(y2-y1)

def get_mapStr(puzzle):
  return ''.join(puzzle.values())

def swap(p1,p2):
  puzzle[p2], puzzle[p1] = puzzle[p1], puzzle[p2]  

seen = set()
def dfs(puzzle,cost):
  global minCost
  mapStr = get_mapStr(puzzle)
  #print(mapStr)
  if mapStr == '...........ABCDABCD':
    return cost
    
  for x in hallway:
    amphi = puzzle[(x,1)]
    if amphi == '.': continue
    if (pos2 := can_enter_room(x,puzzle,targets)):
      if blocked(x,pos2[0],puzzle): continue
      swap((x,1), pos2)
      mapStr = get_mapStr(puzzle)
      if mapStr in seen:
        swap((x,1), pos2)
        continue
      seen.add(mapStr)
      if (erg := dfs(puzzle, cost+distance(x,1,*pos2)*energy[amphi])):
        minCost = min(erg,minCost)
        print(minCost)
      swap((x,1), pos2)
      
  #2. Leave room possible?
  for room in targetsI:
    if (pos1 :=can_leave_room(room, puzzle, targetsI)):
      for pos2 in get_possible_hallway_pos(*pos1, hallway, puzzle):
        swap(pos1,pos2)
        mapStr = get_mapStr(puzzle)
        if mapStr in seen:
          swap(pos1,pos2)
          continue
        seen.add(mapStr)
        dfs(puzzle, cost+distance(*pos1,*pos2)*energy[puzzle[pos2]])
        swap(pos1,pos2)
            

def solve(puzzle):
  dfs(puzzle,0)
  print(minCost)
  
  
      
    

start = pfc()
puzzle = read_puzzle('Tag_23.txt')
energy = dict(A=1, B=10, C=100, D=1000)
hallway = {1,2,4,6,8,10,11}
targets = {'A':3, 'B':5, 'C':7, 'D':9}
targetsI = {val:key for key,val in targets.items()}
minCost = 999999
print(solve(puzzle))
print(pfc()-start)
