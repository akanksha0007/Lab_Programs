
# Create an online food ordering system 

print("Welcome to Akanksha's Food Corner!") #print welcome message

menu = {                         #menu dictionary
    1: ["Pizza", 199],           #dictionary with item number as key and a list of item name and price as value
    2: ["Burger", 99],
    3: ["Pasta", 80],
    4: ["Fries", 80],
    5: ["Maggi", 60],
    6: ["Sandwich",60],
    7: ["Cold Drink",50],
    98: ["Ice Cream",40],
    9: ["Coffee", 20],
    10: ["Tea", 15],
}

total = 0     # Initialize total bill amount
order_list = []   # Initialize list to store ordered items

# Show Menu
print("\nMenu:")
for num, item in menu.items(): # Loop through the menu dictionary
    print(f"{num}. {item[0]} - ₹{item[1]}") # Display each item with its price

while True: # Loop to take orders
    choice = int(input("\nEnter item number to order (0 to finish): ")) 

    if choice == 0:  # If user enters 0, exit the loop
        break
    elif choice in menu: # If choice is valid, process the order
        qty = int(input(f"Enter quantity for {menu[choice][0]}: "))  # Get quantity from user
        price = menu[choice][1] * qty # Calculate total price for the item
        order_list.append((menu[choice][0], qty, price))  # Append item, quantity, and price to order list
        total += price
        print(f"Added {qty} x {menu[choice][0]}") #print confirmation message
    else:
        print("Invalid choice! Please select from the menu.")

# Final Bill
print("\nYour Order Summary:")
for item, qty, cost in order_list: # Loop through the order list to display each item
    print(f"{item} x {qty} = ₹{cost}") # Display each ordered item with its quantity and cost
print(f"\nTotal Bill: ₹{total}")   # Display total bill amount
print("------------------")
print("Thank you for ordering from Akanksha's Food Corner! ")
