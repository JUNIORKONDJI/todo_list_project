# test_todo.py
from todo_list import ToDoList

todo = ToDoList()
todo.add_task("Buy milk")
todo.add_task("Finish homework")

for t in todo.get_tasks():
    print(t.title, t.completed)

todo.toggle_task(0)

print("\nAfter toggling first task:")
for t in todo.get_tasks():
    print(t.title, t.completed)