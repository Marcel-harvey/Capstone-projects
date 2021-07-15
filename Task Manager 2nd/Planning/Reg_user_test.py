#new_user = True
#while new_user:
check_username = True
while check_username:
    new_username = input("What would you like to make the username of the new?: ").lower()
    with open('user.txt', 'r') as username_text:
        for line in username_text:
            check_detail = line.split(", ")[0]
            if new_username == check_detail:
                username_text.seek(0)
                print('Username already exists, please try again')
                new_username = input("What would you like to make the username of the new?: ").lower()
            else:
                check_username = False

new_user = True
while new_user:
    new_password = input("What do you want to make the password of the new user?: ").lower()
    confirm_password = input("Please confirm the password: ").lower()
    if confirm_password == new_password:
        new_details = new_username + ", " + new_password
        with open("user.txt", "a+") as text_file:
            text_file.write('\n' + new_details)
        print("User was successfully registered")
        new_user = False
    else:
        print("The passwords does not match, please try again")