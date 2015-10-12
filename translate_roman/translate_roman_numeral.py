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


def translateRomanNumeral(rn):

    RN = rn.upper()

    num_li = []
    for letter in RN:
        if letter=='I':
            var = 1
        elif letter=='V':
            var = 5
        elif letter=='X':
            var = 10
        elif letter=='L':
            var = 50
        elif letter=='C':
            var = 100
        elif letter=='M':
            var = 1000

        num_li = num_li + [var]

    if len(rn) != 2:
        print ('nil')
    if len(rn) == 2:
        if num_li[0] < num_li[1]:
            ans = num_li[1] - num_li[0]
        elif num_li[0] > num_li[1] or num_li[0] == num_li[1]:
            ans = num_li[1] + num_li[0]
        else:
            ans = 'nil'
        print(ans)

translateRomanNumeral("mx")