from modules import user_info
from modules import item_info
from modules import receipt


def main():
    # Get user information
    name, title, is_senior, age, sex, civil_status = user_info.get_user_info()

    # Get items information
    items = item_info.get_items_info()

    # Calculate total
    total = sum(item["Number of Pieces"] * item["Price per Unit"]
                for item in items)

    discounted = total

    if is_senior:
        # discounted 20%
        discounted *= 0.8

    user_info_dict = {
        "name": name,
        "title": title,
        "is_senior": is_senior,
        "age": age,
        "sex": sex,
        "total": total,
        "civil_status": civil_status,
        "total": total,
        "discounted": discounted
    }

    # Display receipt
    receipt.display_receipt(name, title, items, total, discounted)

    # Store receipt in GROCERY.DAT
    receipt.store_receipt(user_info_dict, items)


if __name__ == "__main__":
    main()
