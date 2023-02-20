import csv

#specify the column indices that you want to read
columns_to_read=[0,2]

#ope csv file and read contents
with open('csvfile.csv','r') as f:
    clmn_reader=csv.reader(f)

    #iterate over the rows
    for row in clmn_reader:
     #print contents of specific cols
        print([row[i] for i in columns_to_read])
