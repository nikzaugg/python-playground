
def join_unique_lists(list1, list2):
    print 'inside function'
    unique_list = []
    for item in list1:
        if item not in unique_list:
            unique_list.append(item)

    for item in list2:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list



# Main Program
# raw_input returns the verbatim string entered by the user
# input actually evaluates the input as Python code
my_list1 = raw_input("Please enter the first list: ")
my_list2 = input("Please enter the second list: ")
print my_list1
print my_list2

my_list1 = my_list1.split(" ")
my_list2 = my_list2.split(" ")
print my_list1
print my_list2
output_list = join_unique_lists(my_list1, my_list2)
print "The unique elements of those two lists are:",output_list

