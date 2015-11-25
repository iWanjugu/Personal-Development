# Using Python, have the function xoxo(str) take the str parameter
# being passed and return the string true if there is an equal number of x's and o's,
# because you cannot recieve an uneven number of hugs and kisses :-)
# otherwise return the string false. Only these two letters will be entered in the string,
# no punctuation or numbers.
# For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.



#my own tests
"""
str = "xoxxoo"
x = []

for i in str:
    i = len(x)
    while i < len(str):
        x.append(str[i:1+i])
        print (x)
        i += 1

print(x)

print(len(str))
print(len(x))

z = x.count("x")
q = x.count("o")
print(z)
print(q)

i = 0

for i < len(x) in str:
    print(i)
    i += 1
"""

############## XOXO FUNCTION
# xo = []
# def xoxo(str):
#
#     for i in str:
#         i = len(xo)
#         while i < len(str):
#             xo.append(str[i:1+i])
#             i += 1
#             # print (xo)
#             count_x = xo.count("x")
#             count_o = xo.count("o")
#             # print (count_x)
#             # print (count_o)
#     print ("The number of 'x's is: ", count_x)
#     print ("The number of 'o's is: ", count_o)
#
#     if (count_o == count_x):
#         print ("TRUE")
#     else:
#         print("FALSE")
#
# print (xoxo("xoxxooxoo"))

def xoxo(str):
    str = str.lower()
    if str.count("x")==str.count("o"):
        print("TRUE")
    else:
        print ("FALSE")

xoxo("XXoxOO")


# keep the function call
#print xoxo("have fun..xoxo")
