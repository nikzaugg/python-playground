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
'''