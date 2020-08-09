"""
Import a csv, present user with options to skip.
Write the results to a csv.
"""

from functions import (open_csv_pop_lst_namedtuple,
                       number_original_contacts,
                       get_list_of_keys,
                       output_options,
                       prompt_user,
                       write_lst_to_csv,)

original_contacts = open_csv_pop_lst_namedtuple()
original_contacts_numbered = number_original_contacts(original_contacts)

nums = get_list_of_keys(original_contacts_numbered)
output_options(original_contacts_numbered)

updated_contacts = prompt_user(original_contacts_numbered)
if updated_contacts:
    write_lst_to_csv(updated_contacts)
else:
    print("no changes made")
