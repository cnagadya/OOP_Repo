""" Illustration of inheritance, encapsulation, polymorphism in OOP using a school scenario as a real world example"""
#----inheritance:sub class inheriting from super class
#students and staff inherit from school members 

#---encapsulation: privatising a function or variable to disable modification outside the class
#staff room is out of bounds for students

#----polymorphism: common methods but with unique actions per instance
#both staff and students have stay method but one stays in staff quarters and the other dormitories
class school_members(object):
	name = ""

	def __init__(self, name):
		self.name = name
	def have_school_access(self):
		print "Hello, welcome to school " + self.name
	



class staff(school_members):
	def _have_staffroom_access(self): #cant be accessed by any other school member other than staff
		print self.name + ", welcome to staffroom"
	def stay(self):
		print self.name + " stays in the staff quarters"


class student(school_members):
	def _no_staffroom_access(self):
		print self.name + ", you are not allowed in staffroom"

	def stay(self):
		print self.name + " stays in the dormitories" 



christine = school_members("Christine")
christine.have_school_access()

ritah = staff("Ritah")
ritah.have_school_access()
ritah._have_staffroom_access()
ritah.stay() #staff quarters because staff


nagadya = student("Nagadya") 
nagadya.have_school_access()
nagadya._no_staffroom_access()
nagadya.stay() #dormitory because student

#wont run because of encapsulation
nagadya._have_staffroom_access() #error, cant access function
ritah._no_staffroom_access()#error, cant access function


