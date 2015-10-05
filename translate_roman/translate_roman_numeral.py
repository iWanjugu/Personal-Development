# Given a roman numeral as input, write a function that converts the roman
# numeral to a number and outputs it.
#
# Ex:
# translateRomanNumeral("LX") # 60
#
# When a smaller numeral appears before a larger one, it becomes
# a subtractive operation. You can assume only one smaller numeral
# may appear in front of larger one.
#
# Ex:
# translateRomanNumeral("IV") # 4
#
# You should return `nil` on invalid input.



rn = 'ix'
RN = rn.upper()
print (RN)
first = RN [0:1]
second = RN [1:2]
print (first)
print (second)

rom_num = [I, V, X, L, C, M] = [1, 5, 10, 50, 100, 1000]

def init(first, second):
    var = ""
    var2 = ""
    for num in rom_num:
        if first == num:
            var = num
        elif second == num:
            var2 = num

        if first < second:
            ans = var2 - var
        elif first > second | first == second:
            ans = var + var2

    print (ans)

init (X,V)


# print(rom_num)
# print(I+X)
#
# for var in RN:
#     var = rom_num[var]
#
#

# ## Converting numerals to numbers
# for letter in rom_num:
#     list = []
#
#
#
# ## The Calculation
# if first < second:
#     ans = first - second
# else:
#     ans = first + second
#    if RN