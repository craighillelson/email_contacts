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


def backup_contacts(destination):
    """Make a copy of contacts."""
    import shutil

    shutil.copy("contacts.csv", destination)


def create_timestamped_filename():
    """Create a filename created including a timestamp."""
    from datetime import datetime

    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H:%M:%S") + "_backup.csv"


def complete_setup(lst):
    """
    Tests to see if folders and files required to run the app. If required
    folders do not exist, create them.
    """
    import os
    from os import path

    print("\n")

    for folder in lst:
        if path.exists(folder):
            print(f"{folder} exists")
        else:
            os.mkdir(folder)
            print(f"{folder} was created successfully")

    print("\nSetup is complete.\n")


def get_domain(lst2):
    """Extract the domain from an email address."""
    first_email_address = lst2[0]
    return first_email_address.split("@")[1]


def get_list_of_keys(dct):
    """Return a list comprised of the keys of a dictionary."""
    return list(dct.keys())


def output_options(dct):
    """Present user with options."""
    print("\nContacts")
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
    print("\nremaining members")
    lst2 = []
    for num, email in dct.items():
        if num not in lst1:
            print(email)
            lst2.append(email)
    return lst2


def prompt_user(dct):
    """Prompt user for members to remove."""
    lst = []
    while True:
        print(f"\nEnter the number of corresponding members you'd like to "
              f"edit or nothing to quit.")
        response = pyip.inputInt("> ", max=len(dct), blank=True)
        if response == "":
            break
        else:
            edited_entry = input(f"Update {dct[response]}\n> ")
            dct[response] = edited_entry
            for num, email in dct.items():
                lst.append(email)

    return lst


def prompt_user_to_remove(a):
    """Prompt user for members to remove."""
    lst = []
    while True:
        print(f"\nEnter the number of corresponding members you'd like to "
              f"skip or enter nothing to stop.")
        response = pyip.inputInt("> ", max=len(a), blank=True)
        if response == "":
            break
        lst = lst + [response]

    return lst


def prompt_user_for_domain(domain):
    """
    After extracting the domain from an email address, prompt the user to
    add more email addresses for that domain or another.
    """
    while True:
        print(f"\nIs {domain} your domain (yes or no)?")
        answer = pyip.inputYesNo("> ")
        if answer != "yes":
            domain = input("What is your domain name?\n> ")
            break
        else:
            break

    return domain


def open_csv_pop_lst_namedtuple():
    """Populate a dictionary with the contents of a csv."""
    lst = []
    with open("contacts.csv") as f:
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
        print("\nContacts")
        for i, (email) in enumerate(lst, 1):
            print(f"{i}. {email}")
    else:
        print("contacts.csv is empty.\n")


def prompt_user_for_prefix(domain, email_addresses):
    """Prompt user for email prefixes."""
    lst = []
    while True:
        print("\nEnter the contact's name (or enter nothing to stop).")
        email_prefix = input("> ")
        email = email_prefix + "@" + domain
        if email not in email_addresses:
            if email_prefix == "":
                break
            lst = lst + [email]
        else:
            print(f"{email} is already in the list")

    return lst


def write_dct_to_csv(file, DCT, HEADERS):
    """Write dictionary to csv."""
    import csv

    with open(file, "w") as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["email,first_name,last_name"])
        for email, user_details in DCT.items():
            keys_values = (email, user_details)
            out_csv.writerow(keys_values)

    print(f"{file} exported successfully")


def write_lst_to_csv(contacts):
    """Write list to csv."""
    with open("contacts.csv", "w") as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["email"])
        for email in contacts:
            out_csv.writerow([email])

    print(f"\n'contacts.csv' exported successfully")
