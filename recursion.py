def permute(s):
	if len(s) <= 1:
		return [s]
	char=[0]
	perm=permute(s[1:])
	
	res=[]
	for perm in perms:
		for i in range(len(perm)+1):
			res.append(perm[:i] + char + perm[i:])
	return res

def base_convert(n,b):
	q = n%b
	if n%b ==0:
		return str(n)
	if b == 0:
		return str(n)
	return str(base_concvert(n//b,b)) + str(q)

