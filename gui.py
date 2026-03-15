import tkinter as tk
from todo_list import ToDoList

class ToDoGUI:
    def __init__(self):
        self.todo = ToDoList()
        self.window = tk.Tk()
        self.window.title("To-Do List")
        self.window.geometry("400x500")
        self.entry = tk.Entry(self.window, width=30, font=("Arial", 14))
        self.entry.pack(pady=10)
        tk.Button(self.window, text="Add Task", command=self.add_task).pack(pady=5)
        self.frame = tk.Frame(self.window)
        self.frame.pack(pady=10)
        self.update_tasks_display()

    def add_task(self):
        title = self.entry.get().strip()
        if title:
            self.todo.add_task(title)
            self.entry.delete(0, tk.END)
            self.update_tasks_display()

    def remove_task(self, index):
        self.todo.remove_task(index)
        self.update_tasks_display()

    def toggle_task(self, index):
        self.todo.toggle_task(index)
        self.update_tasks_display()

    def update_tasks_display(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        for i, task in enumerate(self.todo.get_tasks()):
            text = f"✔ {task.title}" if task.completed else task.title
            lbl = tk.Label(self.frame, text=text, font=("Arial", 14))
            lbl.grid(row=i, column=0, sticky="w", padx=5, pady=2)
            tk.Button(self.frame, text="Toggle", command=lambda i=i: self.toggle_task(i)).grid(row=i, column=1)
            tk.Button(self.frame, text="Delete", command=lambda i=i: self.remove_task(i)).grid(row=i, column=2)

    def run(self):
        self.window.mainloop()