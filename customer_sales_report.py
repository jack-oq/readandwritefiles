#customer_sales_report.py
#Purpose: reads the sales.csv file and creates a new file with the customer ID and calculated total (as shown here salesreport.csv)

import csv

#Open the csv file in read mode
infile = open('sales.csv','r')

#Open the file we are producing (the outfile) in write mode
outfile = open('salesreport.csv','w')

#Creates new csv object
reader = csv.reader(infile)
writer = csv.writer(outfile)

#Write reader row into customers.csv
writer.writerow(['Customer', 'Total'])

#Skip fields header row
next(reader)

for record in reader:
    ID = record[0]
    subtotal = float(record[3])
    tax = float(record[4])
    freight = float(record[5])
    total = subtotal + tax + freight
    round(total, 2)
    writer.writerow([ID, round(total,2)])

#Close files
infile.close()
outfile.close()
