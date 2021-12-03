import sys

with open(sys.argv[1]) as f:
	lines = f.readlines()

lines = [line.strip() for line in lines if line != '']

position = [0, 0]
aim = 0

for line in lines:
	cmd, amount = line.split(' ')
	amount = int(amount)

	if cmd == 'forward':
		position[0] += amount
		position[1] += aim * amount
	elif cmd == 'up':
		# position[1] -= amount
		aim -= amount
	elif cmd == 'down':
		# position[1] += amount
		aim += amount

print(position[0] * position[1])
