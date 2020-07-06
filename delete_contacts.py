"""
Import a csv, present user with options to remove. Write the results to
contacts.csv.
"""

import functions

original_contacts = functions.open_csv_pop_lst_namedtuple()
original_contacts_numbered = functions.number_original_contacts(original_contacts)
nums = functions.get_list_of_keys(original_contacts_numbered)
functions.output_options(original_contacts_numbered)
contacts_to_skip = functions.prompt_user_to_remove(nums)
remaining_members = functions.output_remaining_contacts(original_contacts_numbered, contacts_to_skip)
functions.write_lst_to_csv(remaining_members)
