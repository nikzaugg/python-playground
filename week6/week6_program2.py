def unique_list(my_list):
    output_list = []
    for item in my_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

# Main Body

my_list = input("Please enter a list: ")
output_list = unique_list(my_list)
print output_list