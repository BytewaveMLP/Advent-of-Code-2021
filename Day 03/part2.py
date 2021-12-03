import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
	lines = [line.strip() for line in f.readlines()]

input_str_len = len(lines[0])

def bit_criteria(lines):
	bit_counts = dict()
	for line in lines:
		for i, c in enumerate(line):
			bit_counts[i] = bit_counts.get(i, dict())
			bit_counts[i][c] = bit_counts[i].get(c, 0) + 1
	return bit_counts

bit_counts = bit_criteria(lines)
bit_counts2 = bit_counts

lines2 = lines.copy()

print(lines)

o2_rating = -1
co2_rating = -1

for i in range(input_str_len):
	max_bit = max(bit_counts[i].items(), key=lambda i: i[1])[0]
	min_bit = min(bit_counts2[i].items(), key=lambda i: i[1])[0]
	if bit_counts[i].get('0', 0) == bit_counts[i].get('1', 0):
		max_bit = '1'
	if bit_counts2[i].get('0', 0) == bit_counts2[i].get('1', 0):
		min_bit = '0'
	print(max_bit, min_bit)
	if o2_rating == -1:
		lines = [line for line in lines if line[i] == max_bit]
		bit_counts = bit_criteria(lines)
		print(bit_counts)
		if len(lines) == 1:
			o2_rating = int(lines[0], base=2)
			print('got o2 rating:', o2_rating)
	if co2_rating == -1:
		lines2 = [line for line in lines2 if line[i] == min_bit]
		bit_counts2 = bit_criteria(lines2)
		print(bit_counts2)
		if len(lines2) == 1:
			co2_rating = int(lines2[0], base=2)
			print('got co2 rating:', co2_rating)

	if o2_rating != -1 and co2_rating != -1:
		break

	print(lines, lines2)

print(lines, lines2)

print(o2_rating, co2_rating)

print(o2_rating * co2_rating)
