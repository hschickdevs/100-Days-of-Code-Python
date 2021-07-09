import random

rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

print("🕹️ Let's play a game of Rock Paper Scissors. 🕹️")
print("0 - Rock")
print("1 - Paper")
print("2 - Scissors")
user_index = int(input("Your choice: "))

if 0 <= user_index <= 2:
    computer_index = random.randint(0, 2)
    print(f"You chose: {rps[user_index]}")
    print(f"Computer chose: {rps[computer_index]}")
    if user_index == computer_index:
        print("It's a DRAW!")
    elif user_index == 0:
        if computer_index == 1:
            print("You LOST!")
        else:
            print("You WON!")
    elif user_index == 1:
        if computer_index == 0:
            print("You WON!")
        else:
            print("You LOST!")
    else:
        if computer_index == 0:
            print("You LOST!")
        else:
            print("You WON!")
else:
    print("Invalid choice. Please re-run the code to try again!")
