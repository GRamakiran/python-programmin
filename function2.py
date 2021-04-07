name=input("enter a name  ")
age=int(input("enter your age  "))
def fun(name):
	years=100-age
	return years
years=fun(age)
print("name is "+name)
print("you will become 100years old after "+str(years))