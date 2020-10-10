"""Create a timestamped backup of contacts.csv."""

from functions import backup_contacts, create_timestamped_filename

backup_filename = create_timestamped_filename()
DIRECTORY = "backup"
path = DIRECTORY + "/" + backup_filename
backup_contacts(path)
print(f"\ncontacts.csv was copied to {path}")
