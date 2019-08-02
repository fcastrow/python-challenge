#
#2019.08.02
#FFC
#
#This is my first Python Program
#

import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

total_number_of_months = 0
net_total = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)
        total_number_of_months += 1
        net_total += int(row[1])

print("Total months = " + str(total_number_of_months))
print("net_total = " + str(net_total))
