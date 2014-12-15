import collections.iterable
d = {'a':1,'b':2,'c':3}
for key in d:			#default:key
	print key
for value in d:			#default:key
	print value
for value in d.itervalues(): #set variable value as values  
	print value
for k,v in d.iteritems():	#diedai(zh_cn)at the same time
	print k,v
for ch in 'ABCDEFG':		#can also be used for string
	print ch
#code in console
#>>> from collections import Iterable
# >>> isinstance('abc', Iterable) # str是否可迭代
# True
# >>> isinstance([1,2,3], Iterable) # list是否可迭代
# True
# >>> isinstance(123, Iterable) # 整数是否可迭代
# False