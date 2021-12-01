import sys

with open(sys.argv[1]) as f:
	lines = f.readlines()

lines = [int(line.strip()) for line in lines if line != '']

inc = 0

for i in range(len(lines) - 1):
	if lines[i+1] - lines[i] > 0:
		inc += 1

print(inc)
