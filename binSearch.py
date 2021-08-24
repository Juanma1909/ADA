def binsearch(A,x):
	N = len(A)
	ans= False
	if N!=0:
		low,hi=0,N
		while low +1 !=hi:
			mid = low+((hi-low)>>1)
			if x<A[mid]:
				hi = mid
			else:
				low = mid
		ans = A[low]==x
	return ans,low
def sRight(A,x):
	N = len(A)
	lo,hi = 0,N
	while lo < hi:
		mid = (lo + hi)//2
		if x < A[mid]:
			hi = mid
		else:
			lo = mid + 1
	return lo
        
def sLeft(A,x):
	N = len(A)
	lo,hi = 0,N
	while lo < hi:
		mid = (lo + hi)//2
		if x > A[mid]:
			lo = mid + 1
		else:
			hi = mid
	return lo
def lowb(A,x):
	lo,hi = 0,len(A)
	while lo + 1 != hi:
		mid = lo+((hi-lo)>>1)
		if A[mid]<= x:
			lo = mid
		else:
			hi = mid
	return lo
def uppb(A,x):
	lo,hi = -1,len(A)
	while lo + 1 != hi:
		mid = lo+((hi-lo)>>1)
		if A[mid]>= x:
			hi = mid
		else:
			lo = mid
	return hi

