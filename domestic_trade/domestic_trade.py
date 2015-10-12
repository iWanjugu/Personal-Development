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

##########################
#Total for particular item

#filtering out everything apart from the item we need 'item_no'

location = []
item = []
amount = []
# item_no = raw_input('Enter the item Number: ')
# item_no = str(item_no.upper())

item_no = "DM1724"

for row in csv_f:
    if row[1] == item_no:
        location.append(row[0])
        item.append(row[1])
        amount.append(int(row[2][:-4])) #removing  'KSH' from amount


#Finding total value (KSH) of particular item sold in ALL stores
total_KSH = 0

for amt in amount:
    total_KSH += amt
print ("Total value sold for item number %s is %s" %(item_no, total_KSH))


# Finding total value (KSH) of particular item sold in ONE location
# store_location = raw_input('Enter the store location: ')
# store_location = store_location.lower().capitalize()

store_location = "Nairobi"

tot_store_amt = 0

# Extracting indexes for 'store_location' stores
loc = (i for i,x in enumerate(location) if x == store_location) #list comprehension
for i in loc:
    #Total Salesfrom stores
    tot_store_amt = tot_store_amt + amount[i]
print ("Total value sold for stores in %s is %s"  %(store_location, tot_store_amt))

# Finding largest selling store
locations = set(location)
locations = list(locations)
print(locations)
print(len(locations))
print(len(location))

tot_li = []
tot_loc_li = []
for stuff in locations:
    amn_li = []
    tot = 0
    locs = (i for i,x in enumerate(location) if x == stuff)
    for i in locs:
        tot = tot + amount[i]
        amn_li = amn_li + [amount[i]]
    print ("Total for %s is %s" %(stuff, tot))
    print("Number of Records for %s is %s" %(stuff, len(amn_li)))

    tot_li = tot_li + [tot]
print(tot_li)

# Finding greatest Number
great = (i for i,x in enumerate(tot_li) if x == max(tot_li))
for i in great:
    print ("Location with greates Sales is %s" % (locations[i]))



#
# #---------------------------------------------------------------------------
# #-----  Checks ----#
# # For Nairobi
# amn_nai_li = []
# amt_nai = 0
#
# Nai = (i for i,x in enumerate(location) if x == "Nairobi")
# for i in Nai:
#     # print (i) #indexes for where Nairobi stores occur in list
#     # Number of records for Nairobi
#     amn_nai_li = amn_nai_li + [amount[i]]
#
#     #Total Salesfrom Nairobi stores
#     amt_nai = amt_nai + amount[i]
#
#     # print (amt_nai)
#
#
# # No. of records for item
# print (len(location))
# print (len (amn_nai_li))
#
#


#closing the file
f.close()
