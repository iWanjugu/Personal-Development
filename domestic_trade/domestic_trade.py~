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


def domestic_trade(itemId):
  # Your Code Here!
    import csv
  # Open csv file and assign it to variable opencsv
    with open('TRANS.csv', 'r') as csvfile:
    	total = 0
  # Go through the csv file
        readCSV = csv.reader(csvfile, delimiter=',')
  # Goes through the rows in the csv file
        for row in readCSV:
            for field in row:
                if field == itemId:
           			total += str(row[2])
           	print total

domestic_trade("DM1724")
csvfile.close()
