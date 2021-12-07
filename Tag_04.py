from time import perf_counter as pfc

def read_puzzle(file):
  with open(file) as f:
    numbers, *boards = f.read().split('\n\n')
    numbers = numbers.split(',')
    boards = [[row.split() for row in board.split('\n')] for board in boards]
    return numbers, boards


def checkBingo(board, draw_numbers, draw_number):
  row_cols = [{n for n in row} for row in board]
  row_cols += [{n for n in col} for col in zip(*board)]
  for s in row_cols:
    if s.issubset(draw_numbers):
      all_numbers = {n for row in board for n in row}
      return sum(int(n) for n in (all_numbers - draw_numbers)) * int(draw_number)


def solve(numbers, boards):
  draw_numbers, results = set(), []
  for draw_number in numbers:
    draw_numbers.add(draw_number)
    for board in boards:
      if (bingo := checkBingo(board, draw_numbers, draw_number)):
        results.append(bingo)
        del boards[boards.index(board)]
  return results[0], results[-1]


start=pfc()
print(solve(*read_puzzle('Tag_04.txt')))
print(pfc()-start)