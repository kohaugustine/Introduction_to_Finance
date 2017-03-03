'''
This module serves to the implementation for all the math functions that will 
be used repeatedly throughout the introduction to finance course.

Date created is 22 Jun 2015.
'''
from decimal import Decimal as D
from decimal import getcontext
getcontext().prec = 20  # Set the precision to very high order for maximal accuracy
# All functions here will internally convert all integers or floats into Decimal 
# objects before performing any arithmetic to maximize precision and minimize
# rounding off errors. 

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
    # Carry out single cash flow FV calculation if no annuity was specified
    if pmt == None:
        # leave 100 as integer since Decimal objects cannot be divided by floats
        return (D(1) + (D(r)/D(100))) ** D(n) * D(pv)

    # Carry out annuity FV calculation if no single cash flow was specified
    elif pv == None:
        annuity_length = range(1, n+1)
        # Apply compounding to each annuity payment made based on the number of 
        # years left till end 
        all_compounded_pmt = [(D(1) + (D(r)/D(100))) ** D(n-time_left) * D(pmt) for time_left in annuity_length]
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
    if pmt == None:
        return D(fv) / ((1 + (D(r) / D(100))) ** D(n))

    elif fv == None:
        annuity_length = range(1, n+1)
        # Apply discounting to each annuity payment made according to number of years
        # left till end
        all_compounded_pmt = [D(pmt) * (D(1) / ((D(1) + D(r)/D(100)) ** D(time_left))) for time_left in annuity_length]
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

    # Case when pv is specified, but fv is not specified
    if fv == None:
        annuity_length = range(1, n+1)
        discount_factor = [(D(1) / ((D(1) + D(r)/D(100)) ** D(time_left))) for time_left in annuity_length]
        return D(pv) / sum(discount_factor)

    # Case when fv is specified but pv is not specified
    elif pv == None:
        annuity_length = range(1, n+1)
        compound_factor = [(D(1) + D(r)/D(100)) ** D(time_left - 1) for time_left in annuity_length]
        return D(fv) / sum(compound_factor)

def effective_annual_rate(qr, m):
    '''
    Function to compute the effective annual rate (EAR) based on a stated 
    interest rate. Returns the EAR value in percentage form, ie. 5% instead of 
    0.05.

    Arguments accepted
    ------------------
    * qr = stated (also known as quoted) interest rate which should be given in its original percentage, eg. 
    5% instead of 0.05
    * m = total number of times within a year that the stated/quoted interest 
    rate gets compounded
    '''
    return ((D(1) + (D(qr) / D(100)) / D(m)) ** D(m) - D(1)) * D(100)

'''
TODO: Consider abstracting the two functions into a base class for computing results with interest
'''
