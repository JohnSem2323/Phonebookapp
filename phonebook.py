class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Phonebook:
    def __init__(self, max_size=100):
        self.contacts = []
        self.max_size = max_size

    def insert_contact(self, contact):
        if len(self.contacts) < self.max_size:
            self.contacts.append(contact)
            print(f"Contact '{contact.name}' added.")
        else:
            print("Phonebook is full.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print(f"Contact '{name}' deleted.")
                return True
        print(f"Contact '{name}' not found.")
        return False

    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts[i] = new_contact
                print(f"Contact '{name}' updated to '{new_contact.name}'.")
                return True
        print(f"Contact '{name}' not found.")
        return False

    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: contact.name)
        print("Contacts sorted.")

    def analyze_search_efficiency(self):
        print("Search Time Complexity: O(n)")

def main():
    phonebook = Phonebook()

    while True:
        print("\nPhonebook Menu:")
        print("1. Insert Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Sort Contacts")
        print("7. Analyze Search Efficiency")
        print("8. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            phonebook.insert_contact(Contact(name, phone))

        elif choice == '2':
            name = input("Enter contact name to search: ")
            contact = phonebook.search_contact(name)
            if contact:
                print(f"Found: Name: {contact.name}, Phone: {contact.phone}")
            else:
                print("Contact not found.")

        elif choice == '3':
            phonebook.display_all_contacts()

        elif choice == '4':
            name = input("Enter contact name to delete: ")
            phonebook.delete_contact(name)

        elif choice == '5':
            name = input("Enter contact name to update: ")
            new_name = input("Enter new contact name: ")
            new_phone = input("Enter new contact phone: ")
            success = phonebook.update_contact(name, Contact(new_name, new_phone))
            if not success:
                print("Update failed.")

        elif choice == '6':
            phonebook.sort_contacts()

        elif choice == '7':
            phonebook.analyze_search_efficiency()

        elif choice == '8':
            print("Exiting phonebook application.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

