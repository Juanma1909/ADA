from sys import satdin
def knap(B,W,n,m):
	if n == 0:
		ans = 0
	else:
		ans = knap(B,W,n-1,m)
		if W[n-1] <= m:
			ans = max(ans, B[n-1]+knap(B,W,n-1,m-W[n-1]))
	return ans
def sack(B,A,n,m):
	if n ==0: ans = 0
	else:
		ans = sack(A,n-1,m)
		if m>0:
			ans = max(ans,B[n-1]+sack(B,A,n-1,m-A[n-1]))
	return ans

def main():

	return
main()