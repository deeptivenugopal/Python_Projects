'''
Given a class for a BasicPlan, write the classes for StandardPlan and PremiumPlan which have class attributes of the following:
https://edabit.com/challenge/5T978H873HFZ7xKd8
'''

class BasicPlan:
	can_stream = True
	can_download = True
	has_SD = True
	has_HD = False
	has_UHD = False
	num_of_devices = 1
	price = "$8.99"
	
class StandardPlan(BasicPlan):
	has_HD = True
	has_UHD = False
	num_of_devices = 2
	price = "$12.99"

class PremiumPlan(BasicPlan):
	has_HD = True
	has_UHD = True
	num_of_devices = 4
	price = "$15.99"