"""
Open a csv and populate a dictionary with its contents. Prompt the user to
add members.
"""

import functions

contacts = functions.open_csv_pop_lst_namedtuple()
if contacts:
    domain = functions.get_domain('email', contacts)
    domain_confirmed = functions.prompt_user_for_domain(domain)
    functions.add_user_input_to_csv(domain, contacts)
else:
    add_contacts = pyip.inputYesNo('\nThere are no entries in the csv. Would you like to add contacts?\n> ')
    if add_contacts == 'yes':
        domain = input('What is your domain?\n> ')
        functions.add_user_input_to_csv(domain, contacts)
    else:
        pass
