from definingUserException import *
class Doctor:
	def __init__(self,doctorid,password,firstname,lastname,dob,street,city,state,country,pin):
		self.doctorid = doctorid
		self.password=password
		self.firstname=firstname
		self.lastname=lastname
		self.dob=dob
		self.street=street
		self.city=city
		self.state=state
		self.country=country
		self.pin=pin
	
	def verifyDoctor(self,doctorid,password):
		if(doctorid==self.doctorid and password==self.password):
			print("Successfully login")
		else:
			raise(definingUserException("not a valid User"))

	
doctor1=Doctor("raj@gmail.com",1234,"abhi","ram","11-11-2001","hk street","hyderabad","telangana","India",526262)
doctor1.verifyDoctor("raj@gmail.com",12)

try:
	output=p1.verifyUser("ram@gmail.com",11)
	print(output)
except:
	print("Invalid")