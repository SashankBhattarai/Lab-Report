# Mini Project: Simple To-Do Manager Using Functional Programming

# Add a task
def add_task(task_list, task_name):
    task = {"name": task_name, "completed": False}
    task_list.append(task)
    return task_list

# List pending
def list_pending(task_list):
    return list(filter(lambda t: not t["completed"], task_list))

# Search tasks by keyword
def search_tasks(task_list, keyword):
    return list(filter(lambda t: keyword.lower() in t["name"].lower(), task_list))

# Mark a single task as completed by index
def complete_task(task_list, index):
    if 0 <= index < len(task_list):
        task_list[index]["completed"] = True
    else:
        print("Invalid task number!")
    return task_list

# Display task
def show_tasks(task_list):
    if not task_list:
        print("No tasks found.")
        return
    for i, t in enumerate(task_list, 1):
        status = "Done" if t["completed"] else "Pending"
        print(f"{i}. {t['name']} - {status}")


#
# Main Workflow
#

tasks = []

tasks = add_task(tasks, "Walk")
tasks = add_task(tasks, "Homework")
tasks = add_task(tasks, "Run")

n = int(input("How many tasks do you want to add? "))

for i in range(n):
    name = input(f"Enter task {i+1}: ")
    tasks = add_task(tasks, name)

# Mark a single task as completed
print("\nAll Tasks:")
show_tasks(tasks)
choice = int(input("\nEnter the task number you want to mark as done: ")) - 1
tasks = complete_task(tasks, choice)

print("\nUpdated Tasks:")
show_tasks(tasks)
