# Name: Ruslan Gusakov
# Prog Purpose: this program is for Palermo Pizza
#
#
#
#
#
import datetime

# Pizza prices
small_pizza_price = 9.99
medium_pizza_price = 12.99
large_pizza_price = 14.99
extra_large_pizza_price = 17.99

# Sales tax rate
sales_tax_rate = 0.055

# Initialize variables
total_cost = 0

# Loop to allow multiple orders
while True:
    # Get input from user
    pizza_size = input("What size pizza would you like (small, medium, large, or extra-large)? ")
    num_pizzas = int(input("How many pizzas would you like? "))

    # Calculate pizza cost
    if pizza_size == "small":
        pizza_cost = num_pizzas * small_pizza_price
    elif pizza_size == "medium":
        pizza_cost = num_pizzas * medium_pizza_price
    elif pizza_size == "large":
        pizza_cost = num_pizzas * large_pizza_price
    elif pizza_size == "extra-large":
        pizza_cost = num_pizzas * extra_large_pizza_price
    else:
        print("Invalid pizza size")
        continue

    # Calculate sales tax
    pizza_tax_amount = pizza_cost * sales_tax_rate

    # Calculate total cost
    total_cost += (pizza_cost + pizza_tax_amount)

    # Print receipt
    print("Palmero Pizza")
    print(datetime.datetime.now())
    print("Number of pizzas ordered:", num_pizzas)
    print("Pizza cost: $%.2f" % pizza_cost)
    print("Sales tax: $%.2f" % pizza_tax_amount)
    print("Total: $%.2f" % (pizza_cost + pizza_tax_amount))

    # Ask user if they want to enter another order
    another_order = input("Would you like to enter another order? (Y/N) ").upper()
    if another_order == "Y":
        continue
    elif another_order == "N":
        break
    else:
        print("Invalid input. Please enter Y or N.")

# Print final total cost
print("Total cost for all orders: $%.2f" % total_cost)
