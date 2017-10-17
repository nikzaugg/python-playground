# -*- coding: utf-8 -*-
'''
for i in range(1, 10, 2):
    for y in range(0, (4- i / 2)+1, 1):
        print " ",
    for y in range(0, i, 1):
        print "*",
    print

my_string = "Hello World"
i = 192
while i%2 == 0:
    print my_string
    i = i/2
    print i

#Write a program using while loop, which prints the sum of every fifth numbers from 1 to 1005 ( both 1 and 1005 are included)
sum = 0
x = 1
count = 0
while x <= 1005:
    if x % 5 == 0:
        print(x)
        sum = sum+x
        count += 1
    x = x+1
print sum
print count
    
i = 1
Summation = 0
while i <= 1005:
    Summation  = Summation + i
    print i
    i = i + 5
print Summation 
print i/5


# Write a program using for loop, which ask user to enter a positive integer, n, 
# and prints the sum of every third number from 1 to n ( both 1 and n are included)

n = int(raw_input("Enter positive integer: "))
sum = 0
for i in range(1, n+1, 3):
    print i
    sum += i
print sum

# Fixed Point Iteration
x_old = 0
error = 1
iteration = 0
max_iteration = 100

while (iteration <= max_iteration) and (error > 10**(-8)):
    x_new = (x_old + 10)**0.25
    error = abs(x_old - x_new)
    x_old = x_new
    iteration += 1

print "After",iteration,"iterations, this is the approximation to the fixed point:", x_new


####################### Sample Code ################################
def bisec(a, b, tol):
    """Calculate a root of function 3x^2 − 5 using bisection method.
    
    Input:
    Interval:  [a, b] 
    Tolerance: tol
    Output:
    Refined interval: [a, b]
    midpoint of the interval: mid
    """
    mid = (a + b)/2.0
    iteration = 0
    if (3*a**2 - 5)*(3*b**2 - 5) >= 0:
        print "Error! f(a)*f(b) >=0!"
        return None
    
    else:
        mid = (a + b)/2.0
        iteration = 0
        while (b - a)/2.0 > tol:
            if 3*mid**2 - 5 == 0:
                return a, b, mid
            elif (3*a**2 - 5)*(3*mid**2 - 5) < 0:
                b = mid
            else:
                a = mid
            mid = (a + b)/2.0
            iteration += 1
    print "interval: [",a,",",b,"]", "Midpoint: ", (a + b)/2.0, "Nr of iterarions: ", iteration
    return a, b, (a + b)/2.0

# Main Program

bisec(-0.5, 0.6, 10**(-8))
bisec(-1.5, -0.4, 10**(-8))

# This program calculate the collatz sequence..

def collaz(n):
    if n <=0: return
    l = [n]
    while True:
        if n % 2 == 0:
            n /= 2
            l += [n]
        else:
            n = n*3+1
            l += [n]

        if l[-3:] == [4,2,1]:
            return l

#Main Program  
initial_Value = input('Type in a positive integer number: ')
print 'The Collatz sequence is: \n'
 
CollatzSequence = collaz(initial_Value)
print CollatzSequence


####################### Sample Code ################################
# This program calculate a fixed point x = g(x)  using fixed point theory.

def findroot(g, max_iteration):
    iteration = 0
    x_old = 0.0
    error = 1.0
    while (iteration < max_iteration) and (error > 10**(-8)):
        x_new = g(x_old)
        error = abs (x_old - x_new) 
        x_old = x_new
        iteration += 1
    return x_new

#Main Program
fp = findroot(lambda x : (x+10)**0.25,100)
print "This is the approximation to the fixed point:", fp

fp = findroot(lambda x : (x+50)**0.33,100)

####################### Sample Code ################################
# This program calculate a root of  the polynomial  3x^2 − 5 using bisection method.
def bisec(f, interval, tol):
    a = float(interval[0])
    b = float(interval[1])
    while abs(a-b) > tol:
        if f(a)*f((a+b)/2) <= 0:
            b = (a+b)/2
        elif f((a+b)/2)*f(b) <= 0:
            a = (a+b)/2
        else:
            print "No root found in interval", interval
            return
    return ([a,b],(a+b)/2)

# Main Program

print bisec(lambda x : 3*x**2-5, [-0.5,0.6], 0.00000001)
print bisec(lambda x : 3*x**2-5, [-1.5,-0.4], 0.000000001)


def my_fun(x):
    for m in range(0,3):
        n = 2
        while n <= 10:
            if m == n:
                x = x + 1
            n = n + 1
    return x
    
print my_fun(4)

# i in range(n) -> begins with 1, NOT 0
n = int(raw_input("Enter the height of the triangle as integer: "))
for i in range(n):
    print "* "*i
for i in range(n):
    print "* "*(n-i)


def perfect_number(n):
    """Check for a perfect number.

    Input:
    n : positive integer
    Output:
    True or False
    """

    my_sum = 0
    # In range, as the number it self should not be a diviser
    for diviser in range(1, n):
        if n % diviser == 0:
            my_sum = my_sum + diviser
    if my_sum == n:
        return True
    else:
        return False

# Main Body

answer = perfect_number(6)
print 6, answer
answer = perfect_number(9)
print 9, answer
answer = perfect_number(280)
print 280, answer
answer = perfect_number(8128)
print 8128, answer
'''