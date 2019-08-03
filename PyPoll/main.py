#
#2019.08.02
#FFC
#
#This is my second Python Program
#

import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
output_path = os.path.join(".", "output", "Python_homework_2.5.txt")

total_number_of_votes = 0
list_of_candidates =[]
pct_of_votes_each_candidate_won = []
total_number_of_votes_each_candidate_won = []
election_winner = "me"

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_number_of_votes += 1

OutputFile = open(output_path, 'w')

print("total_number_of_votes " + str(total_number_of_votes))
OutputFile.write("total_number_of_votes " + str(total_number_of_votes) + "\n" )

OutputFile.close()
