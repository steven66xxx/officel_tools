import os
import pandas as pd

# Get current directory
path = os.getcwd()

# Get all Excel files in the current directory
excel_files = [f for f in os.listdir(path) if f.endswith('.xlsx')]

# Create empty DataFrame to store merged data
merged_data = pd.DataFrame()

# Loop through each Excel file and append its data to the merged data
for excel_file in excel_files:
    # Load data from the Excel file into a DataFrame object
    data = pd.read_excel(excel_file)
    # Append the data to the merged data
    merged_data = merged_data.append(data)

# Write the merged data to a new Excel file in the current directory
merged_data.to_excel('merged_data.xlsx', index=False)