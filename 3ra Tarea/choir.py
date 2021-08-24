from sys import stdin
from math import ceil
def solve(notes):
	ans = -1
	acum = 0
	for note in notes:
		acum+=note
	if acum % len(notes) == 0:
		acum = acum/len(notes)
		diff = 0
		for note in notes:
			diff += abs(acum-note)
		if diff%2 == 0:
			ans = int(diff/2)+1
	print(ans)
	return


def main():
	line = stdin.readline().strip()
	while len(line) != 0:
		notes = [int(x) for x in stdin.readline().strip().split()]
		solve(notes)
		line = stdin.readline().strip()
	return
main()
