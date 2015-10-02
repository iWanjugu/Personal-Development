# Using ruby, have the function capitalize(str) take the str parameter being passed and capitalize
# the first letter of each word. Words will be separated by only one space.
# it should take string input from a user
# do not use the capitalize method


def capitalize(str_):

    str = str_.lower()
    str_split = str.split(" ")
    print (str_split)

    new_str = []

    for word in str_split:
        first_letter = word [0:1]
        rest_of_word = word [1:]
        first_letter_cap = first_letter.upper()

        new_word = [first_letter_cap + rest_of_word]

        new_str = new_str + new_word

    print (' '.join (new_str))

capitalize("This is a good day")