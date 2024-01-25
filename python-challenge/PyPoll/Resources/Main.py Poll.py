import os

# Module for reading CSV files
import csv

total_votes = 0 
candidates = {}
all_candidates = []
output = []

csvpath = os.path.join('.', 'PyPoll\Resources', 'election_data.csv')
output_data = os.path.join('.', 'Resources', 'election_data.txt')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    first_row = next(csvreader)
    candidates = {}
    for row in csvreader:
        total_votes +=1
        #if it is the first time a candidate name has been seen in the excel file,then return candidates name as a key  to a separate dictionary and assign a value of 1 
        if row[2] not in candidates:
            candidates[row[2]] = 1
        #if the candidate name is already in the candidates dictionary increment the dictionary by 1 
        else:
            candidates[row[2]] += 1
    output.append ('Election Results\n')
    output.append ('-------------------\n')
    output.append(f'Total Votes: {total_votes}\n')
    # take the candidates vote total and divide by the total number of votes 
    for candidate,candidate_count in candidates.items():
        percentage = (candidate_count / total_votes) * 100
        output.append(f'{candidate}: {percentage:.3f}% ({candidate_count})\n')
    # this gives me just the winners name without the num of votes
    output.append('----------------\n')
    winner = max(candidates, key=candidates.get)
    output.append(f'Winner: {winner}\n')
    output.append('------------------\n')

print(output)
with open('election_data.txt',"w") as election_data:
    election_data.writelines(output)





    
       