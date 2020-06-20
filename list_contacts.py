"""List contacts."""

import csv
from collections import namedtuple


def open_csv_pop_dct_namedtuple():
    """Populate a dictionary with the contents of a csv."""
    dct = {}
    with open('contacts.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            dct[row.email] = [row.first_name, row.last_name, row.phone_number,
                              row.city, row.state, row.zip_code, row.active]

    return dct


def output_contacts(dct):
    """
    If the contacts dictionary contains one or more records, loop through
    the dictionary and print each record. If there are no records, notify the
    user that the database is empty.
    """
    if contacts:
        print('\n')
        for i, (email, details) in enumerate(dct.items(), 1):
            print(f'record: {i}')
            print(f'email: {email}')
            print(f'name: {details[0]} {details[1]}')
            print(f'phone number: {details[2]}')
            print(f'city: {details[3]}')
            print(f'state: {details[4]}')
            print(f'zip code: {details[5]}')
            print(f'active: {details[6]}\n')
    else:
        print('The database is empty.')
    print('\n')


contacts = open_csv_pop_dct_namedtuple()
output_contacts(contacts)
