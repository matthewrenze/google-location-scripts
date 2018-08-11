#%% Summarize Daily Google Location Data

# Purpose: This script summarizes Google location data on a daily basis

# Author: Matthew Renze

# Usage: python.exe Summarize.py [input-file] [output-file]
# - input-file - the CSV file containing Google location data
# - output-file - the CSV file to contain the daily summaries

# Example: python.exe Summarize.py C:\InputFile.csv C:\OutputFile.csv

# Notes: You must use the Convert.py script 
#        first in order to use this script

#%% Load libraries
import sys
import csv
import dateutil.parser

#%% Get arguments from console
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

#%% Open CSV input file
input_file = open(input_file_path)

#%% Create CSV reader
reader = csv.reader(input_file)

#%% Skip the header
next(reader)

#%% Read all rows of data
input_data = [row for row in reader]

#%% Close the input file
input_file.close()

#%% Reverse order of input data
input_data.reverse()

#%% Create summary table
summary_data = []

#%% Create lookup table
lookup_table = {}

#%% Summarize each row
for input_row in input_data:
    
    # Get date-time in ISO format
    iso_date_time = input_row[0]
    
    # Get date-time from ISO format
    date_time = dateutil.parser.parse(iso_date_time)
    
    # Get date from date-time
    date = date_time.date()
    
    # If date already exists then continue
    if (date in lookup_table):
        continue
    
    # Add date to look-up table
    lookup_table[date] = True
    
    # Get remaining fields
    latitude = input_row[1]
    longitude = input_row[2]
    accuracy = input_row[3]
    
    # Create a summary row
    summary_row = [date, latitude, longitude, accuracy]
    
    # Append the summary row to the summary table
    summary_data.append(summary_row)

#%% Create the output file
output_file = open(
    file = output_file_path,
    mode = "wt",
    newline = "")
    
#%% Create a file writer
writer = csv.writer(output_file)

#%% Write the header row
writer.writerow(["Date", "Latitude", "Longitude", "Accuracy"])

#%% Write each row to the output file
for output_row in summary_data:
    writer.writerow(output_row)
    
#%% Close the file
output_file.close()

