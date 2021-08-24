from sys import stdin
from math import sqrt
def sch(a):  
  a.sort(key=lambda x : x[1])  # sort activities by earliest finish time
  ans,n,N = 0,0,len(a)
  while n!=N:
    best,n,ans = n,n+1,ans+1
    while n!=N and a[n][0]<a[best][1]:
      n += 1
  return ans

def main():
	line = stdin.readline().strip().split()
	n,d = int(line[0]),int(line[1])
	case = 1
	while n != 0 and d != 0:
		ans = 0
		rad=[]
		ok = True
		for i in range(n):
			line = stdin.readline().strip().split()
			x,y = int(line[0]),int(line[1])
			if d*d-y*y <0:ok = False
			else:
				cat = sqrt(d*d-y*y)
				rad.append((x-cat,x+cat))
		if ok != True:
			ans = -1
		else:
			ans = sch(rad)
		print("Case " +str(case)+": "+ str(ans))
		blank = stdin.readline()
		line = stdin.readline().strip().split()
		n,d = int(line[0]),int(line[1])
		case+=1



main()
