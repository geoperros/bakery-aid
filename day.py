import csv
from datetime import date
current_date = date.today()
name_del_out = '1'
csv_lines = dict()
def csv_file_creation():
    with open('customers.csv', 'a', newline ='') as new_file:
        fieldnames = ['name' , 'value']
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
        csv_writer.writeheader()

def customer_choice(name, value):
    with open('customers.csv', 'a', newline = '') as new_file:
        fieldnames = ['name' , 'value']
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
        csv_writer.writerow({'name': name,'value':value})

def customer_del(name_del_inp,name_del_out):
    with open('customers.csv', 'r',newline='') as new_file:
        csv_reader = csv.DictReader(new_file)
        for row in csv_reader:
            if row['name'] not in name_del_inp:
                csv_lines.append(row['name'],row['value'])

    with open('customers.csv', 'a', newline='') as new_file_w:
        fieldnames = ['name' , 'value']
        csv_writer = csv.DictWriter(new_file_w, fieldnames=fieldnames)
        csv_writer.writeheader
        csv_writer.writerows(csv_lines)
            
while True:
    choice = input(' "1" Καταχώρηση πελάτη και είδους. "2" Διαγραφή πελάτη "3" Δημειουργεία αρχείου "4" Έξοδος : ')
    if choice == '1':
        name = input('Όνομα πελάτη :')
        value = input('Είδος :')
        customer_choice(name,value)
    elif choice == '2':
        name_del_inp = input('Πελάτης προς διαγραφή : ')
        customer_del(name_del_inp,name_del_out)

    elif choice == '3':
        csv_file_creation()

    elif choice == '4':
        break
