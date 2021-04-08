class Review:
	def __init__(self,doctorname,patientname):
		self.doctorname=doctorname
		self.patientname=patientname
		print("doctorname : "+doctorname)
		print("patientname : "+patientname)
		print("Enter your valuable review : ")
	def patientReview(self):
		x=input()
		print("Thanks for your valuable review")
		
r1=Review("rajesh","abhi")
r1.patientReview()