from sys import stdin
def binom(n,k,mem):
	#print(n)
	#print(k)
	assert 0<=k<=n
	ans,key = None,(n,k)
	if key in mem:
		ans = mem[key]
	else:
		if k == 0 or k ==n: ans = 1
		else:
			if n < (k<<1): k = n-k
			ans =binom(n-1,k-1,mem) + binom(n-1,k,mem)
		mem[key] = ans
	return ans
def solve(n,t,p,mem):
	N = (t-(n*p))+(n-1)
	K = n-1
	if N >= K:
		ans = binom(N,K,mem)
	else:
		ans = 0
	print(ans)
	return
def main():
	cases = int(stdin.readline().strip())
	mem = dict()
	for i in range(cases):
		line = stdin.readline().strip().split()		
		n,t,p = int(line[0]),int(line[1]),int(line[2])
		solve(n,t,p,mem)
	return
main()
