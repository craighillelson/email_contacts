"""Functions."""

import csv
import pyinputplus as pyip
from collections import namedtuple


def add_user_input_to_csv(user_domain, lst):
    """
    Prompt user for input and add each entry to a list. Concatenate resulting
    list and pre-existing list. Write the concatenated list containing all
    contacts to a csv.
    """
    contacts_to_add = prompt_user_for_prefix(user_domain, lst)
    all_contacts = lst + contacts_to_add
    write_lst_to_csv(all_contacts)


def get_domain(lst2):
    """Extract the domain from an email address."""
    lst1 = lst2[0]
    return lst1.split('@')[1]


def get_list_of_keys(dct):
    """Return a list comprised of the keys of a dictionary."""
    return list(dct.keys())


def output_options(dct):
    """Present user with options."""
    print('\nContacts')
    for num, email in dct.items():
        print(num, email)


def number_original_contacts(lst):
    """
    After importing a list of members, number them and populate a dictionary
    with each member's assigned number as the key and their name as the value.
    """
    dct = {}
    for num, email in enumerate(lst, 1):
        dct[num] = email
    return dct


def output_remaining_contacts(dct, lst1):
    """
    Filter the list of original members, excluding the members the user chose to
    skip. Populate a list with the remaining members.
    """
    print('\nremaining members')
    lst2 = []
    for k, v in dct.items():
        if k not in lst1:
            print(v)
            lst2.append(v)
    return lst2
    print_return('\n')


def prompt_user(dct):
    """Prompt user for members to remove."""
    lst = []
    while True:
        print(f'\nEnter the number of corresponding members you\'d like to '
              f'edit or nothing to quit.')
        response = pyip.inputInt('> ', max=len(dct), blank=True)
        if response == '':
            break
        else:
            edited_entry = input(f'Update {dct[response]}\n> ')
            dct[response] = edited_entry
            for num, email in dct.items():
                lst.append(email)
    return lst


def prompt_user_to_remove(a):
    """Prompt user for members to remove."""
    lst = []
    while True:
        print(f'\nEnter the number of corresponding members you\'d like to '
              f'skip or enter nothing to stop.')
        response = pyip.inputInt('> ', max=len(a), blank=True)
        if response == '':
            break
        lst = lst + [response]

    return lst


def prompt_user_for_domain(a):
    """
    After extracting the domain from an email address, prompt the user to
    add more email addresses for that domain or another.
    """
    while True:
        print(f'\nIs {a} your domain (yes or no)?')
        answer = pyip.inputYesNo('> ')
        if answer != 'yes':
            a = input('What is your domain name?\n> ')
            break
        else:
            break

    return a


def open_csv_pop_lst_namedtuple():
    """Populate a dictionary with the contents of a csv."""
    lst = []
    with open('contacts.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            lst.append(row.email)

    return lst


def output_contacts(lst):
    """
    If the contacts dictionary contains one or more records, loop through
    the dictionary and print each record. If there are no records, notify the
    user that the database is empty.
    """
    if lst:
        print('\nContacts')
        for i, (email) in enumerate(lst, 1):
            print(f'{i}. {email}')
    else:
        print('The database is empty.\n')


def prompt_user_for_prefix(a, b):
    """Prompt user for email prefixes."""
    lst = []
    while True:
        print('\nEnter the contact\'s name (or enter nothing to stop).')
        email_prefix = input('> ')
        email = email_prefix + '@' + a
        if email not in b:
            if email_prefix == '':
                break
            lst = lst + [email]
        else:
            print(f'{email} is already in the list')

    return lst


def write_lst_to_csv(LST):
    """Write list to csv."""
    with open('contacts.csv', 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(['email'])
        for i in LST:
            out_csv.writerow([i])

    print(f'\n"contacts.csv" exported successfully')
