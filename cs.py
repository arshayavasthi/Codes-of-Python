import csv
with open('tec.csv')as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')
    for row in readcsv:
        print(row)
        
