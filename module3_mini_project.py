

import re

def show_menu():
    print("/nWelcome to Contact Managment System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def validate_email(email):
    pattern =r'^[a-zA-Z0-9._%=-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email)

def validate_phone(phone):
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.match(pattern, phone)

def add_contact(contacts):
    identifier = input("Enter the unique identifier (phone number or email): ")
    if not validate_email(identifier) and not validate_phone(identifier):
        print("invalid identifier format.")
        return
    
    name = input("Enter name: ")
    phone = input("Enter pnone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information (address, notes): ")

    contacts[identifier] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Additional Information': additional_info
    }
    print("Contact added successfully!")

def edit_contact(contacts):
    identifier = input("Enter the unique identifier of the contact to edit: ")
    if identifier in contacts:
        name = input("Enter new name (leave blank to keep current): ")
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")
        additional_info = input("Enter new additional information (leave blank to keep current): ")

        if name:
            contacts[identifier]['Name'] = name
        if phone:
            contacts[identifier]['Phone'] = phone
        if email:
            contacts[identifier]['Email'] = email
        if additional_info:
            contacts[identifier]['Additional Information'] = additional_info

        print("Contact updated successfully! ")
    else:
        print("Contact not found. ")

def delete_contact(contacts):
    identifier = input("Enter the unique identifier of the contact to delete: ")
    if identifier in contacts:
        del contacts[identifier]
        print("Contacts deleted successfully! ")
    else:
        print("Contact not found. ")

def search_contact(contacts):
    identifier = input("Enter the unique identifier of the contact to sesrch: ")
    if identifier in contacts:
        print(contacts[identifier])
    else:
        print("Contact not found.")

def display_all_contacts(contacts):
    if contacts:
        for identifier, details in contacts.items():
            print(f"\nIDENTIFIER: {identifier} ")
            for key, value in details.items():
                print(f"{key}: {value} ")

    else:
        print("No contacts to display. ")

def export_contacts(contacts):
    file_name = input("Enter the name of the file to export contacts: ")
    with open(file_name, 'w') as f:
        for identifier, details in contacts.items():
            f.write(f"{identifier},{details['Name']}, {details['Phone']}, {details['Email']} , {details['Additional Information']}\n")
    print("Contacts exported successfully! ")

def import_contacts(contacts):
    file_name = input("Enter the name of the file to import contacts: ")
    try:
        with open(file_name, 'r') as f:
            for line in f:
                identifier, name, phone, email, additional_info = line.strip().split(',')
                contacts[identifier] = {
                    'Name': name,
                    'Phone': phone,
                    'Email': email,
                    'Additional Information': additional_info
                }
        print("Contacts imported successfully! ")
    except FileNotFoundError:
        print("File not found. ")

def main():
    contacts = {}
    while True:
        show_menu()
        choice = input("Select an option: ")

        try:
            if choice == '1':
                add_contact(contacts)
            elif choice == '2':
                edit_contact(contacts)
            elif choice == '3':
                delete_contact(contacts)
            elif choice == '4':
                search_contact(contacts)
            elif choice == '5':
                display_all_contacts(contacts)
            elif choice == '6':
                export_contacts(contacts)
            elif choice == '7':
                import_contacts(contacts)
            elif choice == '8':
                print("Goodbye! ")
                break
            else:
                print("Invalid option. try again. ")
        except Exception as e:
            print(f"An error occured: {e} ")

if __name__ == "__main__":
    main()

