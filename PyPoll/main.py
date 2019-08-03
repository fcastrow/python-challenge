#
#2019.08.02
#FFC
#
#This is my second Python Program
#
#2019.08.03
#simplify, quit trying to use a list of two lists, just use two lists...

import os
import csv
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
output_path = os.path.join(".", "output", "Python_homework_2.5.txt")

candidate_list = []
candidate_votes_list = []

total_number_of_votes = 0
candidate_count = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_number_of_votes += 1
        candidate = row[2]
        candidate_found = False

        for candidate_index in candidate_list:
            if( candidate == candidate_list[candidate_index] ):
                candidate_votes_list[candidate_index] += 1
                candidate_found = True
                break

        if not(candidate_found):
            candidate_count += 1
            candidate_list[candidate_count] = candidate
            candidate_votes_list[candidate_count] = 1
            
            


OutputFile = open(output_path, 'w')

print("total_number_of_votes " + str(total_number_of_votes))
OutputFile.write("total_number_of_votes " + str(total_number_of_votes) + "\n" )

OutputFile.close()
