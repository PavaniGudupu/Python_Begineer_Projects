from art import rock, paper, scissors, logo
import random
print(logo)
game_images = [rock, paper, scissors]
print("\n Welcome to the Rock, Paper, Scissors Game!!!")
user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You'r choice: \n")
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer choice: \n")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")