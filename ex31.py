import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)	#add this sentence before the wrapped sentence
		def wrapped(*args, **kw):
			print '%s %s:'%(text, func.__name__)
			return func(*args,  **kw)
		return wrapped
	return decorator

@log('excute')
def now():
	print '2013-12-25'
print now()
print '-'*40
now = log('excute')('now')
print now.__name__

