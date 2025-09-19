class Taskmanager:
    def __init__(self):
        self.tasks = []
        print("Task Manager initialized.")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def show_tasks(self):
        print("Your Task")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Task not found.")

