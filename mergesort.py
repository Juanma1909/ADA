def merge(arr,lo,mid.hi):
	lenL = mid-lo + 1
	lenR = hi-mid
	leftP,righP=[],[]
	for i in range(n):
		leftP[i] = arr[lo+i]
	for i in range(n):
		righP[i] = arr[mid+1+i]
	i,j,k = 0,0,0

	while i < lenL and j < lenR:
		if leftP[i] < righP[j]:
			arr[k] = leftP[i]
			i+=1
		else:
			arr[k] = righP[j]
			j+=1
		k+=1
	while i < lenL:
		arr[k] = leftP[i]
		i+=1
		k+=1
	while j < lenR:
		arr[k] = leftP[j]
		j+=1
		k+=1


def mergesort(Arr,lo,hi):
	if lo +1 != hi:
		mid = lo+((hi-lo)>>1)
		mergesort(Arr,lo,mid)
		mergesort(Arr,mid+1,hi)
		merge(Arr,lo,mid,hi)


