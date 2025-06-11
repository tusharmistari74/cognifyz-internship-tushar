class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return f"📌 {self.title}: {self.description}"


task_list = []

def display_menu():
    print("\n📋 TASK MANAGER MENU")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    if title == "" or description == "":
        print("❌ Title and description cannot be empty.")
        return
    task = Task(title, description)
    task_list.append(task)
    print("✅ Task added successfully!")

def view_tasks():
    if not task_list:
        print("📭 No tasks found.")
        return
    print("\n🔍 All Tasks:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

def update_task():
    if not task_list:
        print("📭 No tasks to update.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: "))
        if 1 <= task_num <= len(task_list):
            new_title = input("New title: ").strip()
            new_desc = input("New description: ").strip()
            if new_title and new_desc:
                task_list[task_num - 1].title = new_title
                task_list[task_num - 1].description = new_desc
                print("🔁 Task updated successfully!")
            else:
                print("❌ Title and description cannot be empty.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task():
    if not task_list:
        print("📭 No tasks to delete.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(task_list):
            deleted_task = task_list.pop(task_num - 1)
            print(f"🗑️ Deleted: {deleted_task.title}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    print("🎯 Welcome to the Console Task Manager")
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()