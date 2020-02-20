import os
import csv
csvpath=os.path.join('/Users/neethaabraham/Documents/ashwin_data/bank_data.csv')

months=0

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvfile)
    for data in csvreader:
        months=months+1

print(f'total months:{months}')


