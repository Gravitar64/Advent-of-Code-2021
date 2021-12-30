from time import perf_counter as pfc
from heapq import heappush, heappop


def read_puzzle(filename):
    with open(filename) as f:
        return "".join(
            [c for row in f.read().split("\n") for c in row if c not in "# "]
        )


def room_solved(room, puzzle, targets):
    return all(puzzle[i] == room for i in targets[room])


def can_leave_room(room, puzzle, targets):
    if room_solved(room, puzzle, targets):
        return False
    for n, i in enumerate(targets[room]):
        if puzzle[i] != ".":
            if n == 0:
                return i
            elif puzzle[i] != room:
                return i


def can_enter_room(amphi, puzzle, targets):
    if room_solved(amphi, puzzle, targets):
        return False
    for i in targets[amphi]:
        if puzzle[i] == ".":
            bestI = i
        elif puzzle[i] != amphi:
            return False
    return bestI


def blocked(i1, i2, puzzle):
    step = 1 if i1 < i2 else -1
    return any(puzzle[v] != "." for v in range(i1 + step, i2 + step, step))


def get_possible_hallway_pos(i1, hallway, puzzle, stepout, targetsI):
    for i2 in hallway:
        if puzzle[i2] != ".":
            continue
        if blocked(stepout[targetsI[i1]], i2, puzzle):
            continue
        yield i2


def distance(i1, i2, stepout, targetsI):
    f, t = min(i1, i2), max(i1, i2)
    step = stepout[targetsI[t]]
    d = abs(step - f) + (t-)//4
    return d


def swap(i1, i2, puzzle):
    p = list(puzzle)
    p[i1], p[i2] = p[i2], p[i1]
    return "".join(p)


def possible_moves(puzzle):
    moves = []
    for i1 in hallway:
        if puzzle[i1] == ".":
            continue
        if not (i2 := can_enter_room(puzzle[i1], puzzle, targets)):
            continue
        if blocked(i1, stepout[puzzle[i1]], puzzle):
            continue
        moves.append((i1, i2, distance(i1, i2, stepout, targetsI)))
    for room in "ABCD":
        if not (i1 := can_leave_room(room, puzzle, targets)):
            continue
        for i2 in get_possible_hallway_pos(i1, hallway, puzzle, stepout, targetsI):
            moves.append((i1, i2, distance(i1, i2, stepout, targetsI)))
    return moves


def solve(puzzle,part1=True):
    queue, seen = [(0, puzzle)], {puzzle: 0}
    solution = "...........ABCDABCD" if part1 else "...........ABCDABCDABCDABCD"
    while queue:
        cost, state = heappop(queue)
        if state == solution:
            return cost
        for i1, i2, dist in possible_moves(state):
            new_cost = cost + dist * energy[state[i1]]
            moved = swap(i1, i2, state)
            if seen.get(moved, 999999) <= new_cost:
                continue
            #if i1 >22:
            #    print(f'{state}\n{moved} {i1}->{i2} {dist} {new_cost}\n')
            seen[moved] = new_cost
            heappush(queue, (new_cost, moved))


energy = dict(A=1, B=10, C=100, D=1000)
hallway = {0, 1, 3, 5, 7, 9, 10}
stepout = {"A": 2, "B": 4, "C": 6, "D": 8}
targets = {"A": [11,15,19,23], "B": [12,16,20,24], "C": [13,17,21,25], "D": [14, 18,22,26]}
targetsI = {v: key for key, val in targets.items() for v in val}


start = pfc()
#print(solve(read_puzzle("Tag_23_a.txt")))
print(solve(read_puzzle("Tag_23_b.txt"),False))
print(pfc() - start)
