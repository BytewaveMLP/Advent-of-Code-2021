import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
	lines = f.readlines()

bit_counts = dict()

for line in lines:
	for i, c in enumerate(line.strip()):
		bit_counts[i] = bit_counts.get(i, dict())
		bit_counts[i][c] = bit_counts[i].get(c, 0) + 1

gamma = int(''.join(max(bit_counts[i], key=bit_counts[i].get) for i in range(len(line.strip()))), base=2)
print(gamma)
epsilon = int(''.join(min(bit_counts[i], key=bit_counts[i].get) for i in range(len(line.strip()))), base=2)
print(epsilon)

print(gamma * epsilon)
