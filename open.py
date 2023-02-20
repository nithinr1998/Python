import csv

#open csv file
with open('csvfile.csv','r') as file:
    #create csv reader
    reader=csv.reader(file)

    #iterate over the rows
    for row in reader:
        print(row)


