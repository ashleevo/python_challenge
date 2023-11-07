#import os module
import os
#module for reading files
import csv

#set path for file
csv_path = os.path.join("election_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))


#make empty lists
candidates = []
number_of_votes = []
percent_of_votes = []

#counter for total votes
total_votes = 0

#using method 2: improved reading using CSV module
with open (csv_path, encoding = 'UTF-8') as csvfile:
    #create variable that holds contents and specify delimiter
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    #iterate through the rows to add to total vote counter
    for row in csvreader:
        # Add to our vote-counter, new candidates not indicated within the list will have 1 added (to signify 1 vote)
        # python indexes columns starting 0, so candidate list will be row 2 
        # ^ conditional statement created
        total_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_of_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_of_votes[index] += 1
    
    # add to the percent of votes list 
    for votes in number_of_votes:
        percentage = (votes/total_votes) * 100
        percentage = (percentage)
        percentage = "%.3f%%" % percentage
        percent_of_votes.append(percentage)
    
    # winning candidate
    winner = max(number_of_votes)
    index = number_of_votes.index(winner)
    winning_candidate = candidates[index]

# print results to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_of_votes[i])} ({str(number_of_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# exporting to a txt file
output = open("printedresults.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_of_votes[i])} ({str(number_of_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))