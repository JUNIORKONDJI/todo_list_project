class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def toggle(self):
        self.completed = not self.completed