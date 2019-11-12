import os
import csv

election_csv = os.path.join("03-Python_homework_Instructions_PyPoll_Resources_election_data.csv")

vote_count = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")

    for row in csvreader:
        vote_count += 1
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1

candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

candidates_and_votes = dict(zip(candidates,votes))
key = max(candidates_and_votes, key=candidates_and_votes.get)

khan_percent = (khan_votes/vote_count) * 100
correy_percent = (correy_votes/vote_count) * 100
li_percent = (li_votes/vote_count) * 100
otooley_percent = (otooley_votes/vote_count) * 100

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(int(vote_count)))
print("-------------------------")
print("Khan: " + str(int(khan_percent)) + "% (" + str(int(khan_votes)) + ")")
print("Correy: " + str(int(correy_percent)) + "% (" + str(int(correy_votes)) + ")")
print("Li: " + str(int(li_percent)) + "% (" + str(int(li_votes)) + ")")
print("O'Tooley: " + str(int(otooley_percent)) + "% (" + str(int(otooley_votes)) +")")
print("-------------------------")
print(f"Winner: " + key)
print("-------------------------")

election_results_file = os.path.join("Election_Results.txt")

with open(election_results_file,"w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write("Total Votes: " + str(int(vote_count)))
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write("Khan: " + str(int(khan_percent)) + "% (" + str(int(khan_votes)) + ")")
    file.write("\n")
    file.write("Correy: " + str(int(correy_percent)) + "% (" + str(int(correy_votes)) + ")")
    file.write("\n")
    file.write("Li: " + str(int(li_percent)) + "% (" + str(int(li_votes)) + ")")
    file.write("\n")
    file.write("O'Tooley: " + str(int(otooley_percent)) + "% (" + str(int(otooley_votes)) +")")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: " + key)
    file.write("\n") 
    file.write("-------------------------")