class demo:
	def __init__(self,name,company,age):
		self.n=name
		self.c=company
		self.a=age
		
	def display(self):
		print(self.n+" working in "+self.c+" from last "+str(self.a)+" years")
		
	
	
class demo1(demo):
	def __init__(self,name,company,age,city):
		super().__init__(name,company,age)
		self.city=city
	
	def display2(self):
	
		print(self.n+" working in "+self.c+" from last "+str(self.a)+" years in "+self.city)

		
		
d1=demo1('kiran','sonata',22,'bangalore')
print(d1.display())
print(d1.display2())