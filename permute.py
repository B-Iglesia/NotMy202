def permute(s):
	if len(s) <= 1:
		return [s]
	
	char=s[0]
	perms = permute(s[1:])
	
	res=[]
	
	for perm in perms:
	#because recursive call is in the middle, values are already generated for each string
	
		for i in range(len(perm)+1):
			res.append(perm[:i] + char + perm[i:])
	return res
print(permute("abc"))
print(permute("pie"))

def base_convert(n,b):
	q = n%b
	l = ['A', "B", "C","D",'E',"F"]
	if n%b == 0:
		return str(n)
	elif b == 0:
		return str(n)
	else:
		return str(base_convert(n//b,b)) + str(q)	
		
print(base_convert(30,4))
print(base_convert(316,16))
