from sys import stdin
def solve(n,crop):
	#print(n)
	#print(crop)
	i = 0
	scare = 0
	while i < n:
		if crop[i] == '.':
			scare+=1
			i+=2
		i+=1
	return scare
def main():
	cases = int(stdin.readline().strip())
	for i in range(cases):
		n = int(stdin.readline().strip())
		crop =[str(x) for x in stdin.readline().strip()] 
		ans = solve(n,crop)
		print("Case " + str(i+1)+": " +str(ans) )
	return
main()