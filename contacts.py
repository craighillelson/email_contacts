"""
Prompt user to enter contact details where email addresses are keys and contact
details are values. Disallow duplicate entries by checking user input against
email addresses already in the database. Prompt user to confirm each entry
before saving to the database.
"""

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
            dct[row.email] = [row.first_name, row.last_name, row.phone_number,
                              row.city, row.state, row.zip_code, row.active]

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
        print('\nEnter contact details or enter to quit.')
        print('Email')
        email = pyip.inputEmail('> ', blank=True)
        if email == '':
            break
        elif email in contacts:
            print('A record with this email address already exists.')
        else:
            first_name = prompt_user('First Name') # capitalize first letter
            last_name = prompt_user('Last Name') # capitalize first letter
            phone_number = prompt_user('Phone Number (xxx-xxx-xxxx)')
            if phone_number_regex(phone_number) != True:
                print('\nPlease enter a phone number in xxx-xxx-xxxx format')
                phone_number = prompt_user('Phone Number')
            else:
                print('city')
                city = input('> ')
                print('state')
                state = pyip.inputUSState('> ')
                print('zip code')
                zip_code = input('> ')
                print('active (yes or no)')
                active = pyip.inputYesNo('> ')
            dct[email] = [first_name, last_name, phone_number, city, state,
                          zip_code, active]

    return dct


def merge_dictionaries():
    """Merge dictionaries."""
    return {**contacts, **contacts_to_add}


def write_dct_to_csv(file, DCT):
    """Write dictionary to csv."""
    with open(file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(['email', 'first_name', 'last_name', 'phone_number',
                         'city', 'state', 'zip_code', 'active'])
        for email, details in DCT.items():
            keys_values = (email, *details)
            out_csv.writerow(keys_values)


def print_contact_details():
    """Print contact details."""
    for email, details in contacts_to_add.items():
        print(f'email: {email}')
        print(f'name: {details[0]} {details[1]}')
        print(f'phone number: {details[2]}')
        print(f'city: {details[3]}')
        print(f'state: {details[4]}')
        print(f'zip code: {details[5]}')
        print(f'active: {details[6]}\n')


def update_user(record_or_records):
    """
    Confirm for the user that their entry or entries were added to the database.
    Output the entries that have been added to the database.
    """
    print(f'\nThe following {record_or_records} added to the database.\n')
    print_contact_details()


contacts = open_csv_pop_dct_namedtuple_print_dct('contacts.csv')
contacts_to_add = enter_contact_details()
if contacts_to_add:
    contacts_plus_contacts_to_add = merge_dictionaries()
    write_dct_to_csv('contacts.csv', contacts_plus_contacts_to_add)
    if len(contacts_to_add) > 1:
        update_user('records were')
    else:
        update_user('record was')
else:
    pass
