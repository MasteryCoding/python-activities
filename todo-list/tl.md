# Todo List

## Introduction

In this activity, we will create a todo list program where we can add tasks, mark them completed, and see the whole list of tasks with their status. 

## Overview

### Step 1: Add Task  

Let’s start by writing a class for todo list which automatically generates the empty list for todo tasks when created. Then we will create a function called `add_task` which does the following: 
 
* Take task as its argument
* Display an error message when the task is empty 
* Append the dictionary representing to the list which contains the `task` key and `False` value for its `status` key
* Display a message confirming the completion of adding the task

* Hint:
    * Assert statement tests if the specified condition is true or false and runs the specified code if the condition is false. 

#### Solution

```py
class TodoList: 

def __init__(self):
self.tasks = [] 

def add_task(self, task):
    assert task, "Task cannot be empty"
    self.tasks.append({"task": task, "completed": False})
    print("Task added") 
```

### Step 2: Mark Task

Now we will write a function called `mark_completed` to mark tasks completed by changing its value to True for status. The function will: 

* Take the index of the task as an argument
* Display an error message if the index is not integer  
* Try changing the value of `status` key to `True` for the task of the given index
* Display an error message if the index is invalid 
* Display a message confirming the completion of marking the task 

* Hint:
    * `isInstance` function is used for checking if the given object has the specified data type
    * `IndexError` occurs when invalid index is accessed 


#### Solution

```py
def mark_completed(self, task_index):
    assert isinstance(task_index, int), "Index should be an integer"
    try:
        self.tasks[task_index]["status"] = True
    except IndexError:
        print("Invalid task index")
    else:
        print("Task marked as completed") 
```

### Step 3: Display Task   

Last function we’ll be writing is named `display_tasks`, which will do the following: 
* Display the title 
* Display value of `task` key and `status` key for each task

* Hint:
    * Use f-string to display values of the dictionary

#### Solution

```py
def display_tasks(self):
    print("To-Do List:")
    for task in self.tasks:
        print(f"{task['task']} - {task['status']}")
```

### Step 4: Finalize the program 

Create an instance for the todo list and continuously provide options to either add, mark, list tasks, or finish the program. We will: 
* Create an instance of the todo list class
* Run the function of the class that corresponds to the keyword 
* Ask for a keyword iteratively until we choose to close the todo list program 

#### Solution

```py
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
```

## Conclusion

Phew, there we have our todo list program! Try adding, marking, and displaying tasks using the program.
