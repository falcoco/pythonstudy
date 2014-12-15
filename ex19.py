def func(a,b,c=0,*args,**kw):
	print 'a=',a,'b=',b,'c=',c,'agrs=',args,'kw=',kw
func(1,2)
func(1,2,c=3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)
args=(1,2,3,4)
kw={'x':99}
func(*args,**kw)