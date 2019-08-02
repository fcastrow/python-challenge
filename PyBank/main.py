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
avg_change = 0


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_number_of_months += 1
        net_total += int(row[1])

        last_profit_loss = int(row[1])
        if total_number_of_months > 1:
            avg_change += int(row[1]) - last_profit_loss

        avg_change = avg_change / total_number_of_months
            

print("Total months = " + str(total_number_of_months))
print("net_total = " + str(net_total))
print("avg_change = " + str(avg_change))
