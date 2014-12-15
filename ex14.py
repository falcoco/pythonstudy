# -*- coding: utf-8 -*-
#def power(x):
#	return x*x
#a = int(raw_input('a integer'))
#print power(a)
def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
a = int(raw_input())
b = int(raw_input())
print power(a)
print power(b,3)     #含默认参数