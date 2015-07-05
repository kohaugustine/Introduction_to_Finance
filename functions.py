'''
This module serves to the implementation for all the math functions that will 
be used repeatedly throughout the introduction to finance course.

Date created is 22 Jun 2015.
'''
from decimal import Decimal, getcontext
getcontext().prec = 20	# Set the precision to very high order for maximal accuracy

def future_value(r, n, pv = None, pmt = None):
	'''
	Function to compute the Future Value based on interest rate and 
	present value. 

	Arguments accepted
	------------------
	* r = interest rate, which should be given in its original percentage, eg. 
	5% instead of 0.05

	* n = number of periods for which the cash flow, either as annuity or single
	flow from one present value

	* pv = present value in dollars, if problem is annuity based, leave this empty

	* pmt = each annuity payment in dollars, if problem is present value based, 
	leave this empty
	'''
	original_args = [r, n, pv, pmt]
	# Convert all integers or floats into Decimal objects to maximize precision and
	# eliminate rounding off errors in between computations, placing the None values 
	# unchanged as they are back in the same position of the list
	dec_args = [Decimal(arg) if arg != None else arg for arg in original_args]

	if dec_args[3] == None:
		# leave 100 as integer since Decimal objects cannot be divided by floats
		return (1 + (dec_args[0]/100))**dec_args[1] * dec_args[2]
	elif dec_args[2] == None:
		annuity_length = range(1, dec_args[1]+1)
		# Apply compounding to each annuity payment made based on the number of 
		# years left till end 
		all_compounded_annuity = [(1 + (dec_args[0]/100))**(dec_args[1]-time_left) * dec_args[3] for time_left in annuity_length]
		return sum(all_compounded_annuity)

		

def present_value(future_value, interest_rate, period_count):
	'''
	Function to compute the Present Value based on interest rate and 
	a given future value. 

	* interest_rate should be given in its original percentage, eg. 
	5% instead of 0.05
	'''
	fv, ir, pc = Decimal(future_value), Decimal(interest_rate), Decimal(period_count)
	return fv/((1 + (ir/100))**pc)

'''
TODO: Consider abstracting the two functions into a base class for computing results with interest
'''