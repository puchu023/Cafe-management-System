def show_menu(menu):
    print("\n===== CAFE MENU =====")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")
    print("======================")

def take_order(menu):
    order = {}
    while True:
        show_menu(menu)
        choice = input("Enter item to order (or 'done' to finish): ").strip().title()

        if choice.lower() == 'done':
            break

        if choice in menu:
            try:
                qty = int(input(f"Enter quantity of {choice}: "))
                if qty <= 0:
                    print("Quantity must be positive.")
                    continue
                order[choice] = order.get(choice, 0) + qty
                print(f"Added {qty} {choice}(s) to your order.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Sorry, that item is not on the menu.")

    return order

def print_bill(order, menu):
    print("\n===== BILL =====")
    total = 0
    if not order:
        print("No items ordered.")
        return

    for item, qty in order.items():
        price = menu[item]
        subtotal = price * qty
        total += subtotal
        print(f"{item} x {qty} = ₹{subtotal}")
    
    print("----------------------")
    print(f"Total Amount: ₹{total}")
    print("======================")

def main():
    # Define the cafe menu
    menu = {
        "Coffee": 50,
        "Tea": 30,
        "Sandwich": 100,
        "Cake": 80,
        "Muffin": 60,
        "Juice": 40
    }

    print("Welcome to the Cafe Management System!")
    order = take_order(menu)
    print_bill(order, menu)

if __name__ == "__main__":
    main()




