# DOMESTIC TRADE
# LANGUAGE: PYTHON

# You have been hired by a trade company to write a program.

# They have given you a CSV (comma separated value, used in spreadsheets) file containing sales data by transaction
#for 10,000 sales transactions.

# Write a function that calculates the grand total of sales for a given item across all stores.

# Your output should be in a form of a dictionary, with total_KSH as a key and the total as a value.

# Additionally, the company wants to know which store location made the largest sales for that item. Add that as another hash key-value pair.

# Notes:
#  - Check out this website for an intro to handling CSV files

# Example:

#   Given a `TRANS.csv` of:

#   store,sku,amount
#   Nairobi,DM1210,7000 KSH
#   Nairobi,DM1182,1968 KSH
#   Naivasha,DM1182,5858 KSH
#   Mombasa,DM1210,6876 KSH
#   Nakuru,DM1182,5464 KSH

# If we enter 'DM1182', you program should return:
# {:total_KSH=> 13290, :largest=> 'Nairobi'}.
#
# def domestic_trade(itemId):
#   # Your Code Here!
#
# domestic_trade("DM1724")

#Working with csv files
#import csv
import csv

#opening file
f = open('TRANS.csv')

csv_f = csv.reader(f) #csv file object

# #printing all rows
# for row in csv_f:
#     print row #every row is a list

# #printing just store names
# for row in csv_f:
#     print row[0] #every row is a list
#

# #printing just item codes
# for row in csv_f:
#     print row[1]
#

##########################
#Total for particular item

#Get item details

item_no = "DM1724"
item_details = []
location = []
item = []
amount = []
details = ""

for row in csv_f:
    if row[1] == item_no:
        location.append(row[0])
        item.append(row[1])
        amount.append(int(row[2][:-4])) #removing  'KSH' from amount
        details = [row[0], row[1], int(row[2][:-4])]
    # var = details[0:1] + details[2:3]
    # print (var)
    # print (var[2:3])

print (location)
print (amount)

N = (i for i,x in enumerate(location) if x == 'Nairobi') #list comprehension
for i in N:
    # print (i)
    for a in amount:
        print (amount[i])

        # tot_Nai =+ amount[i]
    # print (tot_Nai)




# Finding sum of Nairobi Stores
# for row in csv_f:
#     if row[0] == "Nairobi":
#         Nai_Tot += int(row[2][:-4]))
#         print (Nai_Tot)

# i <= len(location)
# for x in location:
#     item_details = x + item([i]) + amount([i])
# print(len (location))
# print(len (item))
# print(len (amount))
# print (amount)

#
# print (set_location = set(location))
# print (set_item = set(item))
# print (set_amount = set(amount))

# #Finding total KSH
# total_KSH = 0
#
# for amt in amount:
#     total_KSH += amt
# print (total_KSH)
#

#Finding store with most sales

### combining the above

# print(len (location))
# print(len (item))
# print(len (amount))

# item_details = []
#
#
# # Finding sum of Nairobi Stores
# for row in csv_f:
#     if row[0] == "Nairobi":
#         Nai_Tot += int(row[2][:-4]))
#         print (Nai_Tot)
#
# # i <= len(location)
# # for x in location:
# #     item_details = x + item([i]) + amount([i])
#
#
# item_details = location + item + amount
# print (item_details)
#
#

# print (item_details)
# print (len(item_details))







#closing the file
f.close()
