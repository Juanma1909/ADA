from sys import stdin
sieve = None
divis = None
MAX = 10001
values = dict()
ans = dict()

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
	global divis,ans	
	while n != 1:
		d,count = divis[n],0
		while n%d == 0:n,count= n //d, count+1
		if d in ans:ans[d] += count
		else: ans[d] = count		
	return ans

def caux(n):
	global divis
	comp = dict()
	while n != 1:
		d,count = divis[n],0
		while n%d == 0:n,count= n //d, count+1
		comp[d] = count
	return comp

def cal_values():
	global values,ans
	values = dict()
	for i in range(2,MAX):
		values[i] = dict(compuestos(i))
	
	return

def solve(n,m):
	global values
	if n != 1:	
		total = 0
		can = True
		div = caux(m)
		maj = dict(values[n])
		while can:
			for v in div:
				if v in maj and (maj[v] - div[v]) >= 0 :
					maj[v] = maj[v] - div[v]
				else:
					can = False
			if can:
				total+=1
		if total != 0: print(total)
		else: print("Impossible to divide")
	else: print("Impossible to divide")	
	return



def main():
	cases = int(stdin.readline().strip())
	cal_sieve()
	cal_values()
	for i in range(cases):
		print("Case {0}:".format(i+1))
		line = stdin.readline().strip().split()
		m,n = int(line[0]),int(line[1])
		solve(n,m)
	return
main()
