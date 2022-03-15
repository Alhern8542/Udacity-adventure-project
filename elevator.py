import time

def print_pause(string):
    print(string)
    time.sleep(2)

def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")

def enter_floor():
    floor = input("Please enter the number for the floor you would like to visit:\n"
                "1. Lobby\n"
                "2. Human recources\n"
                "3. Engineering department\n")
    return floor

items = []

intro()
while True:

    floor = enter_floor()
   
    if floor == "1":
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find yourself in the lobby.")
        if "ID card" in items:
            print_pause("The clerk greets you, but she has already given you your ID card,\n"
            "so there is nothing more to do here now.")
        else:
            items.append("ID card")
            print_pause("The clerk greets you and gives you your ID card.")
        
    elif floor == "2":
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself in the human resources department.")
        if "handbook" in items:
            print_pause("The HR folks are busy at their desks.\n"
                        "There doesn't seem to be much to do here.")
        else:
            print_pause("The head of HR greets you.")
            if "ID card" in items:
                print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
                items.append("handbook")
            else:
                print_pause("He has something for you, but says he can't" 
                            " give it to you until you go get your ID card.")
        
    elif floor == "3":
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself in the engineering department.")
        if "ID card" in items:
            print_pause("You use your ID card to open the door")
            print_pause("Your program manager greets you and tells you that you\n"
            "need to have a copy of the employee handbook in order to start work.")
            if "handbook" in items:
                print_pause("Fortunately, you got that from HR!")
                print_pause("Congratulatons!")
                print_pause("You are ready to start your new job as vice president of engineering!")
        
        else:
            print_pause("Unfortunately, the door is locked and you can't get in.")
            print_pause("It looks like you need some kind of key card to open the door.")
            print_pause("You head back to the elevator.")

    else:
        print_pause("Invalid floor")

    print_pause("Where would you like to go next?")
