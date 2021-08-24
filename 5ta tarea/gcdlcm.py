from sys import stdin
def solve(a,b):
	if b%a == 0:print(str(a) + " " + str(b)) 
	else:print(-1) 
	return
def main():
	cases = int(stdin.readline().strip())
	for _ in range(cases):
		line = stdin.readline().strip().split()
		a,b = int(line[0]),int(line[1])
		solve(a,b)
	return
main()
