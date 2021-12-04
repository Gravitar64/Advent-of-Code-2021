def read_puzzle(file):
  with open(file) as f:
    numbers, *boards = f.read().split('\n\n')
    numbers = numbers.split(',')
    boards = [[row.split() for row in board.split('\n')] for board in boards]
    return numbers, boards


def checkBingo(board, draw_numbers, draw_number):
  all_numbers = {n for zeile in board for n in zeile}
  row_cols = [{n for n in row} for row in board]
  row_cols += [{n for n in col} for col in zip(*board)]
  for s in row_cols:
    if not s.issubset(draw_numbers):
      continue
    return sum(int(n) for n in (all_numbers - draw_numbers)) * int(draw_number)


def solve(numbers, boards):
  draw_numbers, results = set(), []
  for draw_number in numbers:
    draw_numbers.add(draw_number)
    for i, board in enumerate(boards):
      if (bingo := checkBingo(board, draw_numbers, draw_number)):
        results.append(bingo)
        del boards[i]
  return results[0], results[-1]


print(solve(*read_puzzle('Tag_04.txt')))
