# *******         TASK 32             *******
# *******     Compulsory Task         *******
# *******      inventory.py           *******
# *******      Capstone IV            *******
# ---------------  xxx -----------------------


# importing tabulate to display data in table form
from tabulate import tabulate

'''
This program is used to manage the Nike warehouse to optimise delivery time and for improved organisation. It allows
the user read shoe inventory from the text file, allow user to capture data about shoe, view data, restock the low 
quantity shoe, search for shoe and find the shoe with the highest quantity. 
'''

# Below is the class definition for class Shoe which has attributes that provide information about a shoe and methods
# to access those attributes


class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):

        return self.cost

    def get_quantity(self):

        return self.quantity

    def __str__(self):

        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


# The list below will be used to store a list of objects of shoes.
shoe_list = []

# ==========Functions outside the class==============

# The function below reads data from textfile inventory.txt and uses it to create an object of class shoe. The object
# is then added to a list called shoe_list.


def read_shoes_data():
    count = 0

    # Resetting the shoe_list every time the user enters 'r' to read from the inventory text file to prevent
    # adding duplicate data again to the list
    global shoe_list
    shoe_list = []

    while True:
        try:

            inventory_file = open('inventory.txt', 'r+', encoding='utf-8')
            break
        except FileNotFoundError as error:
            print("File does not exist")
            print(error)

    # Reading each and every line of the text file except the first line
    for line in inventory_file:
        if count == 0:
            count += 1
            continue

        # stripping and splitting each line of text file to get all information about the shoe
        split_line = line.strip('\n').split(',')

        # Creating an object of class Shoe by passing the attributes of each shoe from the text file.
        each_shoe = Shoe(split_line[0], split_line[1], split_line[2], int(split_line[3]), int(split_line[4]))

        # Finally adding the object to a list shoe_list
        shoe_list.append(each_shoe)

        count += 1

    inventory_file.close()

# The function below captures the input from the user about the shoe. If the shoe data already exist(ie same country,
# code, product and cost) then only the shoe quantity gets updated. However, if it is completely new shoe then we
# create a new object of Shoe class and add it to the shoe_list. The updated shoe_list is then written back into an
# inventory.txt file to update it


def capture_shoes():

    # Boolean variable to check if shoe data inputted has no duplicate record in shoe_list before it get appended or
    # else only the quantity gets updated
    add_shoe_object = True

    # Getting input from the user
    country = input("Enter Country's Name: ").title()
    code = input("Enter the Product's code: ").upper()
    product = input("Enter Product's Name: ").title()

    # Preventing invalid input from the user
    while True:
        try:
            cost = int(input("Enter the product's price: "))
            quantity = int(input("Enter the product's quantity: "))
            break
        except ValueError as error:
            print("Enter a valid integer value")
            print(error)

    # looping through a shoe list to see if the shoe data inputted details already exist.
    for shoe in shoe_list:

        # If the shoe data has same country,code,product and cost just update the quantity inside the shoe_list
        if shoe.country == country and shoe.code == code and shoe.product == product and shoe.get_cost() == cost:
            shoe.quantity += quantity
            add_shoe_object = False     # Don't append the new shoe data

    if add_shoe_object:

        # If shoe data is completely different, create a new object of class Shoe by passing the data captured above
        new_shoe = Shoe(country, code, product, cost, quantity)

        # Adding a shoe to a shoe_list
        shoe_list.append(new_shoe)
        print("New shoe added to shoe_list.")

    # Writing the updated shoe_list back to an inventory.txt file to update it.
    inventory_file = open('inventory.txt', 'r+', encoding='utf-8')
    inventory_file.write("Country,Code,Product,Cost,Quantity\n")
    for shoe in shoe_list:
        inventory_file.write(shoe.country + ',' + shoe.code + ',' + shoe.product + ',' + str(shoe.get_cost()) + ',' + str(shoe.get_quantity()) + '\n')
    print("shoe_list updated")
    print("Inventory File is updated.")
    inventory_file.close()


# The function below displays the details of each shoe in table format. It gets the string representation of shoe object
# using __str__ function implementation and split them into a list which is then added to shoe_data_list to
# be displayed in the form of table.


def view_all():

    # Defining and initializing the list variable called shoe_data_list to store shoe object's string after splitting
    shoe_data_list = [['Country', 'Code', 'Product', 'Cost', 'Quantity']]

    for shoe in shoe_list:
        # Each shoe object's string representation is type cast to string and is split and appended to shoe_data_list
        shoe_data_list.append(str(shoe).split(', '))

    print(tabulate(shoe_data_list))  # Finally printing in a tabular form


# The function below finds the shoe with the lowest quantity and ask the user to add the quantity and update them.

