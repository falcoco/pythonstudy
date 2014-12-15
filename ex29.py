def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
	return sum
f = lazy_sum(1,3,5,7,9)
# print f
print f()
print lazy_sum.__name__