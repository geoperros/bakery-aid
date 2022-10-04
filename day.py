import csv
from datetime import date
current_date = date.today()
current_file_name = ''
def csv_log_day(current_date, current_name, current_product, current_value, current_file_name):
    with open(current_file_name, 'a', newline = '') as new_file:
        fieldnames = ['ΗΜ/ΝΙΑ', 'ΟΝΟΜΑ', 'ΕΙΔΟΣ','ΠΟΣΟΤΗΤΑ']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writerow({'ΗΜ/ΝΙΑ': current_date, 'ΟΝΟΜΑ': current_name, 'ΕΙΔΟΣ' : current_product , 'ΠΟΣΟΤΗΤΑ' : current_value})

def customer_choice(name, value):
    with open('customers.csv', 'a', newline = '') as new_file:
        fieldnames = ['name' , 'value']
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
        csv_writer.writerow({'name': name,'value':value})

while True:
    choice = input('"1" Επιλογη ονόματος αρχείου. "2" Καταχώρηση πελάτη και είδους. "3" Έξοδος: ')
    if choice == '1':
        current_file_name = input('Εισάγετε όνομα αρχείου : ')
    elif choice == '2':
        name = input('Όνομα πελάτη :')
        value = input('Είδος :')
        customer_choice(name,value)

        




    elif choice == "3":
        break
