print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("\nYou're at a crossroad. Where do you wanna go?")
choice = input("Type 'left' or 'right': ").lower()
if choice == 'left':
    print("\nYou arrive at a beautiful lake.")
    print("You see a island at the middle.")
    print("What do you wanna do?")
    choice = input("Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    if choice == 'wait':
        print("\nYou arrive at a house with three doors.")
        print("Each door has a different color: red, blue, and yellow.")
        print("Which door do you wanna open?")
        choice = input("Type 'red', 'blue', or 'yellow': ").lower()
        if choice == 'red':
            print('\nRoom full of fire.')
            print("Game over!")
        elif choice == 'blue':
            print('\nRoom full of beasts.')
            print("Game over!")
        elif choice == 'yellow':
            print("\nCongratulations! You found the treasure!")
        else:
            print("\nInvalid choice!")
            print("Game over!")
    else:
        print("\nYou are attack by angry piranhas.")
        print("Game over!")

else:
    print("\nYou got hit by a train.")
    print("Game over!")


