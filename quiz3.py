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