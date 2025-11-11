# Task manager code:
# Create dictionary, add user.txt information to it
# Create loop for login.
# Create code for menu options


users = {}  # Create dictionary for user file info

# Load existing users into a dictionary
with open("user.txt", "r") as user_file:
    for line in user_file:
        if line.strip():
            username, password = line.strip().split(", ")
            users[username] = password  # create key:value pairing

# Login loop
while True:
    username = input("Enter your username: ")
    password_input = input("Enter your password: ")
    
    if username in users and users[username] == password_input:
        print(f"\nWelcome, {username}!\n")
        break
    else:
        print("Invalid username or password. Please try again.\n")

# Menu loop: 
while True:
    # Two menu sets, one for admin only including the ds option
    if username == "admin":
        menu = input('''Select one of the following options:
r  - register a user
a  - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e  - exit
: ''').lower()
    else:
        menu = input('''Select one of the following options:
r  - register a user                     
a  - add task
va - view all tasks
vm - view my tasks
e  - exit
: ''').lower()

    if menu == 'r':
        if username != "admin":
            print("Only the admin user can register new users.\n")
            continue

        '''Add a new user'''
        new_user = input("Enter a new username: ")
        new_pass = input("Enter a new password: ")
        confirm_pass = input("Confirm the password: ")

        if new_pass == confirm_pass:
            with open("user.txt", "a") as user_file:
                user_file.write(f"\n{new_user}, {new_pass}")
            print("New user registered successfully.\n")
        else:
            print("Passwords do not match. User not added.\n")

    elif menu == 'a':
        '''Add a new task'''
        name = input("Enter Username that the task is assigned to: ")
        task = input("Enter the title of the task: ")
        work = input("Enter the description of the task: ")
        d_date = input("Enter the tasks due date: ")
        date = input("Enter today's date: ")
        done = "No"

        with open("tasks.txt", "a") as tfile:
            tfile.write(f"\n{name}, {task}, {work}, {date}, {d_date}, {done}")
        print("Task added successfully.\n")

    elif menu == 'va':
        '''View all tasks'''
        print("\n========= All Tasks =========")
        with open("tasks.txt", "r") as task_file:
            for line in task_file:
                fields = line.strip().split(", ")
                print(f"""
Task:          {fields[1]}
Assigned to:   {fields[0]}
Date Assigned: {fields[3]}
Due Date:      {fields[4]}
Completed:     {fields[5]}
Description:   {fields[2]}
""")

    elif menu == 'vm':
        '''View my tasks'''
        print(f"\n========= Tasks for {username} =========")
        found = False
        with open("tasks.txt", "r") as task_file:
            for line in task_file:
                fields = line.strip().split(", ")
                if fields[0] == username:
                    found = True
                    print(f"""
Task:          {fields[1]}
Assigned to:   {fields[0]}
Date Assigned: {fields[3]}
Due Date:      {fields[4]}
Completed:     {fields[5]}
Description:   {fields[2]}
""")
        if not found:
            print("No tasks assigned to you.\n")

    elif menu == 'ds' and username == "admin":
        '''Display statistics'''
        with open("user.txt", "r") as u_file:
            total_users = len([line for line in u_file if line.strip()])

        with open("tasks.txt", "r") as t_file:
            total_tasks = len([line for line in t_file if line.strip()])

        print("\n========= Statistics =========")
        print(f"Total users: {total_users}")
        print(f"Total tasks: {total_tasks}\n")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again.\n")
