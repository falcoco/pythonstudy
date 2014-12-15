'''
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print calc([1,2,3])
print calc((1,3,5,7))
#print calc(1,2,3,4)  #error
'''

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print calc(1,2,3)
print calc(1,3,5,7)
print calc(*[1,2,3])  #frequently used
#name = [1,2,3]
#print clac(*name)
#also worked