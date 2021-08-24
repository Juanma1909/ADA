all_sols = None
def safe(a,n,r):
	ans,c = True,0
	while ans and c!= n:
		ans,c = a[c]!= r and n-c != r-a[c] and n-c != a[c]-r,c+1
	return ans
def nq(a,n):
	global all_sols
	assert 0<=n<=8
	if n == 8:all_sols.append(list(a))
	else:
		for r in range(8):
			if safe(a,n,r):
				a[n] = r
				nq(a,n+1)
	return