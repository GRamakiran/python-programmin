class Booking:
		def __init__(self,patientid,firstname,lastname):
			self.patientid = patientid
			self.firstname=firstname
			self.lastname=lastname
			
		def displayBookingDetails(self,bookingid,slotno,slotdate,slottime):
			self.bookingid=bookingid
			self.slotno=slotno
			self.slotdate=slotdate
			self.slottime=slottime
			print("Your booking is conformed for bookingid "+str(bookingid))
			print("your slot number is "+str(slotno)+" slotdate is "+str(slotdate)+" and slottime is "+str(slottime))
			print("Thanks for booking")
			
			
booking1=Booking("ram@gmil.com","abhi","ram",)
booking1.displayBookingDetails(1,1,"01-01-2022","12:30 pm")
		