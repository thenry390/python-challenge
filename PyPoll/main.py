# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 08:46:24 2020

@author: thenry
"""
import os, csv

totalVotesCast=0  # total rows in file minus header
voteTabulation=[]
indexOfRow=0
voteCount=0
reportList=[]
maxVoteCount=0
winner=""
listLocation=0

election_csv = os.path.join("Resources", "election_data_sample.csv")
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
        try:
            indexOfRow=voteTabulation.index(row[2])
        except ValueError:
            indexOfRow=-1
            
        if (indexOfRow==-1):
#            voteTabulation.append(row[0])
            voteTabulation.append(row[2])
            voteTabulation.append(1)
        else:
            voteCount=int(voteTabulation[indexOfRow+1])+1
            voteTabulation[indexOfRow+1]=voteCount
            
            if(voteCount>maxVoteCount):
                maxVoteCount=voteCount
                winner=voteTabulation[indexOfRow]
            
reportList.append("Election Results")
reportList.append("--------------------------------------")
reportList.append("Total Votes: " + str(totalVotesCast))
reportList.append("--------------------------------------")
for voter in voteTabulation:
    reportList.append(voter)
    listLocation = listLocation + 1
reportList.append("--------------------------------------")
reportList.append("Winner: " + winner)
reportList.append("--------------------------------------")

#print to standard output, or console
for i in range(len(reportList)):
    print(reportList[i])

#print to file   
f = open('./analysis/analysis_output.txt', 'w', newline='')  
for reportLine in reportList:
    f.write(reportLine +'\n')
f.close()



