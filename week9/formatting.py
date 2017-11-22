my_name = 'Sara '
my_age = 20
my_string = "Name = {} and Age = {} ".format(my_name, my_age)
print my_string

my_name = 'Sara '
my_age = 20
my_string = "Name = {0} and Age = {1} ".format(my_name, my_age)
print my_string

my_name = 'Sara '
my_age = 20
my_string = "Name = {1} and Age = {0} ".format(my_age, my_name)
print my_string

first_name = 'Sara '
date_of_birth = [11,02,1990]
family_name = 'Black '
my_string = "First name = {0}, Last name = {2} and Date of Birth = {1} ".format(my_name, date_of_birth, family_name)
print my_string

my_string = "x ={0:4d} and y ={1:7.10f}".format(12, 8.56)
print my_string


my_string = "x ={0:3d} and y ={1:7.4f} and z ={2:7.2f}".format(123456, 8.56, 23.5555)
print my_string
my_string = "{0:10s}:{1:4d}\n{2:10s}:{3:4d} ".format('Sara ', 18, 'John ', 9)
print my_string
