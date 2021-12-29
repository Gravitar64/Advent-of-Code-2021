from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as f:
        return {(x, y): c for y, row in enumerate(f.read().split('\n')) for x, c in enumerate(row) if c not in '# '}


def room_solved(room, puzzle, targetsI):
    return all(puzzle[(room, y)] == targetsI[room] for y in range(1, 3))


def can_leave_room(room, puzzle, targetsI):
    if room_solved(room, puzzle, targetsI):
        return False
    if puzzle[(room, 2)] in 'ABCD':
        return (room, 2)
    if puzzle[(room, 3)] in 'ABCD' and puzzle[(room, 3)] != targetsI[room]:
        return (room, 3)


def can_enter_room(amphi, puzzle, targets):
    room = targets[amphi]
    if all(puzzle[(room, y)] == '.' for y in range(2, 4)):
        return room, 3
    if puzzle[(room, 3)] == amphi and puzzle[(room, 2)] == '.':
        return room, 2


def blocked(x1, x2, puzzle):
    step = 1 if x1 < x2 else -1
    return any(puzzle[v, 1] != '.' for v in range(x1+step, x2+step, step))


def get_possible_hallway_pos(x, _, hallway, puzzle):
    for x2 in hallway:
        if puzzle[(x2, 1)] != '.':
            continue
        if blocked(x, x2, puzzle):
            continue
        yield (x2, 1)


def distance(x1, y1, x2, y2):
    return abs(x2-x1)+abs(y2-y1)


def get_mapStr(puzzle):
    return ''.join(puzzle.values())


def swap(p1, p2, puzzle):
    puzzle[p2], puzzle[p1] = puzzle[p1], puzzle[p2]
    return puzzle


def possible_moves(puzzle):
    moves =[]
    for x in hallway:
        p1 = (x,1)
        amphi = puzzle[p1]
        if amphi == '.': continue
        if not (p2 := can_enter_room(amphi, puzzle, targets)): continue    
        if blocked(p1[0], p2[0], puzzle): continue
        moves.append((p1,p2,distance(*p1,*p2),amphi))
    for room in targetsI:
        if not (p1 := can_leave_room(room, puzzle, targetsI)): continue
        amphi = puzzle[p1]
        for p2 in get_possible_hallway_pos(*p1, hallway, puzzle):
            moves.append((p1,p2,distance(*p1,*p2),amphi))
    return moves

results = []
def dfs(cost,puzzle,path):
    global minCost
    state = get_mapStr(puzzle)
    if state == '...........ABCDABCD':
        return cost, path
    for p1,p2,dist,amphi in possible_moves(puzzle):
        moved = swap(p1,p2,puzzle.copy())
        state = get_mapStr(moved)
        new_cost = cost + dist * energy[amphi]
        if state in seen: continue
        if p2[1] == 1: seen.add(state)
        erg, p = dfs(new_cost, moved, path+[state])
        if erg and erg < minCost:
            minCost = erg
            results.append((minCost,p))
    return False, None



def solve(puzzle):
    dfs(0, puzzle, [get_mapStr(puzzle)])
    cost, path = sorted(results)[0]
    for move in path:
        print(move[:11])
        print(2*'#'+move[11]+'#'+move[12]+'#'+move[13]+'#'+move[14]+'#')
        print(2*'#'+move[15]+'#'+move[16]+'#'+move[17]+'#'+move[18]+'#')
        print()
    print(cost)

start = pfc()
puzzle = read_puzzle('Tag_23.txt')
save_state = get_mapStr(puzzle)
energy = dict(A=1, B=10, C=100, D=1000)
hallway = {1, 2, 4, 6, 8, 10, 11}
targets = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
targetsI = {val: key for key, val in targets.items()}
minCost, seen = 1<<32, set(get_mapStr(puzzle))

print(solve(puzzle))
print(pfc()-start)
