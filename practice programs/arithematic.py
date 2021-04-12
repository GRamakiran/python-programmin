def add(a,b):
	print(a+b)
	
def sub(a,b):
	print(a-b)
	
def mul(a,b):
	print(a*b)
	
def div(a,b):
	print(a/b)
	
def mod(a,b):
	print(a%b)
	
def factorial(a):
	if a==0 or a==1:
		return 1
	else:
		return a*factorial(a-1)

		