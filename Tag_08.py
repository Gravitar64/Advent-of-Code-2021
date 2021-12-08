from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return [[x for x in row.split()] for row in f.readlines()]


def solve(puzzle):
  part1 = sum(len(n) in {2, 4, 3, 7} for row in puzzle for n in row[11:])
  
  part2 = 0
  segments = {*'abcdefg'}
  unique_segments = {2: {*'cf'}, 4: {*'bcdf'}, 3: {*'acf'},
                     7: {*'abcdefg'}, 5: {*'adg'}, 6: {*'abfg'}}
  zahlen = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3,
            'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7,
            'abcdefg': 8, 'abcdfg': 9}

  for row in puzzle:
    translate = {}
    wires = {a: {b for b in segments} for a in segments}
    
    for n in row[:10]:
      for seg in unique_segments[len(n)]:
        wires[seg] -= segments - {*n}
    
    changed = True
    while changed:
      changed = False
      for key, values in wires.items():
        if len(values) != 1: continue
        translate[values.pop()] = key
        changed = True
      for key in translate:
        for values in wires.values():
          if key not in values: continue
          values.remove(key)
    
    e = ''
    for n in row[11:]:
      decrypted = ''
      for z in n:
        decrypted += translate[z]
      decrypted = ''.join(sorted(z for z in decrypted))
      e += str(zahlen[decrypted])
    part2 += int(e)

  return part1, part2

start = pfc()
print(solve(read_puzzle('Tag_08.txt')))
print(pfc()-start)