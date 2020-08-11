"""
Import a csv, present user with options to remove any of the contacts. Write
the results to contacts.csv.
"""

from functions import (open_csv_pop_lst_namedtuple,
                       number_original_contacts,
                       get_list_of_keys,
                       output_options,
                       prompt_user_to_remove,
                       output_remaining_contacts,
                       write_lst_to_csv,)

original_contacts = open_csv_pop_lst_namedtuple()
original_contacts_numbered = number_original_contacts(original_contacts)
nums = get_list_of_keys(original_contacts_numbered)
output_options(original_contacts_numbered)
contacts_to_skip = prompt_user_to_remove(nums)
remaining_members = output_remaining_contacts(original_contacts_numbered,
                                              contacts_to_skip)
write_lst_to_csv(remaining_members)
