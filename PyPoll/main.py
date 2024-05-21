import csv
import os

# Define the path to the CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = {}
winner = ""
winning_votes = 0

# Open the CSV file and read its contents
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
percentages = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    percentages[candidate] = percentage

# Determine the winner
for candidate, votes in candidate_votes.items():
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage in percentages.items():
    print(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, percentage in percentages.items():
        txtfile.write(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
