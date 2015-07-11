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

	* pmt = each annuity payment in dollars, if problem is single cash flow based, 
	leave this empty
	'''
	original_args = [r, n, pv, pmt]
	# Convert all integers or floats into Decimal objects to maximize precision and
	# eliminate rounding off errors in between computations, placing the None values 
	# unchanged as they are back in the same position of the list
	dec_args = [Decimal(arg) if arg != None else arg for arg in original_args]

	# Carry out single cash flow FV calculation if no annuity was specified
	if dec_args[3] == None:
		# leave 100 as integer since Decimal objects cannot be divided by floats
		return (1 + (dec_args[0]/100))**dec_args[1] * dec_args[2]

	# Carry out annuity FV calculation if no single cash flow was specified
	elif dec_args[2] == None:
		annuity_length = range(1, dec_args[1]+1)
		# Apply compounding to each annuity payment made based on the number of 
		# years left till end 
		all_compounded_pmt = [(1 + (dec_args[0]/100))**(dec_args[1]-time_left) * dec_args[3] for time_left in annuity_length]
		return sum(all_compounded_pmt)

	# TODO: Make my function flexible to accept monthly interest rates too
		

def present_value(r, n, fv = None, pmt = None):
	'''
	Function to compute the Present Value based on interest rate and 
	a given future value. 

	Arguments accepted
	------------------
	* r = interest rate, which should be given in its original percentage, eg. 
	5% instead of 0.05

	* n = number of periods for which the cash flow, either as annuity or single
	flow from one present value

	* fv = future value in dollars, if problem is annuity based, leave this empty

	* pmt = each annuity payment in dollars, if problem is single cash flow based, 
	leave this empty
	'''
	original_args = [r, n, fv, pmt]
	dec_args = [Decimal(arg) if arg != None else arg for arg in original_args]
	
	if dec_args[3] == None:
		return dec_args[2]/((1 + (dec_args[0]/100))**dec_args[1])

	elif dec_args[2] == None:
		annuity_length = range(1, dec_args[1]+1)
		# Apply discounting to each annuity payment made according to number of years
		# left till end
		all_compounded_pmt = [dec_args[3] * (1/((1+dec_args[0]/100) ** time_left)) for time_left in annuity_length]
		return sum(all_compounded_pmt)


def payment(r, n, pv = None, fv = None):
	'''
	Function to compute value of each annuity payment based on given interest rate,
	number of periods (in years), present value and future values. 

	Arguments accepted
	------------------
	* r = interest rate, which should be given in its original percentage, eg. 
	5% instead of 0.05

	* n = number of periods for which the annuity cash flow should be paid
	
	* pv = present value in dollars

	* fv = future value in dollars
	
	** If either present or future values are 0 or unknown, just leave that 
	argument blank
	'''
	original_args = [r, n, pv, fv]
	dec_args = [Decimal(arg) if arg != None else arg for arg in original_args]

	# Case when pv is specified, but fv is not specified
	if dec_args[3] == None:
		annuity_length = range(1, dec_args[1]+1)
		discount_factor = [(1/((1+dec_args[0]/100) ** time_left)) for time_left in annuity_length]
		return dec_args[2] / sum(discount_factor)

	# Case when fv is specified but pv is not specified
	elif dec_args[2] == None:
		annuity_length = range(1, dec_args[1]+1)
		compound_factor = [(1 + dec_args[0]/100) ** (time_left - 1) for time_left in annuity_length]
		return dec_args[3] / sum(compound_factor)

'''
TODO: Consider abstracting the two functions into a base class for computing results with interest
'''