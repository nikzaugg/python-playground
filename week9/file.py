''' my_file = open('test.txt', 'r')
my_string = my_file.read()
print my_string

my_file = open('test.txt', 'r')
first_line_string = my_file.readline()
print first_line_string

second_line_string = my_file.readline()
print second_line_string 
my_file = open('test.txt', 'r')
line_list = my_file.readlines()
print line_list
My_file.close()

############
my_file = open('test_2.txt', 'w')

my_string = 'This a test string'
my_file.write(my_string)

value = 120
value_string = str(value)
my_file.write(value_string)

my_string = '*************'
my_file.write(my_string)

my_file.close()

###########
my_file = open('test.txt', 'w')
my_file.write("This is a test file")
my_file.close()

my_file = open('test.txt', 'r+')
my_string = 'Hello'
my_file.write(my_string)
my_file.seek(0) # Go to the beginning of the file
print my_file.read()

my_file.seek(0)
my_file.write("**")
my_file.seek(0) 
print my_file.read()

my_file.close()

##########
my_file = open('test.txt', 'r')
pointer = my_file.tell()
print pointer
my_file.close()
'''
my_file = open('test_2.txt', 'r')

my_string = my_file.read()
print my_string
my_list = my_string.split()
for index in range(len(my_list)):
    if my_list[index] == 'dolor':
        print index,
my_file.seek(0)
my_list = my_file.readlines()
print my_list
for index in range(len(my_list)):
    if my_list[index].find('dolor')!= -1:
        print '\nline', index,': '
        list_2 = my_list[index].split()
        for index_2 in range(len(list_2)):
            if list_2[index_2] == 'dolor':
                print index_2, "\n",
my_file.seek(0)

x = 1

for line in my_file:
    print 'line', x,': '
    print "------------"
    print line.find('dolor')
    print "------------"
    x += 1 