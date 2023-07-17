#employee_bonus.py
#Reads the EmployeePay.csv file and prints out details of each employee

import csv

infile = open('EmployeePay.csv','r')

reader = csv.reader(infile)

next(reader)

for record in reader:
    ID = record[0]
    first_name = record[1]
    last_name = record[2]
    salary = record[3]
    bonus = record[4]
    print()
    print('Employee Details:')
    print(f'ID: {ID}')
    print(f'First Name: {first_name}')
    print(f'Last Name: {last_name}')
    print(f'Salary: {salary}')
    print(f'Bonus: {bonus}')
    print()
    input('Press ENTER to view the next record...')

infile.close()
