def fixed(A):
	N = len(A)
	ans= False
	if N!=0:
		low,hi=0,N
		while low +1 !=hi:
			mid = low+((hi-low)>>1)
			if mid<A[mid]:
				hi = mid
			else:
				low = mid
		ans = A[low]==low
	return ans,low
def main():
	A = [0,1,2,3,4,9,8,11,15,18,26]
	print(fixed(A))
	return
main()