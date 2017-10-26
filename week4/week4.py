############LOOPS
'''
list_numbers = input("please enter a list of integer numbers:")
print "The following numbers of the list are divisible by 3:"
for x in list_numbers:
    if x % 3 == 0:
        print x



print "The following numbers are divisible by 3 and end with 2:"
for index in range(1,300):
    if (index % 10 == 2) and (index % 3 ==0):
        print index

n = 100
summation = 0
counter = 1
while counter <= n:
    summation = summation + counter
    counter += 1

print "Sum of 1 to 100 is equal to", summation

winning_number = 2387
while input("Please enter a 4-digit number: ") != winning_number:  
    print "Sorry, you entered a wrong number!"      
print "Congratulations, you are the lucky winner!"

winning_number = 2387
key = raw_input("Do you want to play the game? (yes/ no)")
while key != 'no':
    password = input("Please enter a 4-digit number.")
    if password == winning_number:
        print "Congratulations, you are the lucky winner!"
        key = 'no'   # or using break instead of this line    
    else:
        print "Sorry, you entered a wrong number!"
        key = raw_input("Do you want to continue? (yes/ no)")


original_number = float(input("Please enter a number: "))
guess = float(input("Please enter your initial guess: "))
epsilon = 0.01
iteration = 0
while abs(original_number - guess**2) > epsilon:
    guess = (guess + original_number/guess )/2
    print guess
    iteration += 1
print "After", iteration,"iterations,",guess,"is an approximation to the root of", original_number     

############END LOOPS

############ BREAK and Continue
word = raw_input("please enter a string: ")
vowels = ['a', 'A', 'e', 'E', 'i','I', 'o', 'O', 'u', 'U']
for letter in word:
    if letter in vowels:
        continue
    print letter,

i = 2
print "The following numbers are prime: " 
while(i < 100):
    j = 2
    while(j < i):                 
        if i%j == 0:
            break                 # leave the inner loop
        j = j + 1
    if j >= i:                    
        print i   
    i = i + 1
'''

def factorial(n):
    """Calculate Factorial of n and return the result.

    Arguments:
    n: a positive integer
      Returns:
    product: the factorial of n
    """
    product = 1
    for index in range(1, n+1):
        product = product * index
    print n,"! is equal to",product
    return product

print factorial.__doc__