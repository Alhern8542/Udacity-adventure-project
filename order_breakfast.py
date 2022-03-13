import time

print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(2)
print("Today we have two breakfasts available.")
time.sleep(2)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(2)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(2)
while True:
    while True:
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            break
        elif "pancakes" in response:
            print("Pancakes it is!")
            break
        else:
            print("Sorry, I don't understand.")
    time.sleep(2)
    print("Your order will be ready shortly.")
    time.sleep(2)
    choice = input("Would you like to place another order? Please say 'yes' or 'no'.\n")
    if "yes" in choice.lower():
        print("Very good, I'm happy to take another order.")
        time.sleep(2)
    elif "no" in choice.lower():
        time.sleep(2)
        print("OK, Goodbye!")
        time.sleep(2)
        break
    else:
        time.sleep(2)
        print("Sorry, I dont understand.")