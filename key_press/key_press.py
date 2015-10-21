# FEATURE PHONE KEY PRESSES
# LANGUAGE: PYTHON


# This is a feature phone keypad:

# ------- ------- -------
# |     | | ABC | | DEF |
# |  1  | |  2  | |  3  |
# ------- ------- -------
# ------- ------- -------
# | GHI | | JKL | | MNO |
# |  4  | |  5  | |  6  |
# ------- ------- -------
# ------- ------- -------
# |PQRS | | TUV | | WXYZ|
# |  7  | |  8  | |  9  |
# ------- ------- -------
# ------- ------- -------
# |     | |     | |     |
# |  *  | |  0  | |  #  |
# ------- ------- -------


# Before predictive text entry systems like T9, you had to press a button repeatedly to cycle through the possible values until you reached the one you wanted. 
# For example, to type "V8" you would press the 8 key three times and then again four times (pressing the 8 key cycles through T->U->V->8), giving us a total of seven key presses. 

# Note: the 0 key handles spaces and outputs 0 when tapped twice.

# Write a function that can calculate the amount of button presses required for any phrase. Except for spaces, punctuation can be ignored.
# Your function should accept both uppercase and lowercase letters and treat them the same.

# Examples:

# presses('V8') # 7
# presses('LOL') # 9
# presses('How R u 2day') # 23 
# presses("i 8 2 Many mandazi 4 brekky") # 55

# Bonus: Try to avoid hard-coding the number of button presses for each letter!

from numpy import array
import string
import numpy as np

# def presses(str):
####################################
###### Keypad values


### Create a matrix of values just like the keypad.
# Index value will be the  number of times tobe pressed

a = list(string.lowercase)
matrix = []

#creating the one digit entities
ones = ('1','*', '0', '#')
matrix1 = np.zeros((1,1))

for x in ones:
    matrix1 = np.concatenate((matrix1, np.matrix([x])))
print (matrix1)

#creating the three digit entities
i = range(0, 27)
a_3 = a[:15]
matrix4 = np.zeros((0, 4))

for i, item in enumerate(a_3):
    if (i%3==0):
        matrix4 = np.concatenate((matrix4 , [a[i:i+3] + [(i/3)+2]]))

print (matrix4)

#creating the four digit entities

# z = range(15, 27)
matrix5 = array ((a[15:19] + [7],\
              a[22:]+[9]))
print matrix5

# # matrix1
#  [['1']
#  ['*']
#  ['0']
#  ['#']]
#
# # matrix4
# [['a' 'b' 'c' '2']
#  ['d' 'e' 'f' '3']
#  ['g' 'h' 'i' '4']
#  ['j' 'k' 'l' '5']
#  ['m' 'n' 'o' '6']]
#
# # matrix5
# [['p' 'q' 'r' 's' '7']
#  ['w' 'x' 'y' 'z' '9']]


# finding index of a value in matrix
val = 'a'
val_index = np.where(matrix4 == val)
print (val_index) #index of value you're looking for

#the y (column) index i,e the number of times the keypad will be pressed to get the desired letter/ number

key_press = int (val_index[1]) + 1
print (key_press)




#
# # Change to lowercase and string
# input = "BoY"
#
# input = str(input.lower())
# print (input)
# #
# for letter in input:
#
