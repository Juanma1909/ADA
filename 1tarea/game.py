from sys import stdin
def solve(Arr):
	n = len(Arr)
	maxsum = 0
	current = 0
	for i in range(n):
		current+=Arr[i]
		if current>maxsum:
			maxsum= current
		elif current < 0:
			current = 0
	return maxsum
def main():
	inp = stdin
	for line in inp.readlines():
		num = [int(x) for x in line.strip().split()]
		print(solve(num))
main()

