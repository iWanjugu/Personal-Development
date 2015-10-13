# Using the Python, have the function CaesarCipher(str,num) take the str parameter and perform a Caesar Cipher shift
# on it using the num parameter as the shifting number.
# A Caesar Cipher works by shifting each letter in the
# string N places down in the alphabet (in this case N will be num).
# Punctuation, spaces, and capitalization should remain intact.
# For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

# to read more about ceaser's cipher visit http://practicalcryptography.com/ciphers/caesar-cipher/ or google some more
# happy coding :-)

import string

str = 'cat and dog'
str = str.split()
print (str)
num = 2
i = 0

blank = " "
alphabet = list(string.ascii_lowercase)
alphabet = alphabet.append(blank)
print(alphabet)
print(len(str))
print(len(alphabet))

# Breaking down sentence




# Breaking down words
sent_index = []
for j in range(0, len(str)):
    W = (i for i,x in enumerate(alphabet) if x == str[j])
    for i in W:
        sent_index = sent_index + [i]
print (sent_index)

new_sent_index = [x+num for x in sent_index]
print (new_sent_index)





# for i in str:
#     while i < len(str):
#         print (str[i])



