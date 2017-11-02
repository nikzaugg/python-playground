def anagram(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    l1 = list(s1)
    l2 = list(s2)
    
    for c in l1:
        if c in l2:
            l2.remove(c)
        else:
            return False

    if len(l2) == 0:
        return True
    return False

def anagram2(s1,s2):
    return anagram(s1.replace(" ", ""), s2.replace(" ", ""))
        
s1 = raw_input("Enter first string: ")
s2 = raw_input("Enter second string: ")
print "first method: ", anagram(s1,s2)
print "second method: ", anagram2(s1,s2)