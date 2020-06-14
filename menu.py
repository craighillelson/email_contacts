"""Provide user with a list of optios."""

import pyinputplus as pyip

options = {
    1: 'contacts.py',
    2: 'list_contacts.py',
    }


def switch_case(argument):
    """Switch case statement."""
    options
    return options.get(argument, 'nothing')


print('\n')
while True:
    print('Make a selection or press enter to quit')
    for num, option in options.items():
        print(num, option)
    selection = pyip.inputInt('> ', min=1, blank=True)
    if selection == '':
        break
    else:
        exec(open(switch_case(selection)).read())
