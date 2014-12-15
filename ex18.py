def person(name, age, **kw):
	print 'name:',name, ',age:',age ,',other',kw
person('Michael',30)

person('Bob',35,city = 'Beijing')

person('Adam',45,gender = 'M',job = 'engineer')

'''
'''
kw = {'city':'Beijing','job':'Engineer'}
#person('Jack',24,city=kw['city'],job=kw['job'])
person('Jack',24,**kw)