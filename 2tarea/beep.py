from sys import stdin
INF = float('inf')
def gen_comp_g(N,positions):
	graph =[[0 for _ in range(N)]for _ in range(N)]
	for i in range(N):
		for j in range(i+1,N):
			graph[i][j]=graph[j][i]= abs(positions[i][0]-positions[j][0])+abs(positions[i][1]-positions[j][1])
	return graph
def phi(u,S,mem):
	global graph
	"""assert 0 < u<N
	assert S.issubset(univ)
	assert not (0 in S)
	assert u in S"""
	key = (u,tuple(S)) #colaboracion con Juan David Arce
	if key in mem:
		ans = mem[key]
	else:
		ans = None
		if len(S) == 1: ans =graph[u][0]
		else:
			ans,Swu = INF, S.difference([u])
			for v in Swu:
				ans = min(ans,graph[u][v]+phi(v,Swu,mem))
		mem[key] = ans
	return ans
def solve(N):
	mem = dict()
	univ = set(i for i in range(1,N))
	ans = INF
	for u in univ:
		ans = min(ans,graph[0][u]+phi(u,univ,mem))

	print("The shortest path has length " + str(ans))
	return
def main():
	global graph
	cases = int(stdin.readline().strip())
	for _ in range(cases):
		line = stdin.readline().strip().split()
		sizex,sizey = int(line[0]),int(line[1])
		line = stdin.readline().strip().split()
		startx,starty = int(line[0]),int(line[1])
		bnum = int(stdin.readline().strip())
		positions = [None for _ in range(bnum+1)]
		positions[0]=(startx,starty)
		for i in range(bnum):
			line = stdin.readline().strip().split()
			posx,posy = int(line[0]),int(line[1])
			positions[i+1] = (posx,posy)
		graph = gen_comp_g(bnum+1,positions)
		#print(graph)
		solve(bnum+1)





	return
main()
