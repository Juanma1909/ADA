from sys import stdin
mutations = 0
found = False
def facto():
	fact = []
	fact.append(1)
	for i in range(1,27):
		fact.append(i*fact[i-1])
	#print(fact)
	return fact
		
def mutate(per,p,x,n,fact):
	global mutations,found	
	if not(found):
		#print(p)
		#print(mutations)
		p = list(p)
		lenp = len(p)
		lenper = len(per)
		if lenp == lenper:
			mutations +=1
			#print(''.join(p))
			if mutations == x:
				found = True
				print(''.join(p))

		else:			
			for i in range(lenp+1):
				letter = per[n]
				add =fact[lenper]//fact[lenp+1]
				#print(add)
				if x > mutations + add:
					mutations = mutations + add
				else:
					mutate(per,p[:i]+[letter]+p[i:],x,n+1,fact)
	return p 



def main():
	global mutations,found
	cases = int(stdin.readline().strip())
	fact = facto()
	for _ in range(cases):
		mutations = 0
		found = False
		per = [str(x) for x in stdin.readline().strip()]
		search = int(stdin.readline().strip())
		fact = facto()
		mutate(per,[per[0]],search,1,fact)
	return
main()
