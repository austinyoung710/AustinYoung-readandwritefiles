import csv

infile = open('employee_data.csv', 'r')
csvfile = csv.reader(infile)

next(csvfile)

for record in csvfile:
    name = record[1]
    salary = float(record[3])
    bonus_percentage = float(record[7])
    bonus = salary * bonus_percentage
    pay = float(salary) + float(bonus)
    print(f"Name: {name}\nSalary: {salary}\nBonus: {bonus}\nPay: {pay}\n")