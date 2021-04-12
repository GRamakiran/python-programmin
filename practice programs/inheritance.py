class base:
	a=10
	b=20
	
	def display1(self):
		print("This is base class")
	
class derived1(base):
	c=11
	d=22
	
	def display(self):
		print("This is derived class 1\n")


		
		
b=base()
print(b.a)
print(b.display1())


d1=derived1()
print(d1.c)
print(d1.display())
print(d1.a)
print(d1.display1())