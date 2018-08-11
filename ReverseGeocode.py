#%% Reverse Geocode Google Location Data

# Purpose: Reverse geocodes lat/lon from Google location data

# Author: Matthew Renze

# Usage: python.exe ReverseGeocode.py input-file output-file
#   - input-file - the CSV file containing Google Location data
#   - output-file - the CSV file containing reverse-geocoded locations

# Example: python.exe ReverseGeocode.py C:/InputFile.csv C:/OutputFile.csv

# Notes: You must use the Convert.py script 
#        first in order to use this script
#
#        Uses reverse geocoder library found here:
#        https://github.com/thampiman/reverse-geocoder

#%% Load libraries
import sys
import csv
import reverse_geocoder as rg

#%% Get arguments from the console
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

#%% Read input CSV file
input_file = open(input_file_path)

#%% Create a CSV reader
csv_reader = csv.reader(input_file)

#%% Skip the header
next(csv_reader)

#%% Read the data
data = [row for row in csv_reader]

#%% Close the input file
input_file.close()

#%% Create the output file
output_file = open(
    file = output_file_path,
    mode = "wt",
    newline = "")

#%% Create a CSV writer
csv_writer = csv.writer(output_file)

#%% Write the header
csv_writer.writerow(["Date", "Latitude", "Longitude", "Accuracy", "Country", "State", "County", "City"])

#%% Create coordinates list
coordinates = []

#%% Get coordinates for each row
for row in data:
    coordinates.append((row[1], row[2]))

#%% Geocode coordinates
results = rg.search(coordinates)

#%% Process each row
for i, row in enumerate(data):    

    # Get matching reverse-geocode results
    result = results[i]    

    # Get fields from input data
    date = row[0]
    latitude = row[1]
    longitude = row[2]
    accuracy = row[3]

    # Get fields from reverse-gecode data
    country = result["cc"]
    state = result["admin1"]
    county = result["admin2"]
    city = result["name"]
    
    # Write row to output file
    csv_writer.writerow([date, latitude, longitude, accuracy, country, state, county, city])
    
#%% Close the output file
output_file.close()
