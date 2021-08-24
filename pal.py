def pal(A,n,m):
	if m >=n:
		ans = 0
	elif m+1==n:
		ans = 1
	elif m+1< n:
		if A[m] != A[n-1]:
			ans = max(pal(A,m+1,n),pal(A,m,n-1))
		else:
			ans = 2+pal(A,m+1,n-1)