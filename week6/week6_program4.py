import random

def unique_elements(list1, list2):
    unique_list = []
    for item in list1:
        if item not in list2:
            unique_list.append(item)

    for item in list2:
        if item not in list1:
            unique_list.append(item)

    return unique_list

def common_elements(list1, list2):
    common_list = []
    for item in list1:
        if item in list2 and item not in common_list:
            common_list.append(item)

    for item in list2:
        if item in list1 and item not in common_list:
            common_list.append(item)

    return common_list

def random_sample(user_number):
    sample = random.sample(range(1,51),user_number)
    return sample


# Main Program
m = input("enter size m for second sample (1-50): ")
n = input("enter size n for second sample (1-50): ")

sample1 = random_sample(m)
sample2 = random_sample(n)

sample1.sort()
sample2.sort()

print "sample1: ", sample1
print "sample2: ", sample2

output_unique = unique_elements(sample1, sample2)
output_common = common_elements(sample1, sample2)

output_unique.sort()
output_common.sort()
print "The unique elements of those two lists are:",output_unique
print "The common elements of those two lists are:",output_common

