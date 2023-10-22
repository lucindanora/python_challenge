#import modules
import os
import csv

#setting file path for csv

election_data = "Resources/election_data.csv"

#converts election_data file to dictionary, and initialize dictionary

def processPollData(file):
    
    voterdict = {}
    with open(file,"r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        #skip header
        csv_header = next(csvreader)

        for row in csvreader: 
            #checks if candidate has been seen yet in the csv, and adds votes as needed
           
            if row[2] in voterdict.keys():
                voterdict[row[2]] += 1
            else:
                voterdict[row[2]] = 1
    return voterdict



#Find winning candidate by using max(), export .txt and placing .txt file in analysis folder

def writeReport(cdict):
    with open("Analysis/voteresults.txt","w") as textfile:
        textfile.write("Election Results\n")
        textfile.write("____________________\n")
        votes = cdict.values()
        total = sum(votes)
        maxvotes = max(votes)
        winnersList = []
        textfile.write(f"Total Votes: {total}\n")
        textfile.write("________________________________________\n")
        for name, votes in cdict.items():
            textfile.write(f"{name}  {votes / total * 100:.3f}% ({votes})\n")
            if votes == maxvotes:
                winnersList.append(name)
        textfile.write("______________________\n")
        textfile.write("Winner: ")
        for w in winnersList:
            textfile.write(w + " ")
        textfile.write("\n_______________________")

#prints results to terminal
def reporting(cdict):
    print("Election Results")
    print("___________________")
    votes = cdict.values()
    total = sum(votes)
    maxvotes =  max(votes)
    winnersList = []
    print(f"Total Votes: {total}")
    print("______________________________________")
    for name,votes in cdict.items():
        print(f"{name}  {votes/total * 100:,.3f}% ({votes})")
        if votes == maxvotes:
            winnersList.append(name)
    print("______________________")
    print("Winner: ",end=" ")
    for w in winnersList:
        print(w + " ",end =' ')
    print()
    print("______________________")



# runs functions seen above 
def main():
    candidatedict = {}
    candidatedict = processPollData(election_data)
    reporting(candidatedict)
    writeReport(candidatedict)

main()