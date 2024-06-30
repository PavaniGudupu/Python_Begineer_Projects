# conditional statements, 
# logical operators,
# code block 
# scope

from art import logo
print(logo)
print("\nWelcome to Tresure Island !!")
print("\n Your mission is to find the treasure.")
cross_road = input("Your ar a cross road. Where do you want to go? Type \"left\" or \"right\" : ")
if cross_road == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim: ")
    if lake == "wait":
        island = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose: ")

        if island == "yellow":
            print("You win!!")

        elif island == "red" or island == "blue":
            print("You falled in fire. You Lose!! Game Over..")

        else:
            print("Enter the correct prompt!!!!!")

    elif lake == "swim":
        print("You falled in lake . You Lose!! Game Over..")

    else:
        print("Enter the correct prompt!!!!!")

elif cross_road == "right":
    print("You falled from the rock . You Lose!! Game Over..")

else:
    print("Enter the correct prompt!!!!!")