# DOMESTIC TRADE
# LANGUAGE: PYTHON

# You have been hired by a trade company to write a program.

# They have given you a CSV (comma separated value, used in spreadsheets) file containing sales data by transaction
# for 10,000 sales transactions.

# Write a function that calculates the grand total of sales for a given
# item across all stores.

# Your output should be in a form of a dictionary, with total_KSH as a key
# and the total as a value.

# Additionally, the company wants to know which store location made the largest sales for that item.
# Add that as another hash key-value pair.

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

def domestic_trade():

    import csv
    f = open('TRANS.csv')
    csv_f = csv.reader(f) #csv file object

    ##########################
    #Total for particular item

    #filtering out everything apart from the item we need 'item_no'
    location = []
    item = []
    amount = []
    item_no = raw_input('Enter the item Number: ')
    item_no = str(item_no.upper())

    for row in csv_f:
        if row[1] == item_no:
            location.append(row[0])
            item.append(row[1])
            amount.append(int(row[2][:-4])) #removing  'KSH' from amount


    #Finding total value (KSH) of particular item sold in ALL stores
    total_KSH = 0

    for amt in amount:
        total_KSH += amt

    # Finding largest selling store
    locations = set(location)
    locations = list(locations)

    tot_list = []
    for stuff in locations:
        tot = 0
        locs = (i for i,x in enumerate(location) if x == stuff)
        for i in locs:
            tot = tot + amount[i]   # Calculating the totals
        tot_list = tot_list + [tot] #Putting the totals in a list

    # Finding greatest Number
    great = (i for i,x in enumerate(tot_list) if x == max(tot_list))
    for i in great:
        largest = (locations[i])

    results = dict([('total_KSH', total_KSH), ('largest', largest)])
    print(results)


    #closing the file
    f.close()

domestic_trade()

