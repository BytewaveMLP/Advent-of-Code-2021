import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
	lines = [line.strip() for line in f.readlines() if line != '']

lines = [list(tuple(int(n) for n in point.split(',')) for point in line.split(' -> ')) for line in lines]

print(lines)

grid = defaultdict(int)

n_overlaps = 0

for line in lines:
	if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
		# discard diagonal line
		print('discard', line)
		continue

	min_x = min(line[0][0], line[1][0])
	max_x = max(line[0][0], line[1][0])
	min_y = min(line[0][1], line[1][1])
	max_y = max(line[0][1], line[1][1])

	for x in range(min_x, max_x + 1):
		for y in range(min_y, max_y + 1):
			if grid[(x, y)] == 1:
				n_overlaps += 1
			grid[(x, y)] += 1

print(grid)
print(n_overlaps)
