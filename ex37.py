
class Dog():
	def setname(self,name):
		self.__name = name
		self.name = name
class Cat():
	pass
dog = Dog();
#dog.__name("yhh")
dog.name("yyy")
print dog
print dog.name()
print dog.__name()


