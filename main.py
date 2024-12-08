# Menu definition
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Coffee machine resources with lowercase keys
coffeeMachineResources = {'water': 1000, 'milk': 600, 'coffee': 300, 'cost': 0}


# Function to check if resources are sufficient
def is_resource_sufficient(drink_ingredients):
    for item, amount in drink_ingredients.items():
        if coffeeMachineResources.get(item, 0) < amount:  # Direct access to lowercase keys
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


# Function to reduce resources
def make_coffee(drink_ingredients):
    for item, amount in drink_ingredients.items():
        coffeeMachineResources[item] -= amount  # Reduce the resources
    print("Here is your coffee! ☕ Enjoy!")


# Function to process coin input from the user
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


# Variable to control the main loop
shall_continue = True

# Main loop
while shall_continue:
    # Get drink choice from the user
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink_choice == "off":
        # Stop the loop if 'off' is entered
        shall_continue = False
        print("Coffee Machine is off.")
    elif drink_choice == "report":
        # Report the resources
        print("Current machine resources:")
        for key, value in coffeeMachineResources.items():
            print(f"{key}: {value}")
    elif drink_choice in MENU:
        # If the chosen drink is in the menu, proceed
        drink = MENU[drink_choice]

        # Step 1: Check if resources are sufficient
        if is_resource_sufficient(drink["ingredients"]):
            # Step 2: Process coin input
            payment = process_coins()
            if payment < drink["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                # Step 3: Update the revenue and make coffee
                coffeeMachineResources["cost"] += drink["cost"]
                make_coffee(drink["ingredients"])
                change = round(payment - drink["cost"], 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
    else:
        # If an invalid drink choice is made
        print("Invalid choice. Please try again.")
