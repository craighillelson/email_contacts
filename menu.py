"""Provide user with a list of options."""

import pyinputplus as pyip

options = {
    1: "add_contacts.py",
    2: "backup_contacts.py",
    3: "delete_contacts.py",
    4: "edit_contacts.py",
    5: "list_contacts.py",
    6: "search_contacts.py",
    7: "setup.py",
}


def switch_case(argument):
    """Switch case statement."""
    # options
    return options.get(argument, 'nothing')


while True:
    print("\nMake a selection or press enter to quit")
    for num, option in options.items():
        print(num, option)
    selection = pyip.inputInt("> ", min=1, max=len(options), blank=True)
    if selection != "":
        exec(open(switch_case(selection)).read())
    else:
        print("\nSession complete.\n")
        break
