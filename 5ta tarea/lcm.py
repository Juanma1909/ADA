from sys import stdin
from math import sqrt
def gcd(a,b):
	if b == 0:ans = a
	else:ans = gcd(b,a%b)
	return ans
def lcm(a,b):
	return (a//gcd(a,b))*b 
def solve(n):
	root = int(sqrt(n))
	divisor = []
	count = 0
	for i in range(1,root+1):
		if n%i == 0:
			divisor.append(i)
			if i*i != n:divisor.append(n//i)
	ld = len(divisor)
	for i in range(ld):
		for j in range(i,ld):
			a,b = divisor[i],divisor[j]
			if lcm(a,b) == n: count+=1
	print(str(n) + " " + str(count))
	return

def main():
	n = int(stdin.readline().strip())
	while n != 0:
		solve(n)
		n = int(stdin.readline().strip())

	return
main()
