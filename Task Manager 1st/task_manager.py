from datetime import date


# Menu bar function
# Checks if the user is the admin or other user
def call_menu(x):
    if x == "admin":
        print('''Please select on of the following:
        t - total number of tasks
        u- total number of users
        r - register user
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit''')
    else:
        print('''Please select on of the following:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit''')


program_on = True
while program_on:
    # Login page
    # Used string building to compare the user input and the actual credentials as its saved in the 'user.txt' file
    login = True
    while login:
        username_input = input("Enter your username please: ").lower()
        password_input = input("Enter your password please: ").lower()
        stored_credentials = ""
        with open("user.txt", "r") as credentials:
            for line in credentials:
                stored_credentials = stored_credentials + line
        stored_credentials = stored_credentials.replace(",", "").split("\n")
        login_attempt = username_input + " " + password_input
        if login_attempt in stored_credentials:
            login = False
        else:
            print("Your username or password is incorrect, please try again \n")
    print("\nYour login was successful \n")

    # Loops the menu until variable "menu" is turned 'False'
    menu = True
    while menu:
        call_menu(username_input)
        choose_option = str(input("\nEnter letter here: ")).lower()
        print(f"You chose option: {choose_option}\n")

        # Total number of tasks
        # Only the admin can use this option, if other user tries, it ignores the command
        if choose_option == "t":
            if username_input == "admin":
                task_counter = 0
                with open("tasks.txt", "r") as text_file:
                    for line in text_file:
                        amount = line
                        task_counter += + 1
                print(f"There are {task_counter} tasks")
            else:
                print("No such entry available, please try again")

        # Total number of users
        # Only the admin can use this option, if other user tries it, ignores the command
        elif choose_option == "u":
            if username_input == "admin":
                user_counter = 0
                with open("user.txt", "r") as text_file:
                    for line in text_file:
                        amount = line
                        user_counter += + 1
                print(f"There are {user_counter} users")
            else:
                print("No such entry available, please try again")

        # Register user
        # Only the admin can use this option, if other user tries, it ignores the command
        elif choose_option == "r":
            if username_input == "admin":
                new_user = True
                while new_user:
                    new_username = input("What would you like to make the username of the new?: ").lower()
                    new_password = input("What do you want to make the password of the new user?: ").lower()
                    confirm_password = input("Please confirm the password: ").lower()
                    if confirm_password == new_password:
                        new_details = new_username + ", " + new_password
                        with open("user.txt", "a+") as text_file:
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

        # Adds a task
        # Asks the user questions that are required to enter into the task list
        # Used string building to get the required format on variable "add_to_tasks
        elif choose_option == "a":
            title = input("What is the title of the task?: ").lower()
            description = input("What is the description of the task?: ").lower()
            due_date = input("When should the task be completed by?: ").lower()
            date_assigned = date.today()
            current_date = date_assigned.strftime("%d %b %Y")
            task_completed = "No"
            title = title.lower()
            description = description.lower()
            due_date = due_date.lower()
            add_to_tasks = (username_input + ", " + title + ", " + description + ", " + due_date + ", " + current_date
                            + ", " + task_completed)
            # Reads the file then appends it at the end
            with open("tasks.txt", "a+") as text_file:
                text_file.seek(0)
                data = text_file.read(100)
                if len(data) > 0:
                    text_file.write("\n")
                text_file.write(add_to_tasks)
            print("Task was successfully added")

        # View all tasks
        elif choose_option == "va":
            print("this is all the current task\n")
            with open("tasks.txt", "r") as text_file:
                for line in text_file:
                    username, title, description, due_date, date_assigned, task_completed = line.split(",", 6)
                    task_completed = task_completed.replace("\n", "")
                    # Made it easier to read for user
                    print(f'''
        Assigned to:        {username}
        Task:               {title}
        Date Assigned:      {date_assigned}
        Due Date:           {due_date}
        Is task complete:   {task_completed}
        Task description:   {description}
        ''')

        # View logged in users tasks
        elif choose_option == "vm":
            print(f"This is all the current tasks for {username_input}\n")
            with open("tasks.txt", "r") as text_file:
                for line in text_file:
                    username, title, description, due_date, date_assigned, task_completed = line.split(",", 6)
                    task_completed = task_completed.replace("\n", "")
                    # Only prints the tasks for the current logged in user
                    # Made it easier to read for the user
                    if username == username_input:
                        print(f'''
        Assigned to:        {username}
        Task:               {title}
        Date Assigned:      {date_assigned}
        Due Date:           {due_date}
        Is task complete:   {task_completed}
        Task description:   {description}
        ''')

        # Exit
        # If both values are turned 'False', the program will close
        elif choose_option == "e":
            menu = False
            program_on = False
        # If the user types in any key that has nothing bound to it
        else:
            print("No such entry available, please try again")

# Recourses:
# https://elearning.wsldp.com/python3/python-get-current-date/
# https://strftime.org/
# https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
# https://www.w3schools.com/python/python_functions.asp
