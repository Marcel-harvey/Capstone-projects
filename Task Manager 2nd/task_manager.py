from datetime import date
from _datetime import datetime


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
        gr - generate reports
        ds - display statistics
        e - exit''')
    else:
        print('''Please select on of the following:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit''')


# Function for register user
def reg_user():
    # Check if the user logged in is 'admin'
    if username_input == "admin":
        # Opens the 'user.txt' text file and compares the user entered value to what is in file
        # If the user entered value is found i will print a message and ask to try again
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

        # Ask the user to make a password and confirm it, if it doesnt match, prompts message and asks again
        # If matches it will append the new username and new password to the 'user.txt' file
        new_user = True
        while new_user:
            new_password = input("What do you want to make the password of the new user?: ").lower()
            confirm_password = input("Please confirm the password: ").lower()
            if confirm_password == new_password:
                new_details = new_username + ", " + new_password
                with open("user.txt", "a+") as append_details:
                    append_details.write('\n' + new_details)
                print("User was successfully registered")
                new_user = False
            else:
                print("The passwords does not match, please try again")
    else:
        print("No such entry available, please try again")


# Function for add task
def add_task():
    # Ask the user all the required questions and converts all the inputs to lowercase
    task_title = input("What is the title of the task?: ").lower()
    task_description = input("What is the description of the task?: ").lower()
    task_due_date = input("When should the task be completed by?: ").lower()
    task_date_assigned = date.today()
    current_date = task_date_assigned.strftime("%d %b %Y")
    task_completion = "no"
    task_title = task_title.lower()
    task_description = task_description.lower()
    task_due_date = task_due_date.lower()
    add_to_tasks = (username_input + ", " + task_title + ", " + task_description + ", " + current_date
                    + ", " + task_due_date + ", " + task_completion)
    # Reads the file then appends it at the end
    with open("tasks.txt", "a+") as user_task:
        user_task.seek(0)
        data = user_task.read(100)
        if len(data) > 0:
            user_task.write("\n")
        user_task.write(add_to_tasks)
    print("Task was successfully added")


# Function for view all tasks
def view_all():
    # Opens the file 'task.txt' and splits everything into separate variables, then prints in a easy to read format
    print("this is all the current task\n")
    with open("tasks.txt", "r") as view_file:
        for line in view_file:
            all_username, all_title, all_description, all_due_date, all_date_assigned, all_task_completed = (
                line.split(",", 6))
            all_task_completed = all_task_completed.replace("\n", "")
            # Made it easier to read for user
            print(f'''
            Assigned to:        {all_username}
            Task:               {all_title}
            Date Assigned:      {all_date_assigned}
            Due Date:           {all_due_date}
            Is task complete:   {all_task_completed}
            Task description:   {all_description}
            ''')


# Function for view tasks of logged in user
def view_mine():
    # Opens the 'tasks.txt' file and splits everything into separate variable then prints in a easy to read format
    # Adds 1 to 'option_counter' and prints the counter above all the variables, to select a task to edit
    print(f"This is all the current tasks for {username_input}\n")
    with open("tasks.txt", "r") as view_text:
        option_counter = 0
        for line in view_text:
            option_counter += +1
            vm_username, vm_title, vm_description, vm_date_assigned, vm_due_date, vm_task_completed = line.split(",", 6)
            vm_task_completed = vm_task_completed.replace("\n", "")
            if vm_username == username_input:
                print(f'''
    Option:             {option_counter}
    Assigned to:        {vm_username}
    Task:               {vm_title}
    Date Assigned:      {vm_date_assigned}
    Due Date:           {vm_due_date}
    Is task complete:   {vm_task_completed}
    Task description:   {vm_description}
            ''')

    # Asks the user to select what task they want to edit according to 'option_counter'
    # or enter '-1' to return to the main menu
    user_option = int(
        input("To return to main menu, enter -1. Or choose a number to edit or mark a task complete: Option"))
    if user_option == -1:
        menu = False
    # Reads through the entire file and breaks at the task where the user selected
    else:
        counter = 1
        with open('tasks.txt', 'r') as test_file:
            for line in test_file:
                if counter < user_option:
                    counter += +1
                else:
                    break
        edit_username, edit_title, edit_description, edit_date_assigned, edit_due_date, edit_task_completed = (
            line.split(', ', 6))
        edit_task_completed = edit_task_completed.replace("\n", "")
        print(f'''
        Assigned to:        {edit_username}
        Task:               {edit_title}
        Date Assigned:      {edit_date_assigned}
        Due Date:           {edit_due_date}
        Is task complete:   {edit_task_completed}
        Task description:   {edit_description}
                ''')

        # The user is asked if he want to edit a task or mark it as complete
        edit_or_mark = input('Do you want to edit as task or mark a task as complete? Enter edit or mark: ').lower()
        edit_task_completed = edit_task_completed.lower()

        # If the user selects edit and the task has not being completed, the user gets asked what he wants to edit
        # The task then gets changed in the file, by locating its position and swapping the value
        if edit_or_mark == 'edit' and edit_task_completed == 'no':
            choose_edit = input(
                'Do you want to edit who the task is assigned to OR the due date? Enter user or date: ').lower()
            if choose_edit == 'user':
                change_user = input('Who do you want to assign the task to?: ').lower()
                edit_username = change_user
                to_write = (edit_username + ', ' + edit_title + ', ' + edit_description + ', ' + edit_date_assigned
                            + ', ' + edit_due_date + ', ' + edit_task_completed + '\n')
                write_task = open('tasks.txt', 'r')
                write_file = write_task.readlines()
                write_file[counter - 1] = to_write

                write_task = open('tasks.txt', 'w')
                write_task.writelines(write_file)
                write_task.close()
                print(f'The user has being changed to {edit_username}')
            elif choose_edit == 'date':
                change_date = input('What would you like to make the new due date? ').lower()
                edit_due_date = change_date
                to_write = (edit_username + ', ' + edit_title + ', ' + edit_description + ', ' + edit_date_assigned
                            + ', ' + edit_due_date + ', ' + edit_task_completed + '\n')
                write_task = open('tasks.txt', 'r')
                write_file = write_task.readlines()
                write_file[counter - 1] = to_write

                write_task = open('tasks.txt', 'w')
                write_task.writelines(write_file)
                write_task.close()
                print(f'The due date has being changed to {edit_due_date} ')

        # If the user selected to mark the task as complete, the 'no' value will be swapped to 'yes'
        # Then it writes back into the file by locating its position
        elif edit_or_mark == 'mark':
            edit_task_completed = 'yes'
            to_write = (edit_username + ', ' + edit_title + ', ' + edit_description + ', ' + edit_date_assigned
                        + ', ' + edit_due_date + ', ' + edit_task_completed + '\n')
            write_task = open('tasks.txt', 'r')
            write_file = write_task.readlines()
            write_file[counter - 1] = to_write

            write_task = open('tasks.txt', 'w')
            write_task.writelines(write_file)
            write_task.close()
            print('Task marked complete')
    return


# Function for task overview
def task_view():
    # Counter variable are declared to count specific pieces
    amount_of_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    over_due_tasks = 0

    # Set the variable 'current_date' to the current date in a specified format
    current_date = date.today()
    current_date = current_date.strftime("%d %b %Y")
    current_date = datetime.strptime(current_date, "%d %b %Y")

    # Opens the 'tasks.txt' file and adds to counter variables where specified
    with open('tasks.txt', 'r') as data:
        for line in data:
            count_username, count_title, count_description, count_date_assigned, count_due_date, count_task_completed =\
                (line.split(', ', 6))
            amount_of_tasks += +1
            count_task_completed = count_task_completed.replace('\n', '').lower()
            if count_task_completed == 'yes':
                completed_tasks += +1
            elif count_task_completed == 'no':
                # Convert date format
                count_due_date = datetime.strptime(count_due_date, "%d %b %Y")
                if current_date > count_due_date:
                    over_due_tasks += +1
                uncompleted_tasks += +1

    percentage_incomplete = round(uncompleted_tasks / amount_of_tasks * 100, 0)
    percentage_due = round(over_due_tasks / amount_of_tasks * 100, 0)

    # made a variable 'report' to save an easy to read format
    report = (f'''The amount of tasks is:   {amount_of_tasks}
