'''
def my_sieve_v1(n):
    if n < 2:
        print("There is no prime before n.")
        return
    else:            
        non_prime = []
        for i in range(2, n+1):
            if i not in non_prime:
                print(i),
                for j in range(i*i, n+1, i):
                    #All the multiples of i before i*i are already considered in previous steps
                    non_prime.append(j)
      

# Main Body
n = input("Please insert a positive integer: ")
print("\nHere is the list of prime numbers from 1 to %s:"%n)
print(type(n))
my_sieve_v1(n) 
'''

# PROGRAM 2  
# Write a program to generate all sublists of a list.
def new_sublist(mask,my_list):
    sub = []
    for i in range(len(mask)):
        if mask[i]:
            sub.append(my_list[i])

    return sub

def next_mask(mask):
    n = len(mask)
    i = n-1
    while mask[i] == 1:
        mask[i] = 0
        i = i - 1
    mask[i] += 1
    return mask     
# Main Body
my_list = input("Please insert a list,e.g., [1,2]): ")
n = len(my_list)
sub_lists = []
mask = [0]*n
for i in range(2**n):
    sub = new_sublist(mask, my_list)
    sub_lists.append(sub)
    mask = next_mask(mask)
    
print "Here is the list of all sublists: \n"
print sub_lists