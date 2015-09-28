# Write a function that return whether or not the input string has balanced parantheses
# Balanced:
#   '((()))'
#   '(()())'
# Not balanced:
#   '((()'
#   '())('

def paren_matcher (str):
    print ("Number of right Parentesis: ", str.count("("))
    print ("Number of right Parentesis: ", str.count(")"))

    if str.count("(") == str.count(")"):
        print ("Parenthesis ARE balanced")
    else:
        print ("Parenthesis are NOT balanced")

paren_matcher ("blah(balh)nahhf(())yup)))")