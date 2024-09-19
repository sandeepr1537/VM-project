import csv
import json

# Read the CSV file and generate the variables.json file
with open('vm_data.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        variables = {
            "resource_group_name": row["resource_group_name"],
            "location": row["location"],
            "vm_name": row["vm_name"],
            "vm_size": row["vm_size"],
            "host_pool_name": row["host_pool_name"]
        }
        
        # Write to variables.json
        with open('variables.json', 'w') as json_file:
            json.dump(variables, json_file, indent=4)
