'''
Simple OOP Calculator
Create methods for the Calculator class that can do the following:

Add two numbers.
Subtract two numbers.
Multiply two numbers.
Divide two numbers.

https://edabit.com/challenge/ta8GBizBNbRGo5iC6
'''

class Calculator:
	
	def add(self,a,b):
		return a + b
		
	def subtract(self,a,b):
		return a - b
	
	def multiply(self,a,b):
		return a * b
		
	def divide(self,a,b):
		return a // b
		
calculator = Calculator()

print(calculator.add(10, 5))

print(calculator.subtract(10, 5))

print(calculator.multiply(10, 5))

print(calculator.divide(10, 5))