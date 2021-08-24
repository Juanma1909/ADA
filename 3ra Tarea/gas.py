from sys import stdin
def mini(S,l,h):
	low,n,ans = l,0,list()
	N = len(S)
	ok = S[0][0] <= 0
	while low < h and n != N and ok:
		best,n = n,n+1		
		while n != N and S[n][0] <= low and ok:
			ok = S[n][0] <= low
			if S[n][1] > S[best][1]:
				best = n
			n+=1
		ans.append(best)
		low = S[best][1]
	ok = ok and low >= h
	if ok == False:
		ans = list()
	return ans
def connect(S,L):
	l=0
	connections = True
	for x in S:
		if x[0] <= l:
			if x[1] > l:l = x[1]
		else: connections = False
	connections = connections and l>=L
	return connections
def main():
	line = stdin.readline().strip().split()
	L,G = int(line[0]),int(line[1])
	while L != 0 and G != 0:
		stations= []
		for _ in range(G):
			line = stdin.readline().strip().split()
			x,r = int(line[0]),int(line[1])
			stations.append((x-r,x+r))
		stations.sort(key=lambda x : x[0])
		#print(stations)
		if connect(stations,L):		
			psans = mini(stations,0,L)
			if len(psans) == 0: print(-1)
			else:print(str(G-len(psans)))
		else: print(-1)
		line = stdin.readline().strip().split()
		L,G = int(line[0]),int(line[1])
	return
main()
