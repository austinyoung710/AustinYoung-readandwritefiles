import csv
#reads the file customers.csv and produces a new file customer_country.csv containing the customer name and country they are from
infile = open('customers.csv', 'r')
csvfile = csv.reader(infile)
next(csvfile)

customerNum = 0
outfile = open('customer_country.csv', 'w') 
outfile.write("Full Name,Country\n")

#use the write() method to write the customer name and country they are from to the file
for record in csvfile:
    outfile = open('customer_country.csv', 'a')
    fullname = record[1] + ' ' + record[2]
    country = record[4]
    outfile.write(f'{fullname},{country}\n')
    customerNum += 1
print(f'Total number of customers: {customerNum}')


    

