import mysql.connector
mydb =mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="python")
	
mycursor=mydb.cursor()

class Patient:
	def __init__(self,firstname,lastname,dob,street,city,state,country,pin):
		
		self.firstname=firstname
		self.lastname=lastname
		self.dob=dob
		self.street=street
		self.city=city
		self.state=state
		self.country=country
		self.pin=pin
		
	def verifyUser(self,user,password):
		sql="select password from patient where userid=%s"
		val=[user]
		mycursor.execute(sql,val)
		result=mycursor.fetchone()
		if(result!=None):
			if(password==result[0]):
				return True
			else:
				return False
		else:
			return False
		
patient1=Patient("abhi","ram","11-11-2001","hk street","hyderabad","telangana","India",526262)
print(patient1.verifyUser(22,"abc"))