Instructions to Use the Phonebook Application
Run the Program: Execute the script in a Python environment. This will start the Phonebook application.

Menu Options: You’ll see a menu with several options. Enter the corresponding number to select an action.

Insert Contact (Option 1):

Choose this option to add a new contact.
Enter the contact’s name when prompted.
Enter the contact’s phone number.
The contact will be added to the phonebook.
Search Contact (Option 2):

Choose this option to find a contact.
Enter the name of the contact you want to search for.
If found, the application will display the contact’s name and phone number; otherwise, it will inform you that the contact was not found.
Display All Contacts (Option 3):

Select this option to see a list of all contacts stored in the phonebook.
If no contacts are available, it will inform you.
Delete Contact (Option 4):

Choose this option to remove a contact from the phonebook.
Enter the name of the contact you wish to delete.
If found, the contact will be removed, and you will receive confirmation. If not found, you’ll be notified.
Update Contact (Option 5):

Select this option to modify an existing contact.
Enter the name of the contact you want to update.
Provide the new contact name and phone number.
The contact will be updated if found; otherwise, you will be notified of the failure.
Sort Contacts (Option 6):

Choose this option to sort the contacts alphabetically by name.
The application will confirm that the contacts have been sorted.
Analyze Search Efficiency (Option 7):

This option provides information about the search time complexity, which is O(n) for this implementation.
Exit the Application (Option 8):

Select this option to close the phonebook application.
A confirmation message will appear, and the program will terminate.
Tips:
Ensure that you enter valid names and phone numbers when prompted.
The phonebook has a maximum capacity of 100 contacts. If you reach this limit, you won’t be able to add more contacts until some are deleted.# Phonebookapp

Explanation of Modules/Functions
InsertContact: Adds a new contact to the list.
SearchContact: Searches for a contact by name and returns it.
DisplayAllContacts: Prints all contacts in the list.
DeleteContact: Removes a contact by name.
UpdateContact: Modifies the details of an existing contact.
SortContacts: Sorts the contacts alphabetically by name (optional).
AnalyzeSearchEfficiency: Measures the time taken for a search operation.
