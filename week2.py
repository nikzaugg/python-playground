# Week 2 of MAT 101
import math
print type(2)
print type(2.34)
print type('eyeasdasd')

print True

print False

print bool(1)

print bool(0)

print bool(None)

print bool("Hi")

x = "Hello world"
print "-----"

print x == "Hello"

print x == "Hello world"

print bool("Hi" or "Bye")

print bool("" or "Hi")

print "" or ""

print "x" and "x"

print x == ("Hello world" or "another string")

print x == "Hello world" or x == "another string"

print not x == "another string"

print "-----"

print "Python numbers"

integer_1 = 5
integer_2 = -2
print type(integer_1)
print type(integer_2)

float_1 = -16.4
float_2 = 2.1
print type(float_1)
print type(float_2)
print "\n"

print "5/-2"
print integer_1/integer_2
print type(integer_1/integer_2)
print "\n"

print "-16.4/2.1"
print float_1/float_2
print type(float_1/float_2)
print "\n"

print "-16.4//2.1"
print float_1//float_2
print type(float_1//float_2)
print "\n"

print "5/-16.4"
print integer_1/float_1
print type(integer_1/float_1)
print "\n"

print "LONG TYPE"

long_integer_1 = 99999999999999999999999999999999999999999

long_integer_2 = 10**40

print long_integer_1
print long_integer_2

print type(long_integer_1)

print type(long_integer_2)
print "---------------"

list1 = range(0,10)
print list1

list2 = range(1, 10, 2)
print list2

names = ['One', 'Two', 'Three', 'Four']
names2 = ["John", "Nik"]
print names
print names2

print names[-4]
print names[0]

x = [1]
print x 

y = [2]
print y

z = [3]
print z

w = x
print w
w[0] = 99
print w
x = x + [4]     # adding in a list means inserting new element to the list, we see it later 
print x
print w

print x, y, z, w

x = 10.015; 
y = 1.005; 
z = 0.03 ; 
print (x+y) + z == x + (y+z)


print  0.3 == 0.3

print 2.21 + 1.81
print int(float('2.21') + float('1.81'))
print int(long(2.21) + long(1.81))

round(2.5, 2)
x = round(2.5264, 2)
print x
print  bool(None)
print bool("")
print bool()
print bool([])
print "__________"

print True + 1

print "-------------"
x, y = -1, 2
print x != y or y**2 == y
print not(x < -2) and y == 5
print not x < -1 and y == -2
print not x < -1 and y == 2

# (false AND false) OR TRUE
print x < -1 and x == y or y < 3