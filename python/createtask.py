# Importing os and sys libraries for clearing the terminal and terminating the process.
import os
import sys

# Sets subtotal = 0 when the function is run again
subtotal = 0

# Adds the item's price to the subtotal
def price_adder(value):
  global subtotal
  subtotal = subtotal + value
  print('-' * 45)
  print("Your subtotal is: $" + str(subtotal))

def final_total(subtotal):
  print("=" * 45)
  # Calculating if total is over $60 and applying a discount if it is
  if subtotal > 60:
    print("Because your order is over $60, you qualify for a 20% discount!" )
    total = round((0.8 * subtotal), 2)
  else:
    total = subtotal
  # Formatting and printing the total
  print("-" * 45)
  print("Your subtotal is: $" + str(subtotal))
  print("-" * 45)
  print("Your final total is: $" + str(total))
  print("=" * 45)
  # Terminating the environment after calculating total
  sys.exit()

# Dictionary with values and predefined function parameters
price_list = [
  ["Shoes", 55, 'price_adder(55)'],
  ["Socks", 5, 'price_adder(5)'],
  ["T-Shirt", 10, 'price_adder(10)'],
  ["Jacket", 30, 'price_adder(30)'],
  ["Hat", 8, 'price_adder(8)']
]
 
# Function intended to display a shop that users can interact with to add items
def shop_menu():

  global subtotal
  # Prints banner part of menu
  print( "=" * 45 + "\n Item Selector \n" + "=" * 45)
  prompts = {0: ["Calculate Final Total", str(subtotal) + " subtotal" , 'final_total(subtotal)']}

  # Creates a dictionary with all menu options
  for item in price_list:
    index = len(prompts)
    prompts[index] = item

  # Prints each option in the menu
  for a, b in prompts.items():
    print(a, '---', b[0], "- $" + str(b[1]))

  user_choice = input("Please select an item: ")

  # Attempt to run selected function (adding to or calculating total)
  try:
    uchoice = int(user_choice)
    try:
        # try as function
        os.system("clear")
        action = prompts.get(uchoice)[2]
        action()
    except TypeError:
        try:  
            exec(action)
        except FileNotFoundError:
            print(f"File not found!: {action}")
        # Tries function again
  # Not a number error
  except ValueError:
      print(f"Not a number: {uchoice}")
  # All other errors
  except UnboundLocalError:
      print(f"Invalid choice: {uchoice}")
  
  shop_menu() # Builds the shop menu again for more choices.

if __name__ == "__main__":
  # Gives instructions and runs the shop
  print("=" * 45)
  print("Choose as many items as you want using the menus. \n If your order is over $60, you qualify for a 20% discount. ")
  shop_menu()