def re_stock():
    # The update variable is used to determine whether the user has re-stock the inventory. If it has been
    # restocked then update is set to True and file will be written
    update = False
    # Creating string to store each and every object of the shoe_list to modify and update the inventory.txt file
    content = 'Country,Code,Product,Cost,Quantity\n'

    # looping through a shoe list
    for shoe in shoe_list:

        # Checking if the shoe quantity is less than 10 and asking user to if they want to refill
        if shoe.get_quantity() < 10:
            print(f"{shoe.product} quantity is {shoe.get_quantity()} and needs restocking ")

            while True:
                choice = input("Do you want to refill. Press 'y' or 'n' ")
                if choice == 'y':
                    while True:
                        try:

                            # Adding the quantity inputted by user to already existing quantity of shoe in the shoe_list
                            # So list get updated here.
                            shoe.quantity += int(input("Enter the quantity to refill: "))
                            print("Shoe List Updated.")

                            update = True  # The quantity must now be updated to a file
                            break

                        except ValueError:
                            print("Enter valid integer number")

                    # Finally adding the updated quantity of shoe along with its other details to a string
                    content += shoe.country + ',' + shoe.code + ',' + shoe.product + ',' + str(shoe.get_cost()) + ',' + str(shoe.get_quantity()) + "\n"
                    break  # Breaking the outer while loop to check if next shoe object need restocking.

                elif choice == 'n':
                    print("No item was restocked.")
                    content += shoe.country + ',' + shoe.code + ',' + shoe.product + ',' + str(shoe.get_cost()) + ',' + str(shoe.get_quantity()) + "\n"
                    break

                else:
                    print("Enter a valid either 'y' or 'n' ")

        # If quantity is ok or no top up is done, just copy the details in the content string.
        else:
            content += shoe.country + ',' + shoe.code + ',' + shoe.product + ',' + str(shoe.get_cost()) + ',' + str(shoe.get_quantity()) + '\n'

    # Finally updating the inventory file if the quantity has been restocked.
    if update:
        with open('inventory.txt', 'w', encoding='utf-8') as inventory_file:
            inventory_file.write(content)
        print("Inventory file has been updated")
    else:
        print("No item was needed to restock!")


# The function below uses shoe code to search for the shoe in the list and returns the string representation of object
# associated with the shoe code

def search_shoe():

    shoe_code = input("Enter the shoe code to find:  ").upper()

    for shoe in shoe_list:
        if shoe_code == shoe.code:
            return shoe


# The function below calculates the total value of each item and prints the information to the console

def value_per_item():
    # Creating a total_value_list variable to store list of products with their total value
    total_value_list = []

    for shoe in shoe_list:
        total_value_list.append([shoe.product, shoe.get_cost() * shoe.get_quantity()])

    # Printing total_value list in tabular form
    print(tabulate(total_value_list))


# The function below finds the product with the highest quantity and print the shoes is for sale

def highest_qty():
    excessive = 0  # To store the quantity of shoe with the largest stock.
    sale_shoe = ''  # To store the shoe with maximum quantity to print it out as sale

    # Looping through each shoe object and checking if the shoe quantity is the largest and assigning both the quantity
    # and shoe name in the above defined variables.

    for shoe in shoe_list:
        if shoe.get_quantity() > excessive:
            excessive = shoe.get_quantity()
            sale_shoe = shoe.product

    return sale_shoe


# ==========Main Menu=============
# Defining main function to provide user with the list of menu to perform various activity.

def main():

    menu = '''++++++++++++++++++++++++++++++++++++++++++++++++++
Please enter your choice :
r  - To read shoe's data from the text file.
c  - To capture data for the shoe.
v  - To view details of the shoes
rs - To restock the quantity of the shoes
s  - To search for the shoes
tv - To calculate total value of each shoes
hq - To determine shoes with highest quantity
e  - exit
++++++++++++++++++++++++++++++++++++++++++++++++++
    '''

    while True:
        menu_choice = input(menu).lower().strip()

        if menu_choice == 'r':
            # Reading a text file to build a list of shoe object

            read_shoes_data()
            print("The shoe data has been read from the inventory file\n")

        elif menu_choice == 'c':
            # Capturing shoe data from the user

            capture_shoes()
            print("Shoe data has been captured\n")

        elif menu_choice == 'v':
            # Viewing shoe details in a table format
            view_all()

        elif menu_choice == 'rs':
            # Restocking the low quantity shoe

            re_stock()
            print("The restocking operation has been completed\n")

        elif menu_choice == 's':
            # Finding shoe with a shoe code

            get_shoe = search_shoe()
            print("Country\t\tCode\t\tProduct Name\t\tCost\t\tQuantity\n")

            # printing the string representation of object define in __str__() by type casting it to string and
            # replacing its comma with horizontal tab
            print(str(get_shoe).replace(',', '\t\t'))

        elif menu_choice == 'tv':
            # Finding total value of each shoe product.

            print("Total value of each shoe items are : ")
            value_per_item()

        elif menu_choice == 'hq':
            # Getting the shoe product with the highest quantity and putting it for sale

            get_highest = highest_qty()
            print(f"The {get_highest} shoe is for Sale\n")

        elif menu_choice == 'e':
            exit()
        else:
            print("Please enter a correct choice")


# Calling the main function
if __name__ == "__main__":
    main()
