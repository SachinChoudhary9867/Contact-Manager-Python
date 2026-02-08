# Contact Management System (Python)

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Contact List ---")
    for c in contacts:
        print("Name:", c["name"])
        print("Phone:", c["phone"])
        print("Email:", c["email"])
        print("-------------------")
    print()

def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    for c in contacts:
        if c["name"].lower() == search_name.lower():
            print("\nContact Found:")
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            found = True
            break

    if not found:
        print("Contact not found.\n")

while True:
    print("---- Contact Management System ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
