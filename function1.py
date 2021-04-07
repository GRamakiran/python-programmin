x=int(input("enter a value  "))
y=int(input("enter a value  "))
z=int(input("enter a value  "))
def max(a,b,c):
	if(a>b and a>c):
		return a
	elif(b>a and b>c):
		return b
	else:
		return c
result=max(x,y,z)
print("The highest value is "+str(result))