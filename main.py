
import csv
import time
from datetime import date
current_date = date.today()
current_term = ''

def new_term(term_name):
    with open(term_name, 'a') as new_file:
        fieldnames = ['date', 'item', 'production','usage']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writeheader()

def csv_log(current_date, current_item, current_production, current_usage, current_term):
    with open(current_term, 'a', newline = '') as new_file:
        fieldnames = ['date', 'item', 'production','usage']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writerow({'date': current_date, 'item': current_item, 'production' : current_production , 'usage' : current_usage})

def usr_input():
    if current_term == '':
        pass
    else:
        current_item = input('Επιλογή είδους :')
        current_production = input('Σημερινή παραγωγή :')
        current_usage = input('Σημερινή κατανάλωση :')

    csv_log(current_date, current_item, current_production, current_usage, current_term)



while True:
    choice = input('Επιλογή λειτουργίας, "1" για εισαγωγή τερματικού, "2" για λειτουργία καταγραφής, επιλογή τερματικού για καταγραφή "3", Έξοδος "4":')
    if choice == '1':
        term_name = input('Εισαγωγή ονοματός αποθήκης :')
        term_name = term_name + ".csv"
        new_term(term_name)
    elif choice == '2':
        usr_input()
    elif choice == '3':
        current_term = input('Επιλογή αποθήκης :')
        current_term = current_term + ".csv"
    elif choice == "4":
        break




