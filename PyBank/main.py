# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 08:46:24 2020

@author: thenry
"""
#added a test to make sure push works in git

import os
import csv

totalMonths=0  # total rows in file minus header
totalAmount=0  # accumulated total of all profit/loss entries
#average will be dynamic
greatestIncreaseAmount=0.0
greatestDecreaseAmount=0.0
greatestIncreaseList=[]
greatestDecreaseList=[]

budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read budget_csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:

        # Convert row to float and compare to grams of fiber
        #if float(row[7]) >= 5:
        #    print(row)
        totalMonths = totalMonths + 1
        totalAmount = totalAmount + float(row[1])
        
        if (int(row[1]) > 0):
            if (int(row[1]) > greatestIncreaseAmount):
                greatestIncreaseAmount=float(row[1])
                greatestIncreaseList = row
        else:
            if (int(row[1]) < greatestDecreaseAmount):
                greatestDecreaseAmount=float(row[1])  
                greatestDecreaseList = row
            
print("Financial Analysis")
print("--------------------------------------")
print("Total Months: " + str(totalMonths))
print("Total: $" + str(totalAmount))
print("Average Change: $" + str(totalAmount/totalMonths))
print("Greatest Increase in Profits: " + str(greatestIncreaseList[0] + " ($" + greatestIncreaseList[1] + ")"))
print("Greatest Decrease in Profits: " + str(greatestDecreaseList[0] + " ($" + greatestDecreaseList[1] + ")"))