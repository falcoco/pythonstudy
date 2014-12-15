L = ['Hello', 'World', 18, 'Apple', None]
# for n in L:
# 	if (isinstance(n)==True):
# 	n = str(n)
print [s.lower() for s in L if isinstance(s,str) == True]