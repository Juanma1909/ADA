from sys import stdin
def encode(a):
	count = 1
	last = a[0]
	coded = []
	for i in range(1,len(a)):
		if a[i] != last:
			coded.append(count)
			last = a[i]
			count = 1
		else:
			count+=1
	coded.append(count)
	return coded
def pop(a,j):
	n = len(a)-1
	a = list(a)
	if j == 0:
		new = a[1:]
	elif j == n:
		new= a[:j]
	else:
		left = a[:j]
		right = a[j+1:]
		suma = left[len(left)-1]+right[0]
		new = left[:len(left)-1] + [suma] + right[1:]
	return new
def solve(coded):
	ans = False
	if len(coded) == 0:
		ans = True
	else:
		for i in range(len(coded)):
			if coded[i] > 1:
				ans = ans or solve(pop(coded,i))		
	return ans
def main():
	cases = int(stdin.readline().strip())
	for i in range(cases):
		a = stdin.readline().strip()		
		coded = encode(a)
		if solve(coded): print(1)
		else:print(0)
		#print(coded)
		#print(pop(coded,3))
	return
main()
