# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 08:46:24 2020

@author: thenry
"""
#added a test to make sure push works in git

import os, csv

totalVotesCast=0  # total rows in file minus header

x=0
y=0
reportList=[]

election_csv = os.path.join("Resources", "election_data.csv")
# Specify the file to write to
output_path = os.path.join("analysis", "analysis_output.csv")

# Open and read budget_csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:

        totalVotesCast = totalVotesCast + 1

reportList.append("Election Results")
reportList.append("--------------------------------------")
reportList.append("Total Votes: " + str(totalVotesCast))
reportList.append("--------------------------------------")
reportList.append("--------------------------------------")
reportList.append("--------------------------------------")

#print to standard output, or console
for i in range(len(reportList)):
    print(reportList[i])

#print to file   
f = open('./analysis/analysis_output.txt', 'w', newline='')  
for reportLine in reportList:
    f.write(reportLine+'\n')
f.close()



