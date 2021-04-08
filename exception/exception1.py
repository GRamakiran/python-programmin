i=int(input("Enter a value"))
try:
	print(10/i)
except ZeroDivisionError:
	print("do not devide with 0")
	
finally:
	print("completed")