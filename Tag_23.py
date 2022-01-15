from time import perf_counter as pfc
from itertools import product
from heapq import heappop, heappush


def read_puzzle(filename):
  with open(filename) as f:
    return ''.join(c for c in f.read() if c not in '#  \n')


def can_enter_room(a, b, amphi, puzzle, t):
  bestI = False
  for i in t:
    if puzzle[i] == '.': bestI = i
    elif puzzle[i] != amphi: return False
  if not blocked(a, b, puzzle): return bestI


def blocked(a, b, puzzle):
  step = 1 if a < b else -1
  for i in range(a+step, b+step, step):
    if puzzle[i] != '.': return True


def can_leave_room(room, puzzle, t):
  if all(puzzle[i] == room for i in t if puzzle[i] != '.'): return False
  for a in t:
    if puzzle[a] == '.': continue
    return a


def get_possible_hallway_pos(a, hallway, puzzle):
  for b in [i for i in hallway if puzzle[i] == '.']:
    if blocked(a,b,puzzle): continue
    yield b


def move(a, b, puzzle):
  p = list(puzzle)
  p[a], p[b] = p[b], p[a]
  return "".join(p)


def possible_moves(puzzle, hallway,stepout,target):
  for a in hallway:
    amphi = puzzle[a]
    if amphi == '.': continue
    if not (b := can_enter_room(a, stepout[amphi], amphi, puzzle, target[amphi])): continue
    yield a,b
  for room in "ABCD":
    if not (a := can_leave_room(room, puzzle, target[room])): continue
    for b in get_possible_hallway_pos(stepout[room],hallway,puzzle):
      yield a,b        


def solve(puzzle):
  energy = dict(A=1, B=10, C=100, D=1000)
  hallway = {0, 1, 3, 5, 7, 9, 10}
  stepout = dict(A=2, B=4, C=6, D=8)
  target = {room: list(range(11+i, len(puzzle), 4)) for i, room in enumerate(stepout)}
  targetI = {v: key for key, val in target.items() for v in val}
  
  queue, seen = [(0, puzzle)], {puzzle: 0}
  solution = '.'*11+'ABCD'*2 if len(puzzle) == 19 else '.'*11+'ABCD'*4
  while queue:
    cost, state = heappop(queue)
    if state == solution: return cost
    for a, b in possible_moves(state, hallway, stepout, target):
      a1,b1 = (a,b) if a < b else (b,a)
      distance = abs(stepout[targetI[b1]] - a1) + (b1-7)//4
      new_cost = cost + distance * energy[state[a]]
      moved = move(a, b, state)
      if seen.get(moved, 999999) <= new_cost: continue
      seen[moved] = new_cost
      heappush(queue, (new_cost, moved))


start = pfc()
print(solve(read_puzzle("Tag_23_a.txt")))
print(solve(read_puzzle("Tag_23_b.txt")))
print(pfc()-start)
