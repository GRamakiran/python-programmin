class Patient:
	def __init__(self,patientid,password,firstname,lastname,dob,street,city,state,country,pin):
		self.patientid = patientid
		self.password=password
		self.firstname=firstname
		self.lastname=lastname
		self.dob=dob
		self.street=street
		self.city=city
		self.state=state
		self.country=country
		self.pin=pin
		
	def verifyUser(self,patientid,password):
		if(patientid==self.patientid and password==self.password):
			print("Successfully login")
		else:
			print("Invalid id or password")
	
patient1=Patient(11111,1234,"abhi","ram","11-11-2001","hk street","hyderabad","telangana","India",526262)
patient1.verifyUser(11111,1234)