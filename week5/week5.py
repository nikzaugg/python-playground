# -*- coding: utf-8 -*-

import math
import fractions
import random

'''
print "pi =", math.pi
print "e =", math.e

frac_1 = fractions.Fraction(-2,4)
frac_2 = fractions.Fraction(18,-25)
print frac_1, frac_2

frac_3 = fractions.Fraction(2,8)
frac_4 = fractions.Fraction(-3,-12)
print frac_3 ==frac_4

frac_7 = fractions.Fraction(0.5)
frac_8 = fractions.Fraction(1.2)
print frac_7
print frac_8

frac_9 = fractions.Fraction(123456,56789)
approximation_9 = frac_9.limit_denominator(10)
print approximation_9

print fractions.gcd(fractions.Fraction('1/15'),fractions.Fraction(1.5))


print random.choice(['spider', 'tiger', 'dog', 'cat', 'fish'])
random.choice("CheckMethodChoiceFromModuleRandom")
random.choice(range(1000))

print random.randint(-100,100)
print random.randrange(1,6)
print random.randint(1,6)

print random.sample(range(1000),5)

print random.uniform(1,10)9

print random. uniform (10,1)

# Exercises Week 5

def func1() :
    x = input("enter number: ")
    f = lambda x : abs(pow(x,5)) - math.cos(math.pi * math.sqrt(x**2 + 1) + math.e)
    return f(x)
# Main Program
print func1()


# Cows and Bulls Game
def game():
    generated_number = str(random.randint(0,10000))
    while(True):
        cows = 0
        bulls = 0
        guess = raw_input("Enter your guess or press q to quit: ")
        print(guess)
        if(guess == "q"):
            print "\n Thanks for playing"
            break

        if(len(guess) < 4):
            print "enter a 4 digit number"
            continue
        
        if(guess == generated_number):
            print "correct! you won! congratulations"
            print "the magic number was: ", generated_number
            break
        
        for i in range(0,len(guess)):
            for j in range(0, len(generated_number)):
                if( (i==j) & (guess[j] == generated_number[i])):
                    bulls += 1
                if( (i!=j) & (guess[j] == generated_number[i])):
                    cows += 1
        print generated_number
        print 'bulls ',bulls, 'cows ', cows
# Main Program
game()
'''

print "Guess a number from 0 to 100"
raw_input("ready?")

answer = None
higher_than = 0
smaller_than = 100

while answer != "yes":
    
    if answer == "higher":
        higher_than = guess
    elif answer == "lower":
        smaller_than = guess
    elif answer == None:
        pass
    else:
        print "invalid input"

    guess = (higher_than + smaller_than) / 2
    print "is it", guess, "?"
    answer = raw_input(
        "enter: yes / higher / lower: ")

print "horray!"
