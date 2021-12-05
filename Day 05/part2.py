import sys
import math
import functools
from collections import defaultdict

sign = functools.partial(math.copysign, 1)

with open(sys.argv[1]) as f:
	lines = [line.strip() for line in f.readlines() if line != '']

lines = [list(tuple(int(n) for n in point.split(',')) for point in line.split(' -> ')) for line in lines]

# print(lines)

grid = defaultdict(int)

n_overlaps = 0

for line in lines:
	x, y = line[0]
	final_x, final_y = line[1]

	slope_x = sign(final_x - x)
	if final_x == x:
		slope_x = 0
	slope_y = sign(final_y - y)
	if final_y == y:
		slope_y = 0

	print(x, y, final_x, final_y, slope_x, slope_y)

	while x != final_x + slope_x or y != final_y + slope_y:
		grid[(x, y)] += 1
		if grid[(x, y)] == 2:
			n_overlaps += 1
		x += slope_x
		y += slope_y

max_x = max(grid.keys(), key=lambda x: x[0])[0]
max_y = max(grid.keys(), key=lambda x: x[1])[1]

for y in range(max_y + 1):
	for x in range(max_x + 1):
		n = grid[(x, y)]
		print(n if n != 0 else '.', end='')
	print()

# print(grid)
print(n_overlaps)
