from sys import stdin
sieve = None
divis = None
MAX = 1000001
values = dict()
def cal_sieve():
	global sieve,divis,MAX
	sieve= [True for _ in range(MAX)]; sieve[0] =sieve[1] = False
	divis = [None for _ in range(MAX)]	
	divis[1] = 1
	divis[2] = 2

	for j in range(4,MAX,2):sieve[j],divis[j] = False,2		
	for i in range(3,MAX,2):
		if sieve[i]:			
			divis[i] = i			
			for j in range(i*i,MAX,i):sieve[j],divis[j] = False,i				
	return
def compuestos(n):
	global divis	
	total = 0
	while n != 1:
		d,count = divis[n],0
		while n%d == 0:n,count= n //d, count+1		
		total+=count

	return total
def cal_values():
	global values
	values[1] = 0
	for i in range(2,MAX):
		values[i] = values[i-1] + compuestos(i)
	return
def solve(n):
	global values
	ans = 0
	for i in range(2,n+1):
		ans += values[i]
	print(ans)
	return
	 
def main():
	global values
	n = stdin.readline().strip()
	cal_sieve()
	cal_values()
	while n != "":
		n = int(n)
		print(values[n])
		n = stdin.readline().strip()
	return
main()
