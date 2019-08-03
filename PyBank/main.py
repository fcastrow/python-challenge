#
#2019.08.02
#FFC
#
#This is my first Python Program
#

import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
output_path = os.path.join(".", "output", "Python_homework_1.5.txt")

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
    csv_header = next(csvreader)

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

OutputFile = open(output_path, 'w')

print("Total Months: " + str(total_number_of_months))
OutputFile.write("Total Months: " + str(total_number_of_months) + "\n" )

print("Total: $" + str(net_total))
OutputFile.write("Total: $ " + str(net_total) + "\n" )

print("Average Change: $" + str(avg_change))
OutputFile.write("Average Change: $" + str(avg_change) + "\n" )

print("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")" )
OutputFile.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")" + "\n" )

print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")" )
OutputFile.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")" + "\n" )

OutputFile.close()
