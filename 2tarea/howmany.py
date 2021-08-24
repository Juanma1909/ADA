from sys import stdin
import sys
sys.setrecursionlimit(10000)
def phi(x,y,r,d,n,k,mem):
	key = (x,y,r,d)
	#print(key)
	#print(n)	
	if key in mem:
		ans = mem[key]
	else:
		if x == 2*n and y == 0 and r == 0 and d == False:
			ans = 1			
		elif x != 2*n and y == 0:
			ans = phi(x+1,y+1,r,True,n,k,mem)
		elif (x != 2*n and y!=0) and (d == False or (d == True and y!=k)):
			ans = phi(x+1,y+1,r,True,n,k,mem) + phi(x+1,y-1,r,False,n,k,mem)
		elif x != 2*n and y!=0 and d ==True and y ==k and r ==0:
			ans = phi(x+1,y+1,r,True,n,k,mem)
		elif x != 2*n and y != 0 and d == True and y == k and r != 0:
			ans = phi(x+1,y+1,r,True,n,k,mem) + phi(x+1,y-1,r-1,False,n,k,mem)
		else: ans = 0
		mem[key] = ans

	return ans

def solve(n,r,k):
	mem = dict()		
	d = None
	x = 0
	y = 0
	ans = phi(x,y,r,d,n,k,mem)
	print(ans)
	return
def main():	
	line = sys.stdin.readline().strip().split()
	while len(line) > 0:
		n,r,k = int(line[0]),int(line[1]),int(line[2])
		solve(n,r,k)
		line = sys.stdin.readline().strip().split()
	return
main()
