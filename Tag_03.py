from time import perf_counter as pfc

def read_puzzle(file):
  with open(file) as f:
    return [row.strip() for row in f]


def genCommon(bits):
  return '10' if bits.count('1') >= bits.count('0') else '01'


def solve(puzzle):
  #Part 1
  gamma = epsilon = ''
  for column in zip(*puzzle):
    mC, lC = genCommon(column)
    gamma += mC
    epsilon += lC

  #Part 2
  filtered_oxy, filtered_co2 = puzzle.copy(), puzzle.copy()
  for i in range(len(puzzle[0])):
    if filtered_oxy:
      mC, _ = genCommon(list(zip(*filtered_oxy))[i])
      filtered_oxy = [row for row in filtered_oxy if row[i] == mC]
      if len(filtered_oxy) == 1:
        oxygen = filtered_oxy.pop()
    
    if filtered_co2:
      _, lC = genCommon(list(zip(*filtered_co2))[i])
      filtered_co2 = [row for row in filtered_co2 if row[i] == lC]
      if len(filtered_co2) == 1:
        co2 = filtered_co2.pop()

  return int(gamma, 2) * int(epsilon, 2),  int(oxygen, 2) * int(co2, 2)


start=pfc()
print(solve(read_puzzle('Tag_03.txt')))
print(pfc()-start)
