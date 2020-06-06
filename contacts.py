"""Contact list application."""

import csv
import pyinputplus as pyip
import re
from collections import namedtuple


def open_csv_pop_dct_namedtuple_print_dct(file_name):
    """Open a csv, populate and print the contents of a dictionary."""
    dct = {}
    with open(file_name) as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            dct[row.email] = [row.first_name, row.last_name, row.phone_number]

    for key in dct.keys():
        print(key)

    return dct


def prompt_user(field):
    """Prompt user for contact details."""
    print(field)
    attribute = input('> ')
    return attribute


def phone_number_regex(phone_number):
    """Test to ensure phone_number is entered in xxx-xxx-xxxx format."""
    regex = '\d{3}-\d{3}-\d{4}'
    if re.search(regex, phone_number):
        return True
    else:
        return False


def enter_contact_details():
    """Add contact details."""
    dct = {}
    while True:
        print('\nEnter contact details or enter to stop.')
        print('Email')
        email = pyip.inputEmail('> ')
        if email in contacts:
            print('A record with this email address already exists.')
        else:
            first_name = prompt_user('First Name')
            last_name = prompt_user('Last Name')
            phone_number = prompt_user('Phone Number (xxx-xxx-xxxx)')
            if phone_number_regex(phone_number) != True:
                print('\nPlease enter a phone number in xxx-xxx-xxxx format')
                phone_number = prompt_user('Phone Number')
            else:
                pass
            dct[email] = [first_name, last_name, phone_number]
        print('\nenter another contact (yes or no)?')
        another = pyip.inputYesNo('> ')
        if another != 'yes':
            break
        else:
            pass

    return dct


def merge_dictionaries():
    """Merge dictionaries."""
    return {**contacts, **contacts_to_add}


def write_dct_to_csv(file, DCT):
    """Write dictionary to csv."""
    with open(file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(['email', 'first_name', 'last_name', 'phone_number'])
        for yankee, details in DCT.items():
            keys_values = (yankee, *details)
            out_csv.writerow(keys_values)


def update_user(user_update):
    """Output the entries that have been added to the database."""
    print(user_update)
    for yankee, details in contacts_to_add.items():
        print(f'email: {yankee}')
        print(f'name: {details[0]} {details[1]}')
        print(f'phone number: {details[2]}\n')


contacts = open_csv_pop_dct_namedtuple_print_dct('contacts.csv')
contacts_to_add = enter_contact_details()
if contacts_to_add:
    contacts_plus_contacts_to_add = merge_dictionaries()
    write_dct_to_csv('contacts.csv', contacts_plus_contacts_to_add)
    if len(contacts_to_add) > 1:
        update_user('\nThe following records were added to the database.\n')
    else:
        update_user('\nThe following record was added to the database.\n')
else:
    pass
