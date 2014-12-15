#Version:1.0
'''
def add_end(L=[]):
	L.append('END')
	return L
print add_end([1,2,3])
print add_end()
print add_end()
'''

#Version:2.0
def add_end(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L
print add_end()
print add_end([1,2,3,4,5,6,7,88])
print add_end()
print add_end()