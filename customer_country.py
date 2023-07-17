#customer_country.py
#Purpose: Reads the file customers.csv and produces a new file containing the customer name and country they are from

import csv

#Open the csv file in read mode
infile = open('customers.csv','r')

#Open the file we are producing (the outfile) in write mode
outfile = open('customer_country.csv','w')

#Creates new csv object
reader = csv.reader(infile)
writer = csv.writer(outfile)

#Write reader row into customers.csv
writer.writerow(['First Name', 'Last Name', 'Country'])

#Skip fields header row
next(reader)

for record in reader:
    first_name = record[1]
    last_name = record[2]
    country = record[4]
    writer.writerow([first_name, last_name, country])

#Close files
infile.close()
outfile.close()
