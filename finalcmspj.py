import re


email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
phone_number_pattern = r'^[0-9]{10}$'
address_book = {}

def add_contact():
    while True:
        try:
            email = input("Please enter an email: ")
            if not re.match(email_pattern, email):
                raise ValueError("Invalid email format. Please try again.")

            phone_number = input("Please enter a phone number: ")
            if not re.match(phone_number_pattern, phone_number):
                raise ValueError("Invalid phone number format. Please try again.")

            full_name = input("Please enter a full name: ")

            address_book[email] = {"email": email, "phone number": phone_number, "name": full_name}
            
            print("Contact added successfully!")
            print(address_book)
            break

        except ValueError as e:
            print(e)

def update_contact():
    email = input("Please enter the email of the contact to update: ")
    if email in address_book:
        phone_number = input("Please enter the new phone number: ")
        full_name = input("Please enter the new full name: ")
        new_email = input("Please enter the new email address (optional, press Enter to keep the same): ")

        updated_contact = {
            "email": new_email if new_email else email,
            "phone number": phone_number,
            "name": full_name
        }

        if new_email and new_email != email:
            del address_book[email]

        address_book[new_email] = updated_contact
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    email = input("Please enter the email of the contact to delete: ")
    if email in address_book:
        address_book.pop(email)
        print("A contact has been deleted")
    else:
        print("Email unavailabe")

def search_contacts():
    search_type = input("Please enter the search type (name, phone number, or email): ").lower()
    search = input(f"Please enter the {search_type} of the contact you want to search: ")

    found_contacts = []
    for contact_email, contact_info in address_book.items():
        if search.lower() in [contact_info['name'].lower(), contact_info['phone number'], contact_email]:
            found_contacts.append(contact_info)
    if found_contacts:
        for contact in found_contacts:
            print(f"Email: {contact['email']} \nPhone number: {contact['phone number']} \nName: {contact['name']}")
    else:
        print("Contact unavailable")

# Main loop
while True:
    cms = """Welcome to the Contact Management System!

Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Quit
"""
    print(cms)
    user_choice = int(input("What would you like to do? "))

    if user_choice == 1:
        add_contact()
    elif user_choice == 2:
        update_contact()
    elif user_choice == 3:
        delete_contact()
    elif user_choice == 4:
        search_contacts()
    elif user_choice == 5:
        if address_book == {}:
            print("No contacts available")
        else:
            print(address_book)
    elif user_choice == 6:
        def export_contacts():
            try:
                file_name = input("Please enter the file name to export contacts: ")
                with open(file_name, 'w') as file:
                    for email, contact_info in address_book.items():
                        file.write(f"Email: {contact_info['email']}\n")
                        file.write(f"Phone number: {contact_info['phone number']}\n")
                        file.write(f"Name: {contact_info['name']}\n\n")
                print("Contacts exported successfully!")
            except FileNotFoundError:
                print("File not found or cannot be created.")
            except PermissionError:
                print("Permission denied. You do not have sufficient permissions to write to this file.")
            except IOError as e:
                print(f"An error occurred while writing to the file: {e}")

        export_contacts()
    elif user_choice == 7:
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
