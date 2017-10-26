''' 
info=["Simon", "White", 24, "Boston", 1.90, 95]
print('Simon' in info)

my_list = ['2', 'Anna', "John", 34, [1, 2]]
if 2 in my_list:
    print 'True'
else:
    print "False"

if 0:
    print 'Yes'
else:
    print "No"

if 2**3 == 8 and 11 % 2 != 2:
    print 'True'
else:
    print "False"

my_list = ['2', 'Anna', "John", 34, [1, 2]]
if "Anna" in my_list or 11 % 2:
    print 'True'
else:
    print "False"

if [34, 'Anna'] not in my_list or 11 % 2:
    print 'True'
else:
    print "False"


user_input = raw_input("Type integer: ")

if int(user_input)%5 == 0:
    print("yes")
else:
    print("No")


temp_input = raw_input("Type Celcius: ")
print(temp_input)
fahrenheit = int(temp_input)*(9.0/5.0)+32
print(fahrenheit) 

input = raw_input("Type Fahreheit or Celcius")
if input[-1] == 'F':
    celcius = int(input[:-1])/(9.0/5.0)-32
    print(celcius)
elif input[-1] == 'C':
    fahrenheit = int(input[:-1])*(9.0/5.0)+32
    print(fahrenheit)
else:
    print("Error, wrong input")


print "List of months: January, February, March, April, May, June, July, August, September, October, November, December"
month_name = raw_input("Input the name of Month: (e.g. April)")
if month_name == "February":  
    print month_name, "has 28/29 days."
elif month_name in ("April", "June", "September", "November"):  
    print month_name, "has 30 days." 
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):  
    print month_name, "has 31 days."  
else:  
    print("Error! Wrong month name") 


a = float(raw_input("Triangle Side 1: "))
b = float(raw_input("Triangle Side 2: "))
c = float(raw_input("Triangle Side 3: "))

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print "The triangle is valid."
if (a**2 == (b**2 + c**2)) or (b**2 == (a**2 + c**2)) or (c**2 == (a**2 + b**2)):
    print "The triangle is right-angle."
elif a == b == c:
    print "The triangle is equilateral."   
else:
    print "The triangle is not valid."  
'''