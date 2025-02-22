import os


def display_receipt(name, title, items, total, discounted):
    # This line defines a function named `display_receipt` that takes four arguments:
    # `name`, `title`, `items`, and `total`.

    # Print Receipt Header
    print("\n\n\n")
    print("=" * 82)
    print(f"{'':<33}--- RECEIPT ---")
    # This line prints a header to indicate the start of the receipt.
    print("=" * 82)

    # Print Total Number of Items
    print(f"Total Items: {len(items)}")
    # Print Customer Information
    print(f"Items bought by: {title} {name}")

    # This line prints the customer's name, including their title (e.g. Mr., Ms., etc.).

    # This line prints the total number of items purchased, which is obtained by getting the length of the `items` list.
    print("=" * 82)
    # Print Column Headers
    print(f"{'Number of Pieces':<20}{'Item Name':<20}{'Manufacturer':<20}{'Number of Pieces*Price':<20}")
    # Print Item Details
    sorted_items = sorted(items, key=lambda x: x['Item Name'])
    for item in sorted_items:
        print(f"{item['Number of Pieces']:<20}{item['Item Name']:<20}{item['Manufacturer']:<20}{item['Number of Pieces'] * item['Price per Unit']:<20}")
    # This line prints the details of each item, including its name, quantity, and price per unit.

    print("=" * 82)
    # Print Total Cost
    print(f"{'':<51}{'TOTAL:'} Php {total:.2f}")
    # This line prints the total cost of the items, which is formatted to display two decimal places, aligned to the right.

    print(f"{'':<40}{'DISCOUNTED TOTAL:'} Php {discounted:.2f}")
    # This line prints the discounted total cost of the items, which is formatted to display two decimal places, aligned to the right.
    # Print Closing Message
    print("\nThank you for shopping! \n")
    # This line prints a closing message to thank the customer for shopping.


def store_receipt(user_info, items):
    file_path = "GROCERY.DAT"
    # file_path = "grocery.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline='') as file:
        if not file_exists:
            # Write header if file does not exist
            file.write(
                "Title Name,Age,Sex,Civil Status,Item No.,Item Name,Manufacturer,Number of Pieces,Price per Unit,Total,Discounted Total\n")

        for item in items:
            file.write(f"{user_info['title']} {user_info['name']},{user_info['age']},{user_info['sex']},{user_info['civil_status']},{item['Item No.']},{item['Item Name']},{item['Manufacturer']},{item['Number of Pieces']},{item['Price per Unit']},{user_info['total']:.2f},{user_info['discounted']:.2f}\n")
    # This block opens the file "grocery.csv" in append mode, writes the header if the file is new, and writes each item's details in CSV format along with user information.

# Example usage:
# items = get_items_info()
# total = sum(item['Number of Pieces'] * item['Price per Unit'] for item in items)
# display_receipt("John Doe", "Mr.", items, total)
