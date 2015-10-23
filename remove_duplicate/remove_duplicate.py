
# def removeDuplicates(string):
# Your code here!

str = "bad boy"
str_ = str.split()
print str_
q = range(len(str))
con_sent = []

for num in q:
    print(str[num])
    con_sent = con_sent.append(str(num))

# for letter in str:
#     #getting
#     ind_pos = (i for i, x in enumerate (str) if x == letter)
#     for z in ind_pos:
#         lett_pos = []
#         lett_pos = lett_pos + [z]
#         print (z)
#         print (lett_pos)

#
# for i in str:
#     print (i)
#     print(str.count(i))
