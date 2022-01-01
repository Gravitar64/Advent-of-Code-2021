from time import perf_counter as pfc
from itertools import product


def read_puzzle(filename):
    with open(filename) as f:
        return [row.split() for row in f.read().split("\n")]


def get_relevant_adds(puzzle):
    div1, div26 = [], []
    for i in range(0,len(puzzle),18):
        if puzzle[i+4][2] == '1':
            div1.append(int(puzzle[i+15][2]))
            div26.append(None)
        else:
            div1.append(None)
            div26.append(int(puzzle[i+5][2]))
    return div1, div26                           


def find_modellNo(digits,div1, div26):
    z = digits_idx = 0
    modellNo = [0]*14
    for i in range(14):
        d1, d26 = div1[i], div26[i]
        if d1 != None:
            z = z*26 +digits[digits_idx]+d1
            modellNo[i] = digits[digits_idx]
            digits_idx +=1
        else:
            w = z%26+d26
            if not (0 < w < 10): return False
            modellNo[i]=w
            z//=26
    return modellNo            


def solve(puzzle, part1=True):
    div1, div26 = get_relevant_adds(puzzle)
    
    number_Space = product(range(9,0,-1),repeat=7) if part1 else \
                   product(range(1,10),repeat=7) 
    
    for digits in number_Space:
        if (res := find_modellNo(digits,div1,div26)):
            return(''.join([str(i) for i in res]))


start = pfc()
print(solve(read_puzzle("Tag_24.txt")))
print(solve(read_puzzle("Tag_24.txt"),False))
print(pfc() - start)