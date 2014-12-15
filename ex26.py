g = (x * x for x in range(10))
print g.next()
print g.next()
print 'test'
for i in g:
	print i
	
#Fibonacci
def fib(max):
		n,a,b = 0,0,1
		while n < max :
			yield b
			a, b = b, a + b
			n = n + 1
print fib(6).next()

def odd():
	print 'step1'
	yield 1
	print 'step2'
	yield 2
	print 'step3'
	yield 3
	print 'step4'
	print 'end'
o = odd()
print o
o.next()
o.next()
o.next()
#o.next()
#o.next()
for n in fib(7):
	print n