import random

print("Welcome to your virtual coin toss program.")

result = random.randint(0,1)
if result == 1:
  print("Heads")
else:
  print("Tails")