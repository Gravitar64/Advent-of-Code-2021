from time import perf_counter as pfc
import math

class Transmission:
  def __init__(self, bits):
    self.bits = bits
    self.pc = 0
    self.sumVersions = 0

  def get(self,n):
    val = int(self.bits[self.pc:self.pc+n],2)
    self.pc += n
    return val  


def read_puzzle(file):
  with open(file) as f:
    hexString = f.read().strip()
    return bin(int(hexString, 16))[2:].zfill(len(hexString)*4)

operations   = (sum, math.prod, min, max, None, lambda x: x[0] > x[1],
                lambda x: x[0] < x[1], lambda x: x[0] == x[1])

def parse(bits):
  bits.sumVersions += bits.get(3)
  typeID  = bits.get(3)

  if typeID == 4:
    result = 0
    while True:
      cont = bits.get(1)
      result = result * 16 + bits.get(4)
      if not cont: return result
  
  results = []
  if bits.get(1):
    for _ in range(bits.get(11)):
      results.append(parse(bits))
  else:  
    lenght = bits.get(15)
    end = bits.pc + lenght
    while bits.pc < end:
      results.append(parse(bits))
  
  return operations[typeID](results)


def solve(puzzle):
  transmission = Transmission(puzzle)
  part2 = parse(transmission)
  return transmission.sumVersions, part2


start = pfc()
print(solve(read_puzzle('Tag_16.txt')))
print(pfc()-start)