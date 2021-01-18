# PyBank Assignment
# By: Luis Gomez - TTh 

# Dependencies

import os
import csv

# Read file

csv_path = os.path.join("Resources", "budget_data.csv")

# Open CSV file

with open(csv_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    # Initialize variables to store data of interest

    total_months = 0
    total_revenue = int()
    avg_revenue = float()
    max_date = ""
    max_profit = 0
    min_date = ""
    min_profit = 0

    # Skip header row

    header_row = next(csvreader)
    
    # Initialize change list and comparisons (previous change, max change, min change)
    
    previous_profit = 0
    change_list = []
    max_change = 0
    min_change = 0

    # For loop to read through the data and collect variables

    for row in csvreader:
        
        # Define variables

        date = row[0]
        profit = int(row[1])

        # Totalize months over dataset and profit

        total_months += 1
        total_revenue += profit

        # Conditionals to compare datapoints and determine min/max change in profit and store date/profit in variables

        # Calculate change in profit starting from the second month 

        if total_months > 1:
            change = profit - previous_profit
            change_list.append(change)
                
                # Max change

            if change > max_change: 
                max_date = date
                max_change = change  
        
           # Min change
        
            elif change < min_change:
                min_date = date
                min_change = change

        previous_profit = profit

    # Calculate average change, dividing total of changes by number of changes

    avg_change = round( sum(change_list) / len(change_list), 2)

# Now that we have all of our variables, we can print them out and store them in a .txt file

result_str = (
    f"Financial Analysis\n"
    f"----------------------------\n" 
    f"Total Months: {total_months}\n"
    f"Total: ${total_revenue}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {max_date} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_date} (${min_change})"
)

print(result_str)

with open("Output/bank_summary.txt", "w") as text: 
    print(result_str, file = text)