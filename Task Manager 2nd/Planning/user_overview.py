from datetime import date
from _datetime import datetime

current_date = date.today()
current_date = current_date.strftime("%d %b %Y")
current_date = datetime.strptime(current_date, "%d %b %Y")

user_amount = 0
task_amount = 0
username_list = []
with open('user.txt', 'r') as user_file:
    for line in user_file:
        other_username, other_password = line.split(',', 2)
        username_list.append(other_username)
        user_amount += +1

task_counter = 0
with open('tasks.txt', 'r') as task_file:
    for line in task_file:
        line = line
        task_counter += +1

user_and_task_amount = f'''The total users is:   {user_amount}
The total tasks is:   {task_counter}\n'''

write_amounts = open('user_overview.txt', 'w')
write_amounts.write(user_and_task_amount)


task_per_user = 0
task_completed = 0
overdue = 0
for i in range(len(username_list)):
    task_per_user = 0
    task_completed = 0
    overdue = 0
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

        user_percentage_tasks = round(task_per_user / task_counter * 100, 2)
        if task_completed != 0:
            percentage_complete = round(task_completed / task_per_user * 100, 2)
        else:
            percentage_complete = 0
        percentage_incomplete = 100 - percentage_complete
        if overdue != 0:
            percentage_overdue = round(overdue / task_per_user * 100, 2)
        else:
            percentage_overdue = 0

        user_write = (f'''{username_list[i]}
amount of tasks:                {task_per_user}
percentage of total tasks:      {user_percentage_tasks}%
percentage of completed tasks:  {percentage_complete}%
percentage of incomplete tasks: {percentage_incomplete}%
percentage of tasks overdue:    {percentage_overdue}% \n''')
        with open('user_overview.txt', 'w') as write_tasks:
            write_amounts.write(user_write)
write_amounts.close()



