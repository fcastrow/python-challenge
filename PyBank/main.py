#
#2019.08.02
#FFC
#
#This is my first Python Program
#

import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
output_path = os.path.join(".", "output", "Python_homework_1.5.csv")

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
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

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

open(output_path, 'w', newline='') as csvfile:
csvwriter = csv.writer(csvfile, delimiter=',')
#csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])


print("Total Months: " + str(total_number_of_months))
csvwriter.writerow(['"Total Months: " + str(total_number_of_months)'])

print("Total: $" + str(net_total))
csvwriter.writerow(['"Total Months: " + str(total_number_of_months)'])

print("Average Change: $" + str(avg_change))
csvwriter.writerow(['"Average Change: $" + str(avg_change)'])

print("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")" )
csvwriter.writerow(['"Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")"'])

print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")" )
csvwriter.writerow(['("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")"'])
