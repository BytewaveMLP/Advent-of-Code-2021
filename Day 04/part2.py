import sys
from typing import List

MARK_CH = 'X'

with open(sys.argv[1]) as f:
	lines = [line.strip() for line in f.readlines()]

def is_bingo_winner(board: List[List[int]]):
	for row in board:
		if row[0] == row[1] == row[2] == row[3] == row[4] == MARK_CH:
			return True
	for col in range(5):
		if board[0][col] == board[1][col] == board[2][col] == board[3][col] == board[4][col] == MARK_CH:
			return True
	return False

def print_board(board: List[List[int]]):
	for row in board:
		print(''.join(f'{n:>4}' for n in row))
	print()

def score_board(board: List[List[int]]):
	return sum(sum(n for n in row if n != MARK_CH) for row in board)

drawing = [int(n) for n in lines[0].split(',')]

boards = []

current_board = []
for line in lines[2:]:
	if line == '':
		boards.append(current_board)
		current_board = []
	else:
		current_board.append([int(n) for n in line.split()])

boards.append(current_board)

for board in boards:
	print_board(board)

already_winners = []
winning_board = None
winning_draw = None

for draw in drawing:
	print(draw)
	for board in boards:
		if board in already_winners: continue
		for row in board:
			for i, n in enumerate(row):
				if n == draw:
					row[i] = MARK_CH
		print_board(board)
		if is_bingo_winner(board):
			unmarked_nums_sum = score_board(board)
			if board not in already_winners:
				print('BINGO!')
				print()
				winning_board = board
				already_winners.append(board)
				winning_draw = draw

print('LAST WINNER:')
print_board(winning_board)
print(score_board(winning_board) * winning_draw)
