"""
Open a csv and populate a dictionary with its contents. Prompt the user to
add members.
"""

import pyinputplus as pyip
from functions import (open_csv_pop_lst_namedtuple,
                       get_domain,
                       prompt_user_for_domain,
                       add_user_input_to_csv,)

contacts = open_csv_pop_lst_namedtuple()
if contacts:
    domain = get_domain(contacts)
    domain_confirmed = prompt_user_for_domain(domain)
    add_user_input_to_csv(domain, contacts)
else:
    add_contacts = pyip.inputYesNo("\nThere are no entries in the csv. "
                                   "Would you like to add contacts (yes or no)?"
                                   "\n> ")
    if add_contacts == "yes":
        domain = input("\nWhat is your domain?\n> ")
        add_user_input_to_csv(domain, contacts)
    else:
        pass
