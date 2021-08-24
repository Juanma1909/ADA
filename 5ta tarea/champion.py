from sys import stdin
sieve = None
prime = None
divis = None
MAX = 1000001
def cal_sieve():
	global sieve,divis,prime,MAX
	sieve= [True for _ in range(MAX)]; sieve[0] =sieve[1] = False
	divis = [None for _ in range(MAX)]	
	prime = [2]; divis[1] = 1; divis[2] = 2

	for j in range(4,MAX,2):sieve[j],divis[j] = False,2		
	for i in range(3,MAX,2):
		if sieve[i]:
			prime.append(i)
			divis[i] = i			
			for j in range(i*i,MAX,i):sieve[j],divis[j] = False,i				
	return
def lowb(A,x): #colaboracion con juan david arce
	lo,hi = 0,len(A)
	while lo + 1 != hi:
		mid = lo+((hi-lo)>>1)
		if A[mid]<= x:
			lo = mid
		else:
			hi = mid
	return lo
def uppb(A,x): #colaboracion con juan david arce
	lo,hi = -1,len(A)
	while lo + 1 != hi:
		mid = lo+((hi-lo)>>1)
		if A[mid]>= x:
			hi = mid
		else:
			lo = mid
	return hi

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

def solve(l,u):
	global prime
	ans,posi= binsearch(prime,l)	
	ans,posf = binsearch(prime,u)
	if not(sieve[l]):
		ans,posi = binsearch(prime,l)
		posi+=1	
	champ = {}	
	isthere,rep,number = True,0,0	
	for i in range(posi,posf+1):
		if i == posi:ante = prime[i]
		elif (prime[i] - ante) not in champ: champ[prime[i] - ante] = 1
		else: champ[prime[i] - ante] +=1
		#print(str(ante) + " " + str(prime[i]))
		ante = prime[i]
	for c in champ:
		if champ[c] > rep: rep = champ[c];number = c
		elif champ[c] == rep and number != c: isthere = False
	if not isthere or number == 0 or l == u:print("No jumping champion")
	else:print("The jumping champion is {0}".format(number))
	return

def main():
	cases = int(stdin.readline().strip())
	cal_sieve()
	for _ in range(cases):
		line = stdin.readline().strip().split()
		l,u = int(line[0]),int(line[1])
		solve(l,u)
	return
main()