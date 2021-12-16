from time import perf_counter as pfc
import math


def read_puzzle(file):
  with open(file) as f:
    return list(bin(int(f.read().strip(), 16))[2:])


sum_versions = 0
bits2int     = lambda x: int(''.join(x), 2)
operations   = (sum, math.prod, min, max, None, lambda x: x[0] > x[1],
                lambda x: x[0] < x[1], lambda x: x[0] == x[1])

def parse(bits):
  global sum_versions
  version, bits = bits2int(bits[:3]), bits[3:]
  typeID, bits  = bits2int(bits[:3]), bits[3:]
  sum_versions += version

  if typeID == 4:
    groups = []
    while True:
      group, bits = bits[:5], bits[5:]
      groups += group[1:]
      if group[0] == '0': return bits2int(groups), bits

  lengthID = bits.pop(0)
  results = []
  if lengthID == '0':
    lenght, bits = bits2int(bits[:15]), bits[15:]
    subpacket, bits = bits[:lenght], bits[lenght:]
    while subpacket:
      result, subpacket = parse(subpacket)
      results.append(result)
  else:
    subpacketsCount, bits = bits2int(bits[:11]), bits[11:]
    for _ in range(subpacketsCount):
      result, bits = parse(bits)
      results.append(result)

  return operations[typeID](results), bits


def solve(puzzle):
  part2, _ = parse(puzzle)
  return sum_versions, part2


start = pfc()
print(solve(read_puzzle('Tag_16.txt')))
print(pfc()-start)