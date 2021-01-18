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

    # For loop to read through the data and collect variables

    for row in csvreader:
        
        # Define variables

        date = row[0]
        profit = int(row[1])

        # Totalize months over dataset and profit

        total_months += 1
        total_revenue += profit

        # Conditionals to compare datapoints and determine min/max profit and store date/profit in variables

        # Max profit

        if profit > max_profit: 
            max_date = date
            max_profit = profit 
        
        # Min profit
        
        elif profit < min_profit:
            min_date = date
            min_profit = profit


    # Calculate average revenue, dividing total revenue by number of entries

    avg_revenue = round(total_revenue / total_months, 2)

# Now that we have all of our variables, we can print them out... 

result_str = (
    f"Financial Analysis\n"
    f"----------------------------\n" 
    f"Total Months: {total_months}\n"
    f"Total: ${total_revenue}\n"
    f"Average Change: ${avg_revenue}\n"
    f"Greatest Increase in Profits: {max_date} (${max_profit})\n"
    f"Greatest Decrease in Profits: {min_date} (${min_profit})"
)

print(result_str)

with open("Output/bank_summary.txt", "w") as text: 
    print(result_str, file = text)