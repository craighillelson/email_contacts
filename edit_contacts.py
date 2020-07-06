"""
Import a csv, present user with options to skip.
Write the results to a csv.
"""

import functions

original_contacts = functions.open_csv_pop_lst_namedtuple()
original_contacts_numbered = functions.number_original_contacts(original_contacts)
nums = functions.get_list_of_keys(original_contacts_numbered)
functions.output_options(original_contacts_numbered)
remaining_contacts = functions.prompt_user(original_contacts_numbered)
functions.write_lst_to_csv(remaining_contacts)
