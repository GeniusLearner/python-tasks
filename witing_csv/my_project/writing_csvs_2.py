import csv

with open('employee_file_2.csv', mode="w") as employee_file:
    employee_writer = csv.writer(
        employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE, escapechar='|')

    employee_writer.writerow(['John, Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica, Meyers', 'IT', 'March'])
