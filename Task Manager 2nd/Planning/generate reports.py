from datetime import date
from _datetime import datetime

amount_of_tasks = 0
completed_tasks = 0
uncompleted_tasks = 0
over_due_tasks = 0

current_date = date.today()
current_date = current_date.strftime("%d %b %Y")
current_date = datetime.strptime(current_date, "%d %b %Y")

with open('tasks.txt', 'r') as data:
    for line in data:
        count_username, count_title, count_description, count_date_assigned, count_due_date, count_task_completed = (
            line.split(', ', 6))
        amount_of_tasks += +1
        count_task_completed = count_task_completed.replace('\n', '').lower()
        if count_task_completed == 'yes':
            completed_tasks += +1
        elif count_task_completed == 'no':
            count_due_date = datetime.strptime(count_due_date, "%d %b %Y")
            if current_date > count_due_date:
                over_due_tasks += +1
            uncompleted_tasks += +1

percentage_incomplete = round(uncompleted_tasks / amount_of_tasks * 100, 0)
percentage_due = round(over_due_tasks / amount_of_tasks * 100, 0)

report = (f'''The amount of tasks is:   {amount_of_tasks}
The amount of tasks that has being completed is:    {completed_tasks}
The amount of tasks that is incomplete is:  {uncompleted_tasks}
The amount of tasks that are over due is: {over_due_tasks}
The percentage of tasks that are incomplete is:     {percentage_incomplete}%
The percentage of over due tasks is:    {percentage_due}%''')

with open('task_overview.txt', 'w') as task_overview:
    task_overview.write(report)

