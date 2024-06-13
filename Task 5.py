# Task 5: Phone Book (using file handling)

# Importing essential libraries
import os

# Function to add a contact
def add_contact():
        name = input("Enter name: ")
        number = input("Enter number: ")
        with open("contacts.txt", "a") as file:
                file.write(name + " " + number + "\n")
        print("Contact added successfully!")

# Function to search a contact
def search_contact():
        name = input("Enter name: ")
        with open("contacts.txt", "r") as file:
                for line in file:
                        if name in line:
                                print(line)
                                return
                print("Contact not found!")

# Function to delete a contact
def delete_contact():
        name = input("Enter name: ")
        with open("contacts.txt", "r") as file:
                lines = file.readlines()
        with open("contacts.txt", "w") as file:
                for line in lines:
                        if name not in line:
                                file.write(line)
        print("Contact deleted successfully!")

# Function to display all contacts
def display_contacts():
        with open("contacts.txt", "r") as file:
                print(file.read())

# Main function
def main():
        if not os.path.exists("contacts.txt"):
                with open("contacts.txt", "w") as file:
                        pass
        while True:
                print("\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Display Contacts\n5. Exit")
                choice = input("Enter choice: ")
                if choice == "1":
                        add_contact()
                elif choice == "2":
                        search_contact()
                elif choice == "3":
                        delete_contact()
                elif choice == "4":
                        display_contacts()
                elif choice == "5":
                        break
                else:
                        print("Invalid choice!")
          
if __name__ == "__main__":
        main()