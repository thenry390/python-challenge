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
greatestIncreaseAmount=0.0
greatestDecreaseAmount=0.0
previousMonth=0.00
change1=0.00
change2=0.00
monthOverMonthChange=[]
greatestIncreaseList=[]
greatestDecreaseList=[]
x=0
y=0
# define a list of lists for finding max and min
maxValue=0
minValue=0
reportList=[]
#trackChangeDict ={'Month':[],'Amount':[]}

budget_csv = os.path.join("Resources", "budget_data.csv")
# Specify the file to write to
output_path = os.path.join("analysis", "analysis_output.csv")

# Open and read budget_csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:

        monthOverMonthChange.append(int(row[1])-previousMonth)

        previousMonth = int(row[1])        

        if (int(row[1]) > 0):
            if (int(row[1]) > greatestIncreaseAmount):
                greatestIncreaseAmount=int(row[1])
                greatestIncreaseList = row
        else:
            if (int(row[1]) < greatestDecreaseAmount):
                greatestDecreaseAmount=int(row[1])  
                greatestDecreaseList = row
                
        totalMonths = totalMonths + 1
        totalAmount = totalAmount + int(row[1])
        
x=sum(monthOverMonthChange)-monthOverMonthChange[0]
y = len(monthOverMonthChange)-1

reportList.append("Financial Analysis")
reportList.append("--------------------------------------")
reportList.append("Total Months: " + str(totalMonths))
reportList.append("Total: $" + str(totalAmount))
reportList.append("Average Change: $" + str(round((x/y),2)))
reportList.append("Greatest Increase in Profits: " + str(greatestIncreaseList[0] + " ($" + str(max(monthOverMonthChange)) + ")"))
reportList.append("Greatest Decrease in Profits: " + str(greatestDecreaseList[0] + " ($" + str(min(monthOverMonthChange)) + ")"))

#print to standard output, or console
for i in range(len(reportList)):
    print(reportList[i])

#print to file   
f = open('./analysis/analysis_output.txt', 'w', newline='')  
for reportLine in reportList:
    f.write(reportLine+'\n')
f.close()



