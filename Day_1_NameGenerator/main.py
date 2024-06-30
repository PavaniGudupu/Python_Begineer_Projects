###String Concatination Variables in Python
# String Manipulation
# Input and Print Functions
# Variable Naming Rules



from art import logo
print(logo)
print("\nWelcome to the name Generator!!!")
name = input("What's the name of the city you grew up in ? \n")
petname = input("What's your pet's name ? \n")
final_name = name + " " + petname
print(f"Your name could be {final_name}")