The amount of tasks that has being completed is:    {completed_tasks}
The amount of tasks that is incomplete is:  {uncompleted_tasks}
The amount of tasks that are over due is: {over_due_tasks}
The percentage of tasks that are incomplete is:     {percentage_incomplete}%
The percentage of over due tasks is:    {percentage_due}%\n''')

    # Writes the variable into the 'task_overview.txt' file
    with open('task_overview.txt', 'w') as task_overview:
        task_overview.write(report)

    # Reads what is in the 'task_overview.txt' file and prints it to the user
    print('Statistic generated:')
    with open('task_overview.txt', 'r') as task_over:
        show_user = task_over.read()
        print(show_user)


# Function for user overview
def user_view():
    # Set the variable 'current_date' to the current date with a specified format
    current_date = date.today()
    current_date = current_date.strftime("%d %b %Y")
    current_date = datetime.strptime(current_date, "%d %b %Y")

    # Set a counter variable to add 1 to, to count the amount of users
    # Made a blank list variable to append all the usernames to
    user_amount = 0
    username_list = []
    with open('user.txt', 'r') as user_file:
        for line in user_file:
            other_username, other_password = line.split(',', 2)
            username_list.append(other_username)
            user_amount += +1

    # Set a counter variable to add 1 to, to count the amount of tasks
    task_amount = 0
    with open('tasks.txt', 'r') as task_file:
        for line in task_file:
            line = line
            task_amount += +1

    # Added the 'user_amount' and 'task_amount' variable to 1 variable with a sentence
    # Writes 'user_and_task_amount' to 'user_overview.txt'
    user_and_task_amount = f'''The total users is:   {user_amount} and the total tasks is:   {task_amount}\n'''
    write_amounts = open('user_overview.txt', 'w')
    write_amounts.write(user_and_task_amount)

    # Loops through all the names in the variable 'username_list'
    for i in range(len(username_list)):
        # Declared counter variable to add 1 to where needed
        task_per_user = 0
        task_completed = 0
        overdue = 0
        # Opens the 'tasks.txt' file and separates everything into separate variables to use
        # Adds 1 to counter variables if conditions are met in if statements
        with open('tasks.txt', 'r') as task_file:
            for line in task_file:
                all_username, all_title, all_description, all_due_date, all_date_assigned, all_task_completed = (
                    line.split(", ", 6))
                all_task_completed = all_task_completed.replace('\n', '')
                all_task_completed = all_task_completed.lower()
                if username_list[i] == all_username:
                    task_per_user += +1
                if username_list[i] == all_username and all_task_completed == 'yes':
                    task_completed += +1
                if username_list[i] == all_username and all_task_completed == 'no':
                    all_due_date = datetime.strptime(all_due_date, "%d %b %Y")
                    if current_date > all_due_date:
                        overdue += +1

            # Did some basic math to calculate percentages, if 1 of the counters was 0 the variable is set to 0
            user_percentage_tasks = round(task_per_user / task_amount * 100, 2)
            if task_completed != 0:
                percentage_complete = round(task_completed / task_per_user * 100, 2)
            else:
                percentage_complete = 0
            percentage_incomplete = 100 - percentage_complete
            if overdue != 0:
                percentage_overdue = round(overdue / task_per_user * 100, 2)
            else:
                percentage_overdue = 0

            # Saves the format in a separate variable then writes it into the file 'user_overview.txt'
            user_write = (f'''{username_list[i]}
    amount of tasks:                {task_per_user}
    percentage of total tasks:      {user_percentage_tasks}%
    percentage of completed tasks:  {percentage_complete}%
    percentage of incomplete tasks: {percentage_incomplete}%
    percentage of tasks overdue:    {percentage_overdue}% \n''')

            write_amounts.write(user_write)
    # The open file variable 'write_accounts' gets closed after everything is written in it
    write_amounts.close()

    # Opens the 'user_overview.txt' file as read only and displays it to the user
    print('Statistic generated:')
    with open('user_overview.txt', 'r') as user_over:
        show_user = user_over.read()
        print(show_user)


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

        # Register user, calls the function 'reg_user()'
        elif choose_option == "r":
            reg_user()

        # Adds a task, calls the function 'add_task()'
        elif choose_option == "a":
            add_task()

        # View all tasks, calls the function 'view_all()'
        elif choose_option == "va":
            view_all()

        # View logged in users tasks, calls function 'view_mine()'
        elif choose_option == "vm":
            view_mine()

        # View task overview, calls function 'task_view()
        elif choose_option == "gr":
            task_view()

        # View user overview, calls function 'user_view()
        elif choose_option == "ds":
            user_view()

        # Exits the program by turning the variables 'menu' and 'program_on' 'False'
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
# https://stackoverflow.com/questions/27135499/read-file-until-specific-line-in-python
# https://www.kite.com/python/answers/how-to-edit-a-specific-line-in-a-text-file-in-python
# https://www.educative.io/edpresso/how-to-convert-a-string-to-a-date-in-python
