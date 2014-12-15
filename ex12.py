# -*- coding: utf-8 -*-
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('incorrect type')
		#对参数类型做检查，只允许整数和浮点数类型的参数
	if x >= 0:
		return x
	else:
		return -x
def _future(x):
	x=x+1
	return x
def _pass():
	pass
def _compare(x):
	if x > 10:
		pass
a=my_abs(10)#这里改变参数测试函数功能
b=my_abs(-2)
c=_future(9)
d=_pass()
e=_compare(11)
print a
print b
print c
print d
print e