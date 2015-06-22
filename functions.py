'''
This module serves to the implementation for all the math functions that will 
be used repeatedly throughout the introduction to finance course.

Date created is 22 Jun 2015.
'''

def future_value(present_value, interest_rate, period_count):
	'''
	Function to compute the Future Value based on interest rate and 
	present value. 

	* interest_rate should be given in its original percentage, eg. 
	5% instead of 0.05
	'''
	# We must add the decimal to 100.0 to ensure that we do not round to
	# integer
	return (1 + (interest_rate/100.0))**period_count * present_value

