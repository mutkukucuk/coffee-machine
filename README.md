Coffee Machine Simulation in Python

Overview

This Python program simulates the functionality of a coffee machine. The user can choose from three types of coffee drinks (Espresso, Latte, and Cappuccino), insert coins to make a payment, and the program will check if the available resources are sufficient to make the selected drink. If the user provides enough money and the resources are available, the machine will prepare the coffee, deduct the necessary ingredients from its inventory, and return any change. The program also allows users to check the current status of the machine’s resources and turn the machine off when done.

Features
	•	Drink Selection: The program offers three drinks: Espresso, Latte, and Cappuccino. Each drink requires a specific combination of ingredients such as water, coffee, and milk.
	•	Resource Management: The machine tracks its available resources (water, milk, coffee) and checks if there are enough ingredients to prepare the selected drink.
	•	Coin Payment System: Users insert coins (quarters, dimes, nickels, and pennies) to make a payment for their selected drink. If the inserted amount is insufficient, the machine will notify the user and refund the money.
	•	Resource Deduction: After a successful transaction, the machine will reduce the amount of resources (water, milk, and coffee) used to prepare the selected drink.
	•	Report Feature: Users can check the current stock of resources in the machine by typing the command “report.”
	•	Exit Feature: The program can be turned off by typing “off.”

Requirements
	•	Python 3.x

How to Run
	1.	Start the program by running the script in a Python environment.
	2.	When prompted, choose a coffee drink by typing espresso, latte, or cappuccino. You can also type report to check the machine’s resources or off to turn the machine off.
	3.	If selecting a drink, you will be prompted to insert coins. Enter the number of quarters, dimes, nickels, and pennies you wish to use.
	4.	The program will either prepare the drink if sufficient resources and payment are provided or inform you of any issues (insufficient resources or funds).

Example Usage
	•	Select a Drink: The program asks the user which drink they would like (espresso, latte, or cappuccino). Upon selection, the program checks if the necessary resources are available.
	•	Insert Coins: The user is prompted to enter the number of coins they wish to insert. The machine calculates the total amount and checks if it is enough to cover the cost of the selected drink.
	•	Change: If the payment exceeds the cost of the drink, the machine returns the change.
	•	Resource Update: After the coffee is made, the machine reduces the amount of resources accordingly and prepares the next user’s selection.

Functionality Details
	•	Resource Check: The program checks the availability of each ingredient required for the selected drink. If any ingredient is insufficient, a message is displayed and the transaction is canceled.
	•	Payment Process: Users are prompted to enter the amount of quarters, dimes, nickels, and pennies they wish to use. The total is calculated, and if the amount is less than the cost of the drink, the transaction is canceled, and the user is refunded.
	•	Machine Report: Users can view the current status of the machine’s resources (water, milk, coffee) by typing report.

How to Exit

To stop the program, type off. This will end the simulation and print a message indicating that the machine is off.

Conclusion

This coffee machine simulation is an excellent example of how to use Python to model real-world systems, manage resources, and handle user interactions. It combines basic concepts like loops, conditionals, and functions, making it a great learning tool for beginners.