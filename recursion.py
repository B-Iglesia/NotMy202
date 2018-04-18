def permute(s):
	if len(s) <= 1:
		return [s]
	char=s[0]
	perm=permute(s[1:])
	
	res=[]
	for perm in perms:
		for i in range(len(perm)+1):
			res.append(perm[:i] + char + perm[i:])
	return res

def l2d(n):
	a=str(n)
	b = a[-2]
	c = a[-1]
	return int(b)*int(c)
print(l2d(52))
def base_convert(n,b):
	q = n%b
	if n%b ==0:
		return str(n)
	if b == 0:
		return str(n)
	if b >10:
		if q == 10:
			return "A"
		if q == 11:
			return "B"
		if q ==12:
			return str(base_convert(n//b,b))+ "C"
		if q == 13:
			return "D"
		if q == 14:
			return "E"
		if q == 15:
			return "F"
	return str(base_convert(n//b,b)) + str(q)

print(base_convert(30,4))
print(base_convert(316,16))


def bear_share(n):
	if n<42:
		return False
	if n==42:
		return True
	else:
		if n%2==0:
			if bear_share(n//2)==False:
				if bear_share(n-42)==False:
					return bear_share(n-(int(str(n)[-1])*int(str(n)[-2])))
				return bear_share(n-42)
			return bear_share(n//2)
		if n%5==0:
			if bear_share(n-42)==False:
				return bear_share(n//2)
			return bear_share(n-42)
		if n%4==0 or n%3==0:
			if bear_share((int(str(n)[-1])*int(str(n)[-2])))==0:
				if bear_share(n-42)==False:
					return bear_share(n//2)
				return bear_share(n-42)
			return bear_share(n-(int(str(n)[-1])*int(str(n)[-2])))
		return False
print(bear_share(250))
print(bear_share(52))
print(bear_share(43))
print(bear_share(40))
print(bear_share(84))
