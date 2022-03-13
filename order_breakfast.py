import time

#saving space via refactoring (print and time.sleep())
def print_pause(string):
    print(string)
    time.sleep(2)

#Bot introduces itself
print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")
while True:
    while True:
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower() #offers 2 choices
        if "waffles" in response:
            print_pause("Waffles it is!")
            break
        elif "pancakes" in response:
            print_pause("Pancakes it is!")
            break
        else:
            print_pause("Sorry, we do not serve that at this time.")
    print_pause("Your order will be ready shortly.")
    choice = input("Would you like to place another order? Please say 'yes' or 'no'.\n")
    if "yes" in choice.lower():
        print_pause("Very good, I'm happy to take another order.")
    elif "no" in choice.lower():
        print_pause("It was a pleasure to serve you, Goodbye!")
        break
    else:
        print("Sorry, I dont understand.")