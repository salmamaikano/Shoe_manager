# -----------imported libraries---------
from shoes import Shoe
from tabulate import tabulate


# ---------Functions------------

# a function for reading from .txt and saving the content as objects in the class
def read_shoes_data():
    # checks for error
    try:

        # opens the .txt file with readability access
        inventory = open("inventory.txt", "r")

        # reads the lines in the file
        content = inventory.readlines()

        # removes the first line of the file
        content.pop(0)

        # check for every line in the file
        for i in content:
            # removes the new line character and splits the line
            i = i.strip("\n").split(",")

            # creating objects for the class shoe
            shoe_list = Shoe(i[0], i[1], i[2], float(i[3]), int(i[4]))

            # adds the objects into a list
            shoes.append(shoe_list)

    # exception for file not found
    except FileNotFoundError:

        # prints the string
        print("File not found")

    # function for showing all the content in the list


def view_all():
    try:
        # opens the .txt file with readability access
        inventory = open("inventory.txt", "r")

        # reads the lines in the file
        content = inventory.readlines()

        # an empty list
        table = []

        # check for every line in the file
        for i in content:
            # removes the new line character and splits the line
            i = i.strip("\n").split(",")

            # creating objects for the class shoe
            table_temp = [i[0], i[1], i[2], i[3], i[4]]

            # adds the objects into a list
            table.append(table_temp)

        print(tabulate(table, headers='firstrow', tablefmt="grid"))

    except FileNotFoundError:

        # prints the string
        print("File not found")


# function for restocking shoes
def restock():
    # setting the lowest_quantity to the quantity of the first item in the list
    lowest_quantity = shoes[0].get_quantity()

    # setting index_num to 0
    index_num = 0

    # increments i for every item in the shoes list
    for i, s in enumerate(shoes):

        # checks if the quantity of the item is lower than the lowest_quantity
        if s.get_quantity() < lowest_quantity:

            # setting the lowest_quantity to the quantity of the current item
            lowest_quantity = s.get_quantity()

            # sets index_num = i
            index_num = i

    # returns index_num
    return index_num


# function for searching shoe items
def search_shoe():

    # gets input from user
    shoe_name = input("Enter the product name of the shoe: ")

    # checks for each item in shoes list
    for i in shoes:

        # checks if the input is same as the product
        if i.get_product() == shoe_name:
            # prints the string
            print('\n---------Product Searched---------\n')

            # returns i
            return i


# function for calculating the value for each item
def value_per_item():

    # checks for each item in the shoe list
    for i in shoes:

        # multiplies the quantity and cost of each item
        value = i.get_quantity() * i.get_cost()

        # prints the strings
        print("------------------------------")

        # prints the item and its value
        print(f"{i} \nTotal value is {float(value)}")

        # prints the string
        print("===============================")


# function for getting the highest quantity of the product
def highest_quantity():

    # setting the highest_quantity to the quantity of the first item in the list
    highest_qty = shoes[0].get_quantity()

    # setting index_num to 0
    index_num = 0

    # increments i for every item in the shoes list
    for i, h in enumerate(shoes):

        # checks if the quantity of the item is lower than the highest_quantity
        if h.get_quantity() > highest_qty:

            # setting the highest_quantity to the quantity of the current item
            highest_qty = h.get_quantity()

            # sets index_num = i
            index_num = i

    # prints the string
    print("--------------Highest Quantity Product----------------")

    # prints the index_num in the list
    print(shoes[index_num])

    # prints the string
    print("=====================================================")


# adding new shoe object to the class
def capture_shoes():

    # gets input from the user
    country = input("Enter the country name of the shoe: ")
    code = input("Enter shoe code: ")
    product = input("Enter product name: ")
    cost = int(input("Enter the cost of the shoe: "))
    quantity1 = int(input("Enter the quantity of the shoe: "))

    # creating new object for the class shoes
    new_shoe = Shoe(country, code, product, cost, quantity1)

    # prints the string
    print("\nNew shoe successfully added\n")

    # adds the object to the list of shoes
    return shoes.append(new_shoe)


# -------------Main Code--------------
# empty list
shoes = []

# calls the function to read from the .txt file and store the contents in the list
read_shoes_data()

# an empty string
choice = ""

# the program runs while the variable is not 0
while choice != 0:

    # checks for error
    try:

        # user input
        choice = int(input('''Enter the number for the action you want to perform 
1- View all shoes
2- Search for a shoe
3- Add a new shoe
4- See shoe with the highest stock
5- check value for each item
6- Restock a shoe
0- To quit
'''))

        # checks if input is same as 1
        if choice == 1:

            # calls the function
            view_all()

        # checks if input is same as 2
        elif choice == 2:

            # calls the function
            print(search_shoe())

        # checks if input is same as 3
        elif choice == 3:

            # calls the function
            capture_shoes()

        # checks if input is same as 4
        elif choice == 4:

            # calls the function
            highest_quantity()

        # checks if input is same as 5
        elif choice == 5:

            # calls the function
            value_per_item()

        # checks if input is same as 6
        elif choice == 6:

            # uses the function to a variable
            pos = restock()

            # prints the string
            print('\n---------lowest qty---------\n')

            # print the list with the position in pos
            print(shoes[pos])

            # prints the string
            print('===============================')

            # gets user input
            restock_input = input(f"Do you want to restock {shoes[pos].get_product()}? Yes-or-No\n").lower()

            # checks if users input is same as the string
            if restock_input == "yes":

                # gets user input
                quantity = int(input("Enter the new quantity: "))

                # sets the new quantity with new quantity from the user
                shoes[pos].set_quantity(quantity)

                # prints the string
                print('\n---------Updated qty---------')

                # print the list with the position in pos
                print(shoes[pos])

                # prints the string
                print('===============================')

        # checks if the input is same as the string
        elif choice == 0:

            # displays the string
            print("Goodbye")

    # catches value errors
    except ValueError:

        # prints the string
        print("Invalid option")
