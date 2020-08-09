"""Search contacts."""

from functions import open_csv_pop_lst_namedtuple

while True:
    contacts = open_csv_pop_lst_namedtuple()
    user_search = input("\nSearch for a contact\n> ")
    if user_search == "":
        break
    if user_search in contacts:
        print(f"{user_search} is listed in the contact database.")
    else:
        print(f"{user_search} is not listed in the contact database.")
