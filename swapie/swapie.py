#Using python, have the function SwapCase(str) take the str parameter
#and swap the case of each character.
#For example: if str is "Hello World" the output should be hELLO wORLD.
#Let numbers and symbols stay the way they are.

#NB do not use the swapcase python method.

# def swappie(str):
#     str_rev = []
#     for i in str:
#         a = i.upper()
#         b = i.lower()
#         if (i == a):
#             str_rev = str_rev.append(i.lower())
#             return str_rev
#         elif (i == b):
#             str_rev = str_rev.append(i.upper())
#             return str_rev
#         print(str_rev)
#
# print (swappie("Beautiful"))


def swappie(str):
    str_rev = []

    for i in str:
        if i == i.upper():
            str_rev.append(i.lower())
             # swap = [i.lower()]
            # str_rev2 = str_rev + swap
        else:
            str_rev.append(i.upper())
            # swap = [i.upper()]
            # str_rev2 = str_rev + swap

    print(''.join(str_rev))

swappie("BeauTiful")