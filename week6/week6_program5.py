def changeCase(input_string):
    changed_string = ''
    for char in input_string:
        if ord(char) <= 122 and ord(char) >= 97:
            changed_string += chr(ord(char)-32)
        elif ord(char) >= 65 and ord(char) <= 90:
            changed_string += chr(ord(char)+32)
    return changed_string


# Main Program

input_string = raw_input("enter string: ")
print input_string

result = changeCase(input_string)
print result