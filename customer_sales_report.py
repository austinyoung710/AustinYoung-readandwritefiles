import csv

infile = open('sales.csv', 'r')
csvfile = csv.reader(infile)
next(csvfile)
previous_customerID = ''

outfile = open('salesreport.csv', 'w') 
outfile.write("Customer ID,Total\n")

for record in csvfile:
    outfile = open('salesreport.csv', 'a')
    customerID = record[0]
    total = float(record[3]) + float(record[4]) + float(record[5])
    if customerID != previous_customerID:
        if previous_customerID != '':
            outfile.write(f'{previous_customerID},{customer_total:.2f}\n')
        customer_total = total
        previous_customerID = customerID
    else:
        customer_total += total

outfile.write(f'{customerID},{total:.2f}\n')