# -*- coding: utf-8 -*-
import math

# Quiz 4 - Program 1
def trapezoid(a, b):
    ''' Calculate stuff
    '''
    f = lambda x: 3*(x**2)*math.exp(3*x)* math.cos(x)
    delta = float(b-a)/2
    res = delta * (f(a) + f(b))
    return res

def composite_trapezoid(a, b, m):
    f = f = lambda x: 3*(x**2)*math.exp(3*x)* math.cos(x)
    delta = float(b-a)/m
    res = 0.5*f(a) + 0.5*f(b)
    for i in range(1,m):
        res += f(a + i*delta)
    res *= delta
    return res
    
# Main Program
''' 
print(trapezoid(1,4))
a, b = input("Please enter interval a,b: ")
m = input("Number of intervals: ")
print(composite_trapezoid(a,b,m)) 
'''
# END Program 1

# Quiz 4 - Program 2

# Part 1
def payments(principal, annual_interest_rate, duration):
    
    annual_interest_rate /= 100.0
    n = duration
    if(annual_interest_rate != 0):
        r = pow(1+(annual_interest_rate/duration),duration)-1
        monthly_payment = principal * ((r*pow(1+r,n)) / (pow(1+r,n)-1))
    else:
        monthly_payment = principal/n
    
    return monthly_payment

# Part 2
def remaining_payments(principal, annual_interest_rate, duration, p):
    
    annual_interest_rate /= 100.0
    n = duration
    r = pow(1+(annual_interest_rate/duration),duration)-1
    remaining_loan_balance = principal * ( ( pow(1+r,n)- pow(1+r,p) ) / (pow(1+r,n)-1))
    return remaining_loan_balance

# Part 3
def loan(loan_amount, annual_interest_rate, total_duration, nr_payments):
    total = loan_amount
    interest_rate = annual_interest_rate
    duration = total_duration*12
    monthly_payment = payments(total, interest_rate, duration)
    loan_balance = remaining_payments(total, interest_rate, duration, nr_payments)
    total_amount_paid = loan_amount - remaining_payments(total, interest_rate, duration, nr_payments)

    print total
    print interest_rate/100.0
    print duration
    print monthly_payment
    print loan_balance
    print total_amount_paid
    

# Main Program
print(payments(100000, 1, 12))
print(remaining_payments(100000, 1, 12, 1))

loan_amount = input("loan amount: ")
annual_interest_rate = input("interest rate: ")
total_duration = input("duration of the loan: ")
nr_payments = input("how many payments: ")
loan(loan_amount, annual_interest_rate, total_duration, nr_payments)
