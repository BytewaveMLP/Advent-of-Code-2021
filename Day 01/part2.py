import sys

with open(sys.argv[1]) as f:
	lines = f.readlines()

lines = [int(line.strip()) for line in lines if line != '']

inc = 0

window = [0, 1, 2]

prev_sum = -1
inc = -1

while window[2] != len(lines):
	print(window)
	print([lines[i] for i in set(window)])
	window_sum = sum(lines[i] for i in set(window))
	print(window_sum)

	if window_sum > prev_sum:
		print(f'{window_sum} > {prev_sum}')
		inc += 1

	prev_sum = window_sum

	window[0] = window[1]
	window[1] = window[2]
	window[2] = window[2] + 1

print(inc)
