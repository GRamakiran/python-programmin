class Patient:
	def __init__(self,userid,password,firstname,lastname,dob,street,city,state,country,pin):
		self.userid = userid
		self.password=password
		self.firstname=firstname
		self.lastname=lastname
		self.dob=dob
		self.street=street
		self.city=city
		self.state=state
		self.country=country
		self.pin=pin
		
	def verifyPatient(self,userid,password):
		if(userid==self.userid and password==self.password):
			print("Successfully login")
		else:
			print("Invalid id or password")
	
patient1=Patient("raj@gmail.com",1234,"abhi","ram","11-11-2001","hk street","hyderabad","telangana","India",526262)
u.verifyPatient("raj@gmail.com",1234)