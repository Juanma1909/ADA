from math import sqrt,floor
sieve = None
prime = None
divis = None
MAX = 1000001
def div(a,b):
	if a <b: ans = 0
	else: ans = 1 + div(a-b,b)
	return ans
def mod(a,b):
	if a < b: ans = a
	else: ans = mod(a-b,b)
	return ans
def era(N):
	tab = [True for _ in range(N)]
	limit = floor(sqrt(N))
	for i in range(2,limit):
		if tab[i]:
			j=i			
			while j + i <N:
				tab[j+i]=False
				j+=i
	ans = []
	for i in range(1,N):
		if tab[i]: ans.append(i)
	return ans
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
def compuestos(n):
	global divis
	ans = dict()
	while n != 1:
		d,count = divis[n],0
		while n%d == 0:n,count= n //d, count+1
		ans[d] = count

	return ans
def emcd(a,b):
	ans = None
	if b == 0:
		ans =(a,1,0)
	else:
		mcd,x1,y1=emcd(b,a%b)
		x = y1
		y = x1 - (a//b)*y1
		ans = (mcd,x,y)
	return ans

	
def main():
	print(compuestos(12))
	cal_sieve()	
	return
main


#print(era(100)) 
