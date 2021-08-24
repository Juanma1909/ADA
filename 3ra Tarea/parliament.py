from sys import stdin
def acumf(N):
	acum = []
	acum.append(2)
	for i in range(3,N):
		acum.append(i+acum[i-3])
	return acum
def solve(n,acum):
	#print(acum)
	i = 0 
	while acum[i] < n:
		i+=1
	#print(i)
	if acum[i] == n:
		#print("soy igual")
		ans = [j for j in range(2,i+3)]
		#print(ans)
	elif acum[i] > n:
		dif = acum[i] -n
		if dif != 1:
			#print("mas de 1")
			ans =[j for j in range(2,i+3)]
			del ans[dif-2]
		else:
			dif = acum[i+1] - n
			ans =[j for j in range(2,i+4)]
			del ans[len(ans)-2]
			del ans[0]
	print(' '.join(map(str,ans)))
	return ans


def main():
	acum = []
	acum = acumf(10000)
	cases = int(stdin.readline().strip())
	blank= stdin.readline()
	for i in range(cases):
		n = int(stdin.readline().strip())
		blank= stdin.readline()
		if n == 1: print(1)
		else:
			solve(n,acum)
			print()
	return
main()
