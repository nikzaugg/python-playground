''' numbers={1: 2, 3:4, 5:6}
numbers.pop(5)
print(numbers)

my_dict={"eins":["one",1],"zwei":["two",2],"drei":["three",3]}
print (my_dict.get("eins",'4'))

number_dict={"one": "uno", "two": "dos", "three": "tres"}
#print number_dict["tres"]

number_dict={"one": "uno", "two": "dos", "three": "tres"}
print "one" in number_dict

values =  [[3, 4, 5, 1], [33, 6, 1, 2]]

v = values[0][0] # 3
print v
print len(values)
for row in range(0, len(values)): # 0, 1, 2
    for column in range(0, len(values[row])): # columns 0, 1, 2
        if v < values[row][column]: # 3 < 
            v = values[row][column]
print v

m = [[x, y] for x in range(0, 2) for y in range(0, 2)]
print m
print len(m)  

def maxeven(lst):
    m = None
    for l in lst:
        for n in l:
            if n % 2 == 0:
                if m == None or m < n:
                    m = n
    return m

#Main Program
lst = input("Enter a 2-dimensional list: ") # [[1,2],[3,4]] -> 4
maximum_even = maxeven(lst)
if maximum_even:
    print "The maximum even value in the list : ", maximum_even
else:
    print "Your list has no even integer."

    

def multiply(mat1, mat2):
    rows = lambda m : len(m)
    cols = lambda m : len(m[0])
    
    if not cols(mat1) == rows(mat2):
        return None

    # do NOT use something like this (because lists are pointed at):
    # out = [[0]*cols(mat2)]*rows(mat1)

    # create matrix with 0s
    out =[[0 for _ in range(cols(mat2))] for _ in range(rows(mat1))]
    print out

    for i in range(rows(mat1)):
        for j in range(cols(mat2)):
            for k in range(cols(mat1)):
                out[i][j] += mat1[i][k] * mat2[k][j]
    return out        
 
# Main Body

A = input("Enter Matrix 1: ")
B = input("Enter Matrix 2: ")
C = multiply(A, B)
print C   


def tostring(num):

    d = {"0" : ["zero", ""],
         "1" : ["one", ""],
         "2" : ["two","twenty "],
         "3" : ["three","thirty "],
         "4" : ["four","forty "],
         "5" : ["five","fifty "],
         "6" : ["six","sixty "],
         "7" : ["seven","seventy "],
         "8" : ["eight","eighty "],
         "9" : ["nine","ninety "],
         "10" : "ten",
         "11" : "eleven",
         "12" : "twelve",
         "13" : "thirteen",
         "14" : "fourteen",
         "15" : "fifteen",
         "16" : "sixteen",
         "17" : "seventeen",
         "18" : "eighteen",
         "19" : "nineteen"}

    nl = list(str(num))
    print nl
    s = d[nl[0]][0] + " thousand "
    print s
    if not nl[1] == "0":
        s += d[nl[1]][0] + " hundred "
    

    if nl[2] == "1":
        s += d[nl[2] + nl[3]]
    elif nl[2] == "0":
        if nl[3] == "0":
            return s
        else:
            s += d[nl[3]][0]
    else:
        s += d[nl[2]][1] + d[nl[3]][0]

    return s

#Main Program

my_number = input("Enter a four-digit number: ")
output_string = tostring(my_number)
print output_string
'''

# This program receive the age of the user as an input 
# and give the age category as output.

age = input("How old are you? ")

dictionary = {
      age < 0:     "Unborn",
  0 < age <= 1:     "Infant",
  1 < age <= 4:     "Toddler",
  4 < age <= 11:    "Child",
 11 < age <= 17:    "Teenager",
 19 < age <= 55:    "Young Adult",
 19 < age <= 55:    "Adult",
 55 < age <= 100:   "Elder Adult",
100 < age <= 110:   "Centenarian",
110 < age:          "Supercentenarian"}

print dictionary[True]