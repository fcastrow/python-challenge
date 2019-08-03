#
#2019.08.02
#FFC
#
#This is my second Python Program
#
#2019.08.03

import os
import csv
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
output_path = os.path.join(".", "output", "Python_homework_2.5.txt")

candidate_list = []
candidate_votes_list = []
winner = "me"
winner_votes = 0

total_number_of_votes = 0
candidate_count = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_number_of_votes += 1
        candidate = row[2]
        candidate_found = False

        for candidate_index in range(len(candidate_list)):
            if( candidate == candidate_list[candidate_index] ):
                candidate_votes_list[candidate_index] += 1
                candidate_found = True
                break

        if not(candidate_found):
            candidate_list.append(candidate)
            candidate_votes_list.append(1)
            candidate_count += 1

OutputFile = open(output_path, 'w')

print("Election Results")
OutputFile.write("Election Results\n" )

print("-------------------------")
OutputFile.write("-------------------------\n" )

print("Total Votes: " + str(total_number_of_votes))
OutputFile.write("Total Votes: " + str(total_number_of_votes) + "\n" )

print("-------------------------")
OutputFile.write("-------------------------\n" )

for candidate_index in range(len(candidate_list)):
    print(candidate_list[candidate_index] + ": " + str(round(100*candidate_votes_list[candidate_index]/total_number_of_votes,2)) + "(" + str(candidate_votes_list[candidate_index]) + ")" )
    OutputFile.write(candidate_list[candidate_index] + ": " + str(round(100*candidate_votes_list[candidate_index]/total_number_of_votes,2)) + "(" + str(candidate_votes_list[candidate_index]) + ")\n" )
    if(candidate_votes_list[candidate_index] > winner_votes):
        winner_votes = candidate_votes_list[candidate_index]
        winner = candidate_list[candidate_index]

print("-------------------------")
OutputFile.write("-------------------------\n" )

print("Winner: " + winner)
OutputFile.write("Winner: "  + winner + "\n" )

print("-------------------------")
OutputFile.write("-------------------------\n" )

OutputFile.close()
