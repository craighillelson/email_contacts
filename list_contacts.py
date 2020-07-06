"""List contacts."""

import functions

contacts = functions.open_csv_pop_lst_namedtuple()
functions.output_contacts(contacts)
