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

for row in csv_f:
    if row[1] == item_no:
        location.append(row[0])
        item.append(row[1])
        amount.append(row[2][:-4]) #removing  'KSH' from amount

# print(len (location))
# print(len (item))
# print(len (amount))

set_location = set(location)
set_item = set(item)
set_amount = set(amount)

print(set_location)
print(set_item)
print(set_amount)

### combining the above
# print item_details
# print (len(item_details))

#finding total

for amt in amount:
    total_amount = sum(int(amt))
print (total_amount)

#closing the file
f.close()