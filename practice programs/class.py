class Human:
	def __init__(self,name,height,weight):
		self.n=name
		self.h=height
		self.w=weight
	
	def walk(self):
		print(self.n+" can walk")
		
	def run(self):
		print(self.n+" can run")
		
		
kiran=Human("kiran",5.7,69)
kiran.run()
kiran.walk()
ram=Human("Ram",5.6,65)
ram.walk()
ram.run()
	