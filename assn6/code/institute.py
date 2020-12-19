from student1 import * 

class Institute:
	def __init__(self, students = []):
		self.students = students

	def isStudentOf(self, s):
		if s in self.students:
			return True
		else:
			return False

	def isAddable(self, s):
		if s not in self.students:
			for student in self.students:
				if student.rollNumber == s.rollNumber:
					a = False
					break
				else:
					a = True
		else:
			a = False
		return a

	def addStudent(self, s):
		if Institute.isAddable(self, s) == True:
			self.students.append(s)
			return True
		else:
			return False






