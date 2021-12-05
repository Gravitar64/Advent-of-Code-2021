from time import perf_counter as pfc

class Board():
  def __init__(self, board):
    self.board = board
    self.row_cols = self.gen_rc()
    self.all_numbers = self.gen_an()

  def gen_rc(self):
    rc = [{int(n) for n in row} for row in self.board]
    return rc + [{int(n) for n in col} for col in zip(*self.board)]

  def gen_an(self):
    return {int(n) for row in self.board for n in row}

  def check_Bingo(self, draw_numbers, draw_number):
    for s in self.row_cols:
      if not s.issubset(draw_numbers): continue
      return sum(self.all_numbers - draw_numbers) * draw_number


def read_puzzle(file):
  with open(file) as f:
    numbers, *boards = f.read().split('\n\n')
    numbers = [int(n) for n in numbers.split(',')]
    boards =  [Board([row.split() for row in board.split('\n')]) for board in boards]
    return numbers, boards


def solve(numbers, boards):
  draw_numbers, results = set(), []
  for draw_number in numbers:
    draw_numbers.add(draw_number)
    for board in boards:
      if (bingo := board.check_Bingo(draw_numbers, draw_number)):
        results.append(bingo)
        del boards[boards.index(board)]
  return results[0], results[-1]

start = pfc()
print(solve(*read_puzzle('Tag_04.txt')))
print(pfc()-start)