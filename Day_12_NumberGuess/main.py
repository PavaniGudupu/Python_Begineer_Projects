import random
from art import logo

num = random.randint(1, 100)
easy_attempt = 10
hard_attempt = 5

def easy(num, easy_attempt):
    game = True
    while game:
        print(f"You have {easy_attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == num:
            print(f"You got it! The answer was {num}")
            game = False
        elif guess > num:
            easy_attempt -= 1
            print("Too high.\nGuess again")
        elif guess < num:
            easy_attempt -= 1
            print("Too low.\nGuess again")

        if easy_attempt == 0:
            game = False
            print(f"All attempts used. The correct number was {num}. No attempts remaining.")

def hard(num, hard_attempt):
    game = True
    while game:
        print(f"You have {hard_attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == num:
            game = False
            print(f"You got it! The answer was {num}")
        elif guess > num:
            hard_attempt -= 1
            print("Too high.\nGuess again")
        elif guess < num:
            hard_attempt -= 1
            print("Too low.\nGuess again")

        if hard_attempt == 0:
            game = False
            print(f"All attempts used. The correct number was {num}. No attempts remaining.")

print(logo)
print(f"\nWelcome to the Number Guess Game!!\nAnswer : {num}")
print(f"\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    easy(num, easy_attempt)
elif difficulty == 'hard':
    hard(num, hard_attempt)
else:
    print("Invalid input! Please type 'easy' or 'hard'.")
