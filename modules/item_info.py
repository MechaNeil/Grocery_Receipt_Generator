def get_items_info():
    # This line defines a function named `get_items_info` that takes no arguments.

    # Get Number of Items
    while True:
        try:
            num_items = int(input("Enter the number of items to be bought: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # This line prompts the user to enter the number of items they want to buy.
    # The input is converted to an integer using the `int()` function and stored in the `num_items` variable.

    # Initialize Empty List
    items = []
    # This line initializes an empty list called `items` that will be used to store information about each item.

    # Loop Through Each Item
    for i in range(num_items):
        # This line starts a `for` loop that will iterate `num_items` times.
        # The variable `i` will take on the value of each iteration, starting from 0.

        # Get Item Details
        item_no = i+1
        print(f"Item No {item_no}")
        # This line prompts the user to enter the item number for the current item.
        # The `f-string` is used to insert the current item number (`i+1`) into the prompt.

        while True:
            item_name = input("Enter item name: ")
            if len(item_name) > 0:
                break
            else:
                print("Item name cannot be empty. Please enter a valid item name.")
        # This line prompts the user to enter the name of the current item.

        while True:
        
            manufacturer = input("Enter manufacturer: ")
            if len(manufacturer) > 0:
                break
            else:
                print("Manufacturer cannot be empty. Please enter a valid manufacturer name.")
        # This line prompts the user to enter the manufacturer of the current item.

        while True:
            try:
                num_pieces = int(input("Enter number of pieces: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        # This line prompts the user to enter the number of pieces for the current item.
        # The input is converted to an integer using the `int()` function.

        while True:
            try:
                price_per_unit = float(input("Enter price per unit (Php): "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        # This line prompts the user to enter the price per unit for the current item.
        # The input is converted to a floating-point number using the `float()` function.

        # Store Item Details in Dictionary
        price_number_of_pieces = num_pieces * price_per_unit
        items.append({
            "Item No.": item_no,
            "Item Name": item_name,
            "Manufacturer": manufacturer,
            "Number of Pieces": num_pieces,
            "Price per Unit": price_per_unit,
            "Price Number of Pieces": price_number_of_pieces
        })
        # This line creates a dictionary to store the details of the current item.
        # The dictionary is then appended to the `items` list.

    # Sort Items by Name
    items = sorted(items, key=lambda x: x["Item Name"])
    # This line sorts the `items` list in ascending order based on the "Item Name" key.
    # The `sorted()` function returns a new sorted list, which is then assigned back to the `items` variable.
    # The `lambda` function is used to specify the sorting key.

    # Return Sorted Items
    return items
    # This line returns the sorted `items` list.

# Example usage:
# items = get_items_info()
# for item in items:
#     print(item)
