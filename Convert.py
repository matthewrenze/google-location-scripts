#%% Convert Google Location Data JSON to CSV

# Purpose: Converts Google location data from JSON format to CSV format

# Author: Matthew Renze

# Usage: python.exe Convert.py input-file output-file
#   - input-file - the Google location JSON file to be converted
#   - output-file - the CSV file to be created from the conversion

# Example: python.exe Convert.py C:\InputFile.json C:\OutputFile.json

# Note: Works with Google Location data from the Google Takeout website
#       found here: https://takeout.google.com/
#
#       Currently returns only date-time, latitude, longitude, and accuracy

#%% Load libraries
import sys
import json
import csv
import datetime

#%% Get arguments from console
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

#%% Read JSON file
input_file = open(input_file_path)

#%% Parse JSON data
input_data = json.load(input_file)

#%% Close the file
input_file.close()

#%% Open the output file
output_file = open(
    file = output_file_path, 
    mode = "wt", 
    newline = "")

#%% Create a file writer
writer = csv.writer(output_file)

#%% Write header to output file
writer.writerow(["DateTime", "Latitude", "Longitude", "Accuracy"])

#%% Write rows of data to output file
for item in input_data["locations"]:
    
    # Read timestamp
    timestamp = int(item["timestampMs"])
    
    # Convert timestamp to seconds
    timestamp_seconds = timestamp / 1000
    
    # Convert timestamp to date/time
    date_time = datetime.datetime.utcfromtimestamp(timestamp_seconds)
    
    # Convert timestamp to ISO date time
    iso_date_time = date_time.isoformat()
    
    # Read latitude (E7 format)
    latitudeE7 = item["latitudeE7"]
    
    # Convert to normal latitude
    latitude = int(latitudeE7) / 1E7
    
    # Read longitude (E7 format)
    longitudeE7 = item["longitudeE7"]
    
    # Convert to normal longitude
    longitude = int(longitudeE7) / 1E7
    
    # Read accuracy
    accuracy = item["accuracy"]
    
    # Create row of data
    row = [iso_date_time, latitude, longitude, accuracy]
    
    # Write row of data to output file
    writer.writerow(row)
    
#%% Close the output file
output_file.close()