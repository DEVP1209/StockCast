import csv
import json

# Initialize an empty list to store the JSON objects
json_array = []

# Open and read the CSV file
with open('symbols.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        symbol = row['SYMBOL']+".NS"
        json_object = {"key": symbol, "value": symbol}
        json_array.append(json_object)

json_file_name = 'symbols.json'

with open(json_file_name, 'w') as jsonfile:
    json.dump(json_array, jsonfile, indent=2)

print(f"JSON data has been saved to {json_file_name}")