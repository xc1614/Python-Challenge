import csv
import os

csv_path = os.path.join ("..","Resources","budget_data.csv")

total_months = []
total_profits = []
profit_changes = 0
monthly_changes =[]
previous_value = 0

with open(csv_path) as csv_file:
    csvreader= csv.reader(csv_file, delimiter=",")
    csv_header=next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profits.append(row[1])
    print (len(total_months))

    total_profits=[int(x)for x in total_profits]
    total_profits_sum= sum(total_profits)
    print (total_profits_sum)

for i in range(len(total_profits)-1):
    monthly_changes.append(total_profits[i+1]-total_profits[i])