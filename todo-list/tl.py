class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        assert task, "Task cannot be empty"
        self.tasks.append({"task": task, "status": False})
        print("Task added")

    def mark_completed(self, task_index):
        assert isinstance(task_index, int), "Index should be an integer"
        try:
            self.tasks[task_index]["status"] = True
        except IndexError:
            print("Invalid task index")
        else:
            print("Task marked as completed")

    def display_tasks(self):
        print("To-Do List:")
        for task in self.tasks:
            print(f"{task['task']} - {task['status']}")

todo_list = TodoList()

action = input("Enter 'add' to add a task, 'complete' to mark a task as completed, 'display' to see the whole list, or 'done' to finish the program: ")

while action != "done":
    if action == 'add':
        task = input("Enter task: ")
        todo_list.add_task(task)
    elif action == 'complete':
        task_index = int(input("Enter task index to mark as completed: "))
        todo_list.mark_completed(task_index)
    elif action == 'display':
        todo_list.display_tasks()
    action = input("Enter 'add' to add a task, 'complete' to mark a task as completed, 'display' to see the whole list, or 'done' to finish the program: ")