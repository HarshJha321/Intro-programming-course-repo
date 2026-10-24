# Function to display the menu
def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


# Function to retrieve price and name based on item number
def get_item_price(choice):
    if choice == 1:
        return 3.00, "Taco"
    elif choice == 2:
        return 4.50, "Burrito"
    elif choice == 3:
        return 3.95, "Nachos"
    elif choice == 4:
        return 2.95, "Soft Drink"
    else:
        return 0.00, ""


# --- Main Program Execution ---

print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

orders = []
total_due = 0.0

# Loop until user enters 5
choice = 0
while choice != 5:
    print_menu()
    choice = int(input("Enter selection: "))

    if choice >= 1 and choice <= 4:
        price, item_name = get_item_price(choice)
        total_due = total_due + price
        orders.append(item_name)
        print("You selected a", item_name)
    elif choice == 5:
        # Quit option
        pass
    else:
        print("Invalid choice, please select 1-5.")

# Print the final receipt
order_summary = " and ".join(orders)
print(f"You ordered a {order_summary}. Your total is ${total_due:.2f}")