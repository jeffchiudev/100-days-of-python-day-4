import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
player_input = int(input("Welcome to the RPS Championships, type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
player_choice = options[player_input]
computer_choice = random.choice(options)
print(player_choice)
print("Computer chose:")
print(computer_choice)

if (player_choice == rock) and (computer_choice == scissors):
  print("You Win!")
elif (player_choice == rock) and (computer_choice == paper):
  print("You Lose.")
elif (player_choice == paper) and (computer_choice == rock):
  print("You Win!")
elif (player_choice == paper) and (computer_choice == scissors):
  print("You Lose.")
elif (player_choice == scissors) and (computer_choice == paper):
  print("You Win!")
elif (player_choice == scissors) and (computer_choice == rock):
  print("You Lose.")
else:
  print("You Draw.")
  