{% include navbar.html %}

{% include style.html %}


# Create Performance Task

### Plan
My plan is to have a shopping cart/price calculator that takes user input for items, finds it from a list, and then uses that information to calculate the total. This total would also be checked to see if a discount or voucher is applicable and inform the user.

### Runtime
Select "1" in this menu to view the create task.

{% include repl_embed.html %}

### Create Task Video - [[Link]](https://youtu.be/XLt2iPqYrBo)
{% include ct_video.html %}

### Create Task Written Response

- 3a.i : The overall purpose of the program is to take multiple inputs from a user with the items that the user wants, and then use it to calculate the total of those items. Then the user will receive a 20% discount if the value of the items is above $60. The program will display both the original total and then the discounted total if the discount is applicable.

- 3a.ii : The video demonstrates the program being able to take user inputs to take and use the value of each item to calculate what the total would be. Finally, the video shows what happens when the total matches the criteria for a discount, which it then applies if that is the case.

- 3a.iii : The video demonstrates the user input, which is a user inputting different numbers to select the items they want through a menu, in any order and combination. The video then demonstrates the output, which includes the subtotal, a discount message (if a discount is applicable), and then the final total.

- 3b.i : Data storage in list:

```python
price_list = [
  ["Shoes", 55, 'price_adder(55)'],
  ["Socks", 5, 'price_adder(5)'],
  ["T-Shirt", 10, 'price_adder(10)'],
  ["Jacket", 30, 'price_adder(30)'],
  ["Hat", 8, 'price_adder(8)']
]
```

- 3b.ii: Data in the list being used:

```python
 # Creates a dictionary with all menu options
  for item in price_list:
    index = len(prompts)
    prompts[index] = item

  # Prints each option in the menu
  for a, b in prompts.items():
    print(a, '---', b[0], "- $" + str(b[1]))
```

- 3b.iii: The name of the list in this response is price_list, and it is a python two-dimensional list.
- 3b.iv: The data contained in this list represent the names, prices, and function input of each item in the shop available for user input. The function input corresponds to the function that would be executed with a preset parameter.
- 3b.v: The data in this dictionary is essential for calculating the total cost of all the items that the user has inputted. Without this dictionary, the program would be unable to function, and it would output a total of $0 every time. If this list did not exist, the most likely way for the user to calculate their total price would be to manually input the price of each item that they have, which would likely be more inconvenient as it would require more work for the user. 

- 3c.i : priceadder procedure

```python
# Adds the item's price to the subtotal
def price_adder(value):
  global subtotal
  subtotal = subtotal + value
  print('-' * 45)
  print("Your subtotal is: $" + str(subtotal))
```

- 3c.ii : usage of the priceadder procedure

Preset parameters for each item.
```python
price_list = [
  ["Shoes", 55, 'price_adder(55)'],
  ["Socks", 5, 'price_adder(5)'],
  ["T-Shirt", 10, 'price_adder(10)'],
  ["Jacket", 30, 'price_adder(30)'],
  ["Hat", 8, 'price_adder(8)']
]
```
AND using the correct parameter based on user input
```python
user_choice = input("Please select an item: ")

  # Attempt to run selected function (adding to or calculating total)
  try:
    uchoice = int(user_choice)
    try:
        # try as function
        os.system("clear")
        action = prompts.get(uchoice)[2]
        action()
```

- 3c.iii : The priceadder procedure takes the input, “value”, which is the price of the item that the user selected. Then the procedure finds the current subtotal (important to make sure the user can calculate the price for more than one item). Finally, the procedure adds this price to the subtotal and prints the current subtotal out.
- 3c.iv: First, the procedure takes the global subtotal variable that is defined and saved outside of the procedure. Then the procedure takes the value parameter given depending on the user's item choice, and then adds it to the subtotal to make the new subtotal value. Finally, the new subtotal is printed in a string format for the user to be able to see the new subtotal value.
- 3d.i : 

First Call (first iteration of):
```python
["Shoes", 55, 'price_adder(55)'],
```

Second Call (second iteration of):
```python
["Socks", 5, 'price_adder(5)'],
```

- 3d.ii : In the first call, the condition tested is the price_adder(55), in which the parameter is the value of the shoes option. This adds 55 to the current subtotal, and outputs the new subtotal for the user to see. In the second call, the condition tested is price_adder(5), the parameter is the value of the socks option. This adds 5 to the subtotal, and then outputs the new subtotal.

- 3d.iii : Although the order and parameters of the call can vary based on which option the user chooses at which time, the first call shown results in 55 being added to the subtotal value, which is the value of the shoes, and the new subtotal is then shown. Meanwhile, the second call shown results in 5 being added to the subtotal value, which is the value of the socks, with the new subtotal value being displayed. Both calls add a specified value to the subtotal and then display it for the user to be able to see what their subtotal is every time they input an item.



<!-- ### Code Snippets

List
```python
price_list = [
  ["Shoes", 55, 'price_adder(55)'],
  ["Socks", 5, 'price_adder(5)'],
  ["T-Shirt", 10, 'price_adder(10)'],
  ["Jacket", 30, 'price_adder(30)'],
  ["Hat", 8, 'price_adder(8)']
]  
```

Shop Menu Function
```python
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
```

Price Adder and Final Total function
```python
# Adds the item's price to the subtotal
def price_adder(value):
  global subtotal
  subtotal = subtotal + value
  print('-' * 45)
  print("Your subtotal is: ", subtotal)

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
  print("Your final total is: $" + str(total))
  print("=" * 45)
  # Terminating the environment after calculating total
  sys.exit()
```
 -->
