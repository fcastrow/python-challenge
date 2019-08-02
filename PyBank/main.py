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
greatest_increase = 0
greatest_increase_date = "1/1/1900"
greatest_decrease = 0
greatest_decrease_date = "1/1/1900"
change = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_number_of_months += 1
        net_total += int(row[1])

        if total_number_of_months > 1:
            change = int(row[1]) - last_profit_loss
            avg_change += change
            if change > greatest_increase:
                greatest_increase_date = row[0]
                greatest_increase = change
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        last_profit_loss = int(row[1])
avg_change = avg_change / total_number_of_months

print("Total months = " + str(total_number_of_months))
print("net_total = " + str(net_total))
print("avg_change = " + str(avg_change))
print("greatest_increase = " + str(greatest_increase_date) + " (" + str(greatest_increase)) + ")"
print("greatest_decrease = " + str(greatest_decrease_date) + " (" + str(greatest_decrease)) + ")"
