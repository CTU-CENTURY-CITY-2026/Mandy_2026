from menu import display_menu
from crud_operations import *

while True:
    display_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        view_products()
    elif choice == "2":
        add_product()
    elif choice == "3":
        update_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")