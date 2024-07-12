name = input("Type your name: ")
print("Welcome ",name, "to our adventurous games.")

answer = input("You have come to dirt road and dead end. Which way would you like to go? (choose: left or right): ").lower()

if answer == "left":
    left_adv = input("You come to a river. You can walk around or swim accross. choose: walk or swim: ").lower()
    if left_adv == "walk":
        print("You walk many miles and ran out of water and you lose")
    elif left_adv == "swim":
        print("You swam across and eaten by an alligator")
    else:
        print("Not a valid option. You lose!!!")   


elif answer == "right":
    right_adv = input("You come to a bridge. You can cross or head back. choose: cross or go back: ").lower()
    if right_adv == "cross":
        right_adv = input("You cross the bridge and meet a stranger. Do you talk to them? (Yes/No)").lower()
        if right_adv == "yes":
            print("You talked to stranger and got Gold. So you WON!!!")
        elif right_adv == "no":
            print("You ignored the stranger. You lost!!")
        else:
            print("Not a valid option. Loser")
    elif right_adv == "back":
        print("You go back and lose.")
    else:
        print("Not a valid option. You lose!!!")

else:
    print("Not a valid option. You lose!!!")

print("Thank you for trying " ,name)