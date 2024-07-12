master_pwd = input("What is your Master Password?: ")

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("password.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing passwords or quit: (View/add/q )").lower()
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode!!!")

    
