class Student:
	num = 2020000
	def __init__(self, name):
		self.name = name
		Student.num  += 1
		self.rollNumber = 'imt' + str(Student.num)


