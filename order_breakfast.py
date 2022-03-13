import time

#saving space via refactoring (print and time.sleep())
def print_pause(string):
    print(string)
    time.sleep(2)

# template for user input
def valid_input(prompt,option1,option2):
    while True:
        message = input(prompt).lower()
        if option1 in message:
            return message
        elif option2 in message:
            return message
        else:
            print_pause("Sorry, I dont understand.")

#Bot introduces itself
print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")

while True:
    
    response = valid_input("Please place your order. Would you like waffles or pancakes?\n","waffles","pancakes") #offers 2 choices
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
       
    print_pause("Your order will be ready shortly.")
    choice = valid_input("Would you like to place another order? Please say 'yes' or 'no'.\n","yes","no") #offers 2 choices
    if "yes" in choice:
        print_pause("Very good, I'm happy to take another order.")
    elif "no" in choice:
        print_pause("It was a pleasure to serve you, Goodbye!")
        break
    