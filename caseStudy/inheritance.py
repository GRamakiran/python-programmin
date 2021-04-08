from patient import *
			
class Doctor(Patient):
	def __init__(self,patientid,password,firstname,lastname,dob,street,city,state,country,pin,dep):
		super().__init__(patientid,password,firstname,lastname,dob,street,city,state,country,pin)
		self.dep=dep
		
	def verifyUser(self,patientid,password):
		print("this method is from doctor")
		if(patientid==self.patientid and password==self.password):
			print("Successfully login")
		else:
			print("Invalid id or password")

			

d1=Doctor(11111,1234,"abhi","ram","11-11-2001","hk street","hyderabad","telangana","India",526262,"cardiology")
d1.verifyUser(1111,1234)
p1=Patient(11111,1234,"abhi","ram","11-11-2001","hk street","hyderabad","telangana","India",526262)
d1=p1
d1.verifyUser(11111,1234)