import csv

with open('employee_file_3.csv', mode="w") as employee_file:
    fieldnames = ['name', 'dept', 'birth_month']
    employee_writer = csv.DictWriter(
        employee_file, fieldnames=fieldnames)

    employee_writer.writeheader()
    employee_writer.writerow({'name': 'John Smith', 'dept':'Accounting','birth_month': 'November'})
    employee_writer.writerow({'name':'Erica Meyers', 'dept':'IT', 'birth_month':'March'})
