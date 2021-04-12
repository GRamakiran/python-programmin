from abc import ABC ,abstractmethod

class Bank(ABC):
	@abstractmethod
	def rateOfInterestHouse(self):
		None
	@abstractmethod
	def rateOfInterestCar(self):
		None
class Sbi(Bank):
	def rateOfInterestHouse(self):
		print("house rate of interest is 3.4%")
		
	def rateOfInterestCar(self):
		print("car rate of interest is 5%")
		
		
obj=Sbi()
obj.rateOfInterestCar()