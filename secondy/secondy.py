# Using Python, have the function Secondy(lis) take the list of numbers stored in lis
# and return the second lowest and second greatest numbers, respectively, separated by a space.
# For example: if lis contains [7, 7, 12, 98, 106] the output should be 12 98.
# The list will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers!

#SECONDY 1
def Secondy1(lis):

    #Extract Ducpicates


    ##################

    list = sorted(lis)

    #getting second number
    second = list[0:1]

    #getting second last number
    i = len(list)
    second_last = list [i-2:i-1]

    xx = second + second_last
    y = " ".join(str(i) for i in xx)
    print (y)

# keep this function call below here
lis = [7, 7, 12, 98, 106]
Secondy1 (lis)


# SECONDY 2

def Secondy2(lis):
    lis = [7, 7, 12, 98, 106]

    #remove duplicates
    lis = set(lis)
    list = sorted(lis)

    #getting second number
    second = list[1]

    #getting second last number
    second_last = list [-2]

    print second,second_last

Secondy2 (lis)