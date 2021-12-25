from time import perf_counter as pfc
from collections import defaultdict

#Ideen
#1. kann ein amphipod aus der hallway in seinen Raum wechseln
#2. kann ein amphipod seinen raum in die hallway verlassen

def read_puzzle(filename):
  walls, amphipods,rooms = set(), defaultdict(list), defaultdict(list)
  with open(filename) as f:
    for y,row in enumerate(f.read().split('\n')):
      for x,c in enumerate(row):
        if c == '#': walls.add((x,y))
        if c in 'ABCD': 
          amphipods[c].append((x,y))
          rooms[x].append((c,y))

  return walls, amphipods, rooms

def get_free_hallway_pos(hallway):
  return {pos for pos,state in hallway.items() if state == ''}


def reachable(x1,y1,x2,y2,amphipods):
  if any((x1,ny) in amphipods.values() for ny in range(y1,y2+1)): return False
  if any((nx,y2) in amphipods.values() for nx in range(x1,x2+1)): return False
  return True

def target_reached(c,x,y):
  if y != targets[c]: return False
    
def room_solved(room,renter,targets):
  return all(room == targets[amphi] for amphi,_ in renter)


def leave_room(c,x1,y1):
  if not (points := get_free_hallway_pos()): return False
  return {(x2,y2) for x,y in hallway if reachable(x1,y1,x2,y2)}


def get_board_pos(amphipods):
  board_pos = ''
  for amphi,x,y in sorted(amphipods):
    board_pos += f'{amphi} {x} {y}'
  return board_pos

def distance(x1,y1,x2,y2):
  return abs(x2-x1)+abs(y2-y1)      

def solve(walls, amphipods, rooms):
  energy = dict(A=1, B=10, C=100, D=1000)
  hallway = {(1,1):'',(2,1):'',(4,1):'',(6,1):'',(8,1):'',(10,1):'',(11,1):''}
  targets = {'A':3, 'B':5, 'C':'7', 'D':9, '.' :None}
  cost = 0
  # enter target-room from hallway?
  for pos,amphi in hallway:
    if amphi == '': continue
  
  # leave room to hallway?
  for x, renter in rooms.items():
    if room_solved(x,renter,targets): continue
    for ri, (amphi, y) in enumerate(renter):
      if amphi == '.': continue
      if targets[amphi] == x and y==3: continue
      if y in {2,3}:
        for pos2 in get_free_hallway_pos(hallway):
          if not reachable(x,y,*pos2,amphipods): continue
          cost += distance(x,y,*pos2) * energy[amphi]
          rooms[x][ri] = ('.',y)
          hallway[pos2] = amphi
          amphi_poss = amphipods[amphi]
          ai = amphi_poss.index((x,y))
          amphipods[amphi][ai] = pos2
          print(rooms)
          print(hallway)
          print(amphipods)

   



start = pfc()
print(solve(*read_puzzle('Tag_23.txt')))
print(pfc()-start)
