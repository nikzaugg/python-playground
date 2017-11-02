####################### Sample Code ################################
def reverse_v1(my_string):
  my_list = my_string.split()
  result = []
  for element in my_list:
    result.insert(0,element)
  return " ".join(result)

# method 2
def reverse_v2(my_string):
  my_list = my_string.split()
  my_list.reverse()
  return " ".join(my_list)

# test code
my_string = raw_input("Enter a sentence: ")
print reverse_v1(my_string)
print reverse_v2(my_string)

my_string = "this is a test"
print my_string.count('s',5)

my_string = "hello hello"
#'he' '' 'o he' '' 'o'
print my_string.split('l')