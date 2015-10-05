# Using Python, have the function Secondy(lis) take the list of numbers stored in lis
# and return the second lowest and second greatest numbers, respectively, separated by a space.
# For example: if lis contains [7, 7, 12, 98, 106] the output should be 12 98.
# The list will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers!


def Secondy(lis):

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
lis = [3,66,73,93,2,5]
Secondy (lis)

# # x = x.append(second_last)
# # print (x)
