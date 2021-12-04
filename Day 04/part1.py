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
		print(' '.join(str(n) for n in row))
	print()

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

for draw in drawing:
	print(draw)
	for board in boards:
		for row in board:
			for i, n in enumerate(row):
				if n == draw:
					row[i] = MARK_CH
		if is_bingo_winner(board):
			unmarked_nums_sum = sum(sum(n for n in row if n != MARK_CH) for row in board)
			print(unmarked_nums_sum)
			print(draw)
			print(unmarked_nums_sum * draw)
			exit(0)

