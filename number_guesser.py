import random

# top_of_range = input("Type a number: ") # Here even if the user types input as a number but also it will be string so to change that we use if statement below. 

# if top_of_range.isdigit(): #
#     top_of_range = int(top_of_range)

# else:
#     print("Please type a number next time. ")
#     quit()


# random_number = random.randint(0, top_of_range)
# print(random_number)

user_guess = input("Please type a number: ")
if user_guess.isdigit():
    user_guess = int(user_guess)

else:
    print("please type a number next time")
    quit()

random_number = random.randint(0, user_guess)

guesses = 0
while True:
    guesses += 1
    user_guess = input("Please type a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time!")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number")

print("You got right in " , guesses ,  "guesses")