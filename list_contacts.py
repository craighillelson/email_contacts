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
                              row.state]

    return dct


def output_contacts(dct):
    """
    If the contacts dictionary contains one or more records, loop through
    the dictionary and print each record. If there are no records, notify the
    user that the database is empty.
    """
    print('\n')
    if contacts:
        for i, (email, details) in enumerate(dct.items(), 1):
            print(i, email, *details)
    else:
        print('The database is empty.')
    print('\n')


contacts = open_csv_pop_dct_namedtuple()
output_contacts(contacts)
