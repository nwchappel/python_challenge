import os
import csv

budget_csv = os.path.join("03-Python_homework_instructions_PyBank_Resources_budget_data.csv")

print("Financial Analysis")
print("----------------------------")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")
    month_count = sum(1 for row in csvreader)
    print("Total Months: " + str(int(month_count)))

total = []
average_change = []

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        row_totals = row[1]
        # print(row_totals)
        total.append(int(row_totals))
    print(f"Total: ${sum(total)}")
    for i in range(len(total)-1):
        average_change.append(total[i+1] - total[i])
    print(f"Average Change: ${round(sum(average_change) / len(average_change),2)}")

greatest_increase_profits = max(average_change)
greatest_decrease_profits = min(average_change)

# print(greatest_increase_profits)
# print(greatest_decrease_profits)

months = []

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        month_totals = row[0]
        # print(month_totals)
        months.append(str(month_totals))

greatest_increase_month = average_change.index(max(average_change)) + 1
greatest_decrease_month = average_change.index(min(average_change)) + 1

print(f"Greatest Increase in Profits: {months[greatest_increase_month]} (${(str(greatest_increase_profits))})")
print(f"Greatest Decrease in Profits: {months[greatest_decrease_month]} (${(str(greatest_decrease_profits))})")