class Circle:
	PI = 3.1415
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return Circle.PI * (self.radius ** 2)

	def circumference(self):
		return 2 * Circle.PI * self.radius

class Rectangle:
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth

	def area(self):
		return self.length * self.breadth

	def circumference(self):
		return 2 * (self.length + self.breadth)


		
