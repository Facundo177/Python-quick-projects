name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across? Type walk or swim: ")
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died of dehydration.")
    else:
        print("Not a valid option.")
elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly, do you want to cross it or head back? (cross/back): ")
    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk o them? (yes/no): ")
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and lose the game.")
        else:
            print("Not a valid option.")
    else:
        print("Not a valid option.")
else:
    print("Not a valid option.")

print("Thank you for playing,", name)