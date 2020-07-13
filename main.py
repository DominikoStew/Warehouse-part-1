"""
    Warehouse program
    functionality:
        - Repeated menu
        1: Register items to a catalog
            id (auto generated)
            title (str)
            category (str)
            price (float)
            stock (int)

        2: List the items on the catalog
"""

from menu import clear, print_menu, print_header
from item import Item

# global variables
catalog = []  # list

# functions


def register_item():
    print_header('Register new Item')

    try:
        title = input("Item Title:  ")
        cat = input("Item Category: ")
        price = float(input("Item Price: "))
        stock = int(input("Items in Stock: "))

        # create an instance of Item (an object)
        new_item = Item(1, title, cat, price, stock)
        catalog.append(new_item)

        print("Item created ")

    except ValueError:
        print("** Error: incorrect value, try again")
    except:
        print("** Error, try again")


def display_catalog():
    print_header("Items in your catalog")

    for item in catalog:
        print(str(item.id).rjust(2)
              + " | " + item.title.ljust(25)
              + " | " + item.category.ljust(10)
              + " | " + str(item.price).rjust(15)
              + " | " + str(item.stock).rjust(5))
        print('-' * 75)


# instuctions

opc = ''
while(opc is not 'x'):
    clear()
    print_menu()

    opc = input('Please select an option: ')

    if(opc == '1'):
        register_item()
    elif(opc is '2'):
        display_catalog()

    input('Press Enter to continue')
