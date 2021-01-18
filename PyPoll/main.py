# PyPoll Assignment
# By: Luis Gomez - TTh 

# Dependencies

import os
import csv

# Read file

csv_path = os.path.join("Resources", "election_data.csv")

# Open CSV file

with open(csv_path) as csvfile:
    
    # Read .csv file

    csvreader = csv.reader(csvfile, delimiter = ",")

    # Store header row

    csv_header = next(csvreader)

    # Create list of candidates

    candidate_list = []
    votes_per_candidate = []
    election_winner = 0

    # For loop to gather needed data through each column:

    for row in csvreader:

        # Read the candidate
        current_candidate = row[2]

        # Add candidate to the list and initialize vote count if not already there
        if not current_candidate in candidate_list:
            candidate_list.append(current_candidate) 
            votes_per_candidate.append(0)

        # Count vote for a candidate if in the candidate list
        if current_candidate in candidate_list:
            candidate_index = candidate_list.index(current_candidate)
            votes_per_candidate[candidate_index] += 1
        

    
    # Calculate total votes

    total_votes = sum(votes_per_candidate)

    # Calculate vote shares

    vote_share_per_candidate = []

    for candidate in candidate_list:
        vote_share_per_candidate.append(0)
        vote_index = candidate_list.index(candidate)
        vote_share_per_candidate[vote_index] = round((votes_per_candidate[vote_index] / total_votes) * 100, 4)

    # Print election results

    results_str1 = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------"
    )

    print(results_str1)

    # Define how many candidates there are 
    total_candidates = len(candidate_list)

    # For loop to print each candidate along with their vote

    for i in range(total_candidates):
        print(f"{candidate_list[i]}: {vote_share_per_candidate[i]}00% ({votes_per_candidate[i]})")

    # Determine the winner

    winner_index = votes_per_candidate.index(max(votes_per_candidate))

    results_str2 = (
        f"-------------------------\n"
        f"Winner: {candidate_list[winner_index]}"
    )

    print(results_str2)

    