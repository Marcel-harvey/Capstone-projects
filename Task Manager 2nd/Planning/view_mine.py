def edit_file(x):
    write_task = open(x, 'r')
    write_file = write_task.readlines()
    write_file[counter - 1] = to_write

    write_task = open(x, 'w')
    write_task.writelines(write_file)
    write_task.close()
    return


username_input = input("username: ")
print(f"This is all the current tasks for {username_input}\n")
with open("tasks.txt", "r") as text_file:
    option_counter = 0
    for line in text_file:
        option_counter += +1
        username, title, description, date_assigned, due_date, task_completed = line.split(",", 6)
        task_completed = task_completed.replace("\n", "")
        if username == username_input:
            print(f'''
Option:             {option_counter}
Assigned to:        {username}
Task:               {title}
Date Assigned:      {date_assigned}
Due Date:           {due_date}
Is task complete:   {task_completed}
Task description:   {description}
        ''')

user_option = int(input("To return to main menu, enter -1. Or choose a number to edit or mark a task complete: Option"))
if user_option == -1:
    menu = False
else:
    counter = 1
    task_details = ''
    with open('tasks.txt', 'r') as test_file:
        for line in test_file:
            if counter < user_option:
                counter += +1
            else:
                break
    edit_username, edit_title, edit_description, edit_date_assigned, edit_due_date, edit_task_completed = line.split(
        ', ', 6)
    edit_task_completed = edit_task_completed.replace("\n", "")
    print(f'''
    Assigned to:        {edit_username}
    Task:               {edit_title}
    Date Assigned:      {edit_date_assigned}
    Due Date:           {edit_due_date}
    Is task complete:   {edit_task_completed}
    Task description:   {edit_description}
            ''')

    edit_or_mark = input('Do you want to edit as task or mark a task as complete? Enter edit or mark: ').lower()
    edit_task_completed = edit_task_completed.lower()
    if edit_or_mark == 'edit' and edit_task_completed == 'no':
        choose_edit = input(
            'Do you want to edit who the task is assigned to OR the due date? Enter user or date: ').lower()
        if choose_edit == 'user':
            change_user = input('Who do you want to assign the task to?: ').lower()
            edit_username = change_user
            to_write = (edit_username + ', ' + edit_title + ', ' + edit_description + ', ' + edit_date_assigned
                        + ', ' + edit_due_date + ', ' + edit_task_completed + '\n')
            edit_file('tasks.txt')
            print(f'The user has being changed to {edit_username}')
        elif choose_edit == 'date':
            change_date = input('What would you like to make the new due date? ').lower()
            edit_due_date = change_date
            to_write = (edit_username + ', ' + edit_title + ', ' + edit_description + ', ' + edit_date_assigned
                        + ', ' + edit_due_date + ', ' + edit_task_completed + '\n')
            edit_file('tasks.txt')
            print(f'The due date has being changed to {edit_due_date} ')
    elif edit_or_mark == 'mark':
        edit_task_completed = 'yes'
        to_write = (edit_username + ', ' + edit_title + ', ' + edit_description + ', ' + edit_date_assigned
                    + ', ' + edit_due_date + ', ' + edit_task_completed + '\n')
        edit_file('tasks.txt')
        print('Task marked complete')

# Resources
# https://stackoverflow.com/questions/27135499/read-file-until-specific-line-in-python
# https://www.kite.com/python/answers/how-to-edit-a-specific-line-in-a-text-file-in-python
