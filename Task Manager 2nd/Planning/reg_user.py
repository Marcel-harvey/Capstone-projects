def reg_user(x):
    if x == "admin":
        new_user = True
        while new_user:
            new_username = input("What would you like to make the username of the new?: ").lower()
            new_password = input("What do you want to make the password of the new user?: ").lower()
            confirm_password = input("Please confirm the password: ").lower()
            if confirm_password == new_password:
                new_details = new_username + ", " + new_password
                with open("user.txt", "a+") as text_file:
                    username, password = text_file.readlines()
                    text_file.seek(0)
                    data = text_file.read(100)
                    if len(data) > 0:
                        text_file.write("\n")
                        new_user = False
                    text_file.write(new_details)
                print("User was successfully registered")
            else:
                print("The passwords does not match, please try again")
    else:
        print("No such entry available, please try again")