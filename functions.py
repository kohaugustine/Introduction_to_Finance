'''
This module serves to the implementation for all the math functions that will 
be used repeatedly throughout the introduction to finance course.

Date created is 22 Jun 2015.
'''
from decimal import Decimal, getcontext
getcontext().prec = 20	# Set the precision to very high order for maximal accuracy

def future_value(present_value, interest_rate, period_count):
	'''
	Function to compute the Future Value based on interest rate and 
	present value. 

	* interest_rate should be given in its original percentage, eg. 
	5% instead of 0.05
	'''
	# Convert all integers or floats into Decimal objects to maximize precision and
	# eliminate rounding off errors in between computations
	pv, ir, pc = Decimal(present_value), Decimal(interest_rate), Decimal(period_count)
	# leave 100 as integer since Decimal objects cannot be divided by floats
	return (1 + (ir/100))**pc * pv

def present_value(future_value, interest_rate, period_count):
	'''
	Function to compute the Present Value based on interest rate and 
	a given future value. 

	* interest_rate should be given in its original percentage, eg. 
	5% instead of 0.05
	'''
	fv, ir, pc = Decimal(future_value), Decimal(interest_rate), Decimal(period_count)
	return fv/((1 + (ir/100))**pc)