import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'PyBank\Resources', 'budget_data.csv')
output_data = os.path.join('.', 'PyBank\Resources', 'budget_anaysis.txt')

total_months = 0
change_month = []
net_change_list = []
increase = ["", 0]
decrease = ["", 999999999]
net_total = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months +=1
    net_total += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

        net_change = int(row[1]) - prev_net
        #print("net change" +str(net_change))
        prev_net = int(row[1])
        #print ("prev net" +str(prev_net))
        net_change_list += [net_change]
        change_month = [row[0]]

        if net_change > increase[1]:
            increase[0] = row[0]
            increase[1] = net_change


        if net_change < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = net_change

# Calculate the Average Net Change
Avg_net = sum(net_change_list)/ len(net_change_list)


output = (
    f"Financial Analysis\n"
    f"Total Months: {total_months}\n"
    f"Total: {net_total}\n"
    f"Average Change: ${Avg_net}\n"
    f"Greatest Increase in Profits:{increase[0]} (${increase[1]})\n"
    f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})\n")

print(output)

with open(output_data, "w") as txt_file:
    txt_file.write(output)