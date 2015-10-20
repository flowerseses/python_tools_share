import csv
from dateutil.parser import parse
from dateutil.tz import *
import datetime

def new_row(row1, row2):
    return not((row1[0] == row2[0]) and (row1[1] == row2[1]) and (row1[4] == row2[4]))

def main():
    count = 0;
    emails = {}
    num_rows = 0
    with open("emails.csv") as csvfile:
        reader = csv.reader(csvfile)
        prev_row = None
        for row in reader:
            if prev_row == None or new_row(prev_row, row):
                num_rows += 1
                prev_row = row
                source = row[0]
                target = row[1]
                date = parse(row[4])
                if source in emails:
                    if target in emails[source]:
                        emails[source][target].append(date)
                    else:
                        emails[source][target] = [date]
                else:
                    emails[source] = {target: [date]}

    print(num_rows)


if __name__ == "__main__":
    main()    
