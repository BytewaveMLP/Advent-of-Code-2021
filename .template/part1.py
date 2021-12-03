import sys

with open(sys.argv[1]) as f:
	lines = [line.strip() for line in f.readlines()]

