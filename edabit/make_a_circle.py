'''
Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PI*r^2) and getPerimeter() (2*PI*r) which give both respective areas and perimeter (circumference).
https://edabit.com/challenge/nC7iHBbN8FEPy2EJ2
'''
from math import pi,ceil
class Circle:
	
	def __init__(self,radius):
		self.radius = radius
		
	def getArea(self):
		return ceil(pi * self.radius**2)
		
	def getPerimeter(self):
		return ceil(2 * pi * self.radius)
		
circy = Circle(11)
print(circy.getArea())

circy = Circle(4.44)
print(circy.getPerimeter())