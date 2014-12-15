'a test demo'
__anthor__ = 'yhh'

import sys

def test():
	args = sys.argv
	if len(args)==1:
		print 'HelloWorld'
	elif len(args)==2:
		print 'Hello, %s!' % args[1]
	else:
		print 'Too Many arguments!'
if __name__=='__main__':
	test()
	print 'test'