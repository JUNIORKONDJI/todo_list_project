# todo_list.py
from task import Task

class ToDoList:
    """
    Manages all tasks in the to-do list.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle()

    def get_tasks(self):
        return self.tasks