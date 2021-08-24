def knap(B,W,n,m):
	if n == 0:
		ans = 0
	else:
		ans = knap(B,W,n-1,m)
		if W[n-1] <= m:
			ans = max(ans, B[n-1]+knap(B,W,n-1,m-W[n-1]))
	return ans

def knaptab(B,W,M):
	N = len(B)
	tab = [[None for _ in range(M+1)]for _ in range(N+1)]

	for m in range(M+1): tab[0][m] = 0

	n,m=1,0
	while n != N+1:
		if m == M+1:
			n,m= n+1,0
		else:
			tab[n][m]= tab[n-1][m]
			if W[n-1]<= m:
				tab[n][m] = max(tab[n][m],B[n-1]+tab[n-1][m-W[n-1]])
			m+=1
	return tab[N][M]
def knapvec(B,W,M):
	N = len(B)
	vec = [0 fopr _ in range(M+1)]
	n,m=1,M
	while n != N+1:
		if m == -1: n,m = n+1,M
		else:
			if W[n-1] <=m: vec[m] = max(vec[m],B[n-1]+vec[m-W[n-1]])
			m-=1
	return vec[M]

