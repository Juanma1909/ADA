from sys import stdin
from collections import deque
def solve(q,x,n):
	#print("top: " +  str(q[0]))
	#print("x: " + str(x))
	ans = False
	q = deque(q)
	if n == 1:		
		if q[0] == x:ans = True
	else:
		for _ in range(n):
			t = q.popleft()			
			ans = ans or solve(q,x+t,n-1) or solve(q,x-t,n-1)
			if x % t == 0: ans = ans or solve(q,x//t,n-1)
			q.append(t)
	return ans

def main():
	line = [int(x) for x in stdin.readline().strip().split()]
	while line[0] != 0:
		q = deque(line)
		if solve(q,23,5): print("Possible")
		else: print("Impossible")
		line = [int(x) for x in stdin.readline().strip().split()]
	return
main()
