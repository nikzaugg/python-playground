# Strings are immutable
# -*- coding: utf-8 -*-

x = 'Hello'
print x[0], x[1], x[-1]
print 3*x

my_string = "The string module contains a number of useful constants and classes,as well as some deprecated legacy functions that are also available as methods on strings"
 
print my_string.count("str")
print my_string.count("as")
print my_string.count("z")
print my_string.count("s", 0, 30)   

my_string = "If the optional argument count is given, the first count occurrences are replaced"
 
my_string.replace("re", "**")
print my_string

new_string = my_string.replace("o", "OOOO")
print new_string

new_string = my_string.replace("t", "TTT", 2)
print new_string

my_list = my_string.split()
my_list2 = my_string.split('a')
print my_list
print my_list2

my_string = "AtesTsTriNg"
new_string = my_string.capitalize()
print new_string

my_string = "Hello world"
print my_string.find("z")
print my_string.find("l")

my_string = "Hello world"
print my_string.rfind("l")
print my_string.rfind("z")

my_string = "Hello world"
print my_string.index("l")
# print my_string.index("z")

my_string = "A test sTriNg"
print my_string.upper()

my_list = [ "one", "two", "three"]
my_string = "+"
print my_string.join(my_list)

print ord('a')

print ord('A')

print ord('&')

print chr(97)

print unichr(97)

print chr(108)

print unichr(108)

print chr(33)

print unichr(33)

print chr(127)

print unichr(127)