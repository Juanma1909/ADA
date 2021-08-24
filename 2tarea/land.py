from sys import stdin
def solve(n,m,mat):	
	lo,hi = 0,0
	tree = 0

	while lo != m:
		hi = lo
		col = [0 for _ in range(n)]
		while hi != m:
			cont=0				
			for i in range(n):
				col[i] = mat[i][hi] or col[i]
			maxi = 0
			for i in range(n):
				if col[i] == 0: cont +=1
				else: cont = 0
				if cont > maxi: maxi = cont
			if maxi*((hi-lo)+1)>tree: tree = maxi*((hi-lo)+1)
			hi+=1
		lo+=1
	print(tree)
	return tree
		

def main():
	line = stdin.readline().strip().split()
	N,M= int(line[0]),int(line[1])
	while N != 0 or M != 0:
		mat = [[None for _ in range(M)]for _ in range(N)]		
		for i in range(N):
			line = stdin.readline().strip().split()
			for j in range(M):
				mat[i][j] = int(line[j])				
		solve(N,M,mat)
		line = stdin.readline().strip().split()
		N,M = int(line[0]),int(line[1])

	return
main()