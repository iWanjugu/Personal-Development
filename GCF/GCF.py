# // Using java, have the function divide(num1,num2)
# // take both parameters being passed and return the Greatest Common Factor.
# // That is, return the greatest number that evenly goes into both numbers with no remainder.
# // For example: 20 and 10 both are divisible by 1, 2, 5 and 10 so the output should be 10.
# // The range for both parameters will be from 1 to 10^3.


def divide(num1, num2):
    c = min (num1,num2)
    cf= 0

    for i in range(1,c+1):
        if num1%i==0 and num2%i==0:
            cf = i
    print (cf)

divide(7,49)
