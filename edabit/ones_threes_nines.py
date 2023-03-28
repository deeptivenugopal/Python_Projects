'''
Ones, Threes and Nines (Version #1)
Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class. You will make variables (self.ones, self.threes, self.nines) to do this.

https://edabit.com/challenge/X6xZ2EaqqQbGF7Bwv
'''

class ones_threes_nines:
	
	def __init__(self,num):
		self.ones = num // 1
		self.threes = num // 3
		self.nines = num // 9
		
n1 = ones_threes_nines(5)
print(n1.nines)

print(n1.ones)

print(n1.threes)