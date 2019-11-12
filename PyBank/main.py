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

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        row_totals = row[1]
        #print(row_totals)
        total.append(int(row_totals))
    print(f"Total: ${sum(total)}")
    