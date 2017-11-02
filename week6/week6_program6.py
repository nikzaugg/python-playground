def reverse_string_function(s):
    l = s.split(" ")
    for i, s in enumerate(l):
        print s[::-1] 
        l[i] = s[::-1] # This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.
    return " ".join(l)
            


# Main Program

input_string = raw_input("enter sentence where strings are separated by space: ")
result = reverse_string_function(input_string)
print result