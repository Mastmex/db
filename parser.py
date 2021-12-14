import csv
from os import name

filename="surnames.csv"
nam="surnames.txt"

fields = []
rows = []
names = []
with open(filename,'r') as csvfile:
    csvreader =csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)  
    print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
  
with open(nam,'w') as un:
    for row in rows:
        un.write(row[0]+'\n')

