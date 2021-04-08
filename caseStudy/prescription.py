class Prescription:
	def __init__(self,pres_id,patientid,bookingid):
		self.pres_id=pres_id
		self.patientid=patientid
		self.bookingid=bookingid
		
	def presList(self,tablet,injection,saline):
		self.tablet=tablet
		self.injection=injection
		self.saline=saline
		print("tablet = "+tablet)
		print("injection = "+injection)
		print("saline = "+saline)
		
p1=Prescription(1,"rqm@gmail.com",1)
p1.presList("ibuprofen","aceteminophen","glucose saline")
	