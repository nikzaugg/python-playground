my_list = ["Blue", "Black", "Yellow", "Red", "Green", "Orange", "Orange"]
new_list = ["Car", "Bike", "Skateboard"]

print(my_list)
my_list.insert(0, "X")
print(my_list)
my_list.append("APPEND")
print(my_list)
my_list.remove("Black")
print(my_list)
item = my_list.pop(3) # pop([i]) - brackets indicate only that it is optional
print(item, '\n')

print(my_list)
print(my_list.index("Green"), '\n')

my_list.extend(['EXTEND1', 'EXTEND2'])
print(my_list, '\n')

print(my_list.count("Orange"))

my_list.sort()
print('sorted list: ', my_list, '\n')

my_list.reverse()
print('reversed list: ', my_list, '\n')

print(dir(my_list))