def binsearch(A,x):
	N = len(A)
	ans= False
	pos = None
	if N!=0:
		low,hi=0,N
		while low + 1!=hi:
			mid = low+((hi-low)>>1)
			print(low,hi)
			print(mid)
			if x<=A[mid]:
				hi = mid
			else:
				low = mid
			print(low,hi)
		if x == A[low]:
			ans = True
			pos = low
		elif x == A[hi]:
			ans = True
			pos = hi
		#ans = A[low]==x
	return ans,pos
arr =[1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,5,5,6,7]
print(binsearch(arr,2))

