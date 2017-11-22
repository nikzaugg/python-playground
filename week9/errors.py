# Name Error
try:
    x_1 = y_1 + 1
except NameError:
    print "The variable name is not defined!"
else:   
    print x_1

# Zero Division Error
x,y = 2, 0
try:
    z = x / y
except ZeroDivisionError:
        print "Divide by zero!"
else:
    print z

# Example
x = input("Please enter a number different from zero: ")
try:
    y = 1/float(x)
except ZeroDivisionError:
    print "Divide by zero error!"
except ValueError:
    print "The input is not a number!"
except:
    print "something went wrong!"
else:   
    print "The 1/{0} is {1}".format(x,y)
finally:
    print "End."