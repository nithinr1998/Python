# Write a Python program to write a Python dictionary to a csv file.
# After writing the CSV file read the CSV file and display the content.

import csv

# Data to be inserted
data = [{'Name': 'Shyam', 'Age': 22, 'Place': 'E.petta'},
{'Name': 'Nithin', 'Age': 23, 'Place': 'Vagamon'},
{'Name': 'Philip', 'Age': 22, 'Place': 'Angel valley'}]

# Write to CSV file
with open('Mca 2022.csv', 'w') as csvfile:
      headernames = ['Name', 'Age', 'Place']
      csvwriter = csv.DictWriter(csvfile, fieldnames=headernames)
      csvwriter.writeheader()
      for row in data:
           csvwriter.writerow(row)

# Read from CSV file and print contents
with open('Mca 2022.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
              print(row)