def bgcd(a,b):
	if b == 0: ans = a 
	else:
		if a < b: ans = bgcd(b,a)
		else:
			pa = a%2 == 0
			pb = b%2 == 0
			if pa and pb: ans = 2*bgcd(a//2,b//2)
			elif not(pa) and pb: ans = bgcd(a,b//2)
			elif not(pb) and pa: ans = bgcd(a//2,b)
			elif not(pa) and not(pb): ans = bgcd((a-b)//2,b)

	return ans
