from data.category import Task, Project, Custom
from data.datamanager import ManageData


class ManageTask:
    def __init__(self):
        self.Manager = ManageData()
        self.data = self.Manager.data
        self.remaining_task = 0
        self.completed_task = 0

    def add_todo(self, todo: [Task, Project, Custom]): # added_on: str = None, due_date: str = None):
        self.data['todos'][todo.task] = todo.__dict__
        self.Manager.save(self.data)

    def rm_todo(self, todo: Task):
        if todo.task in self.data.get("todos").keys():
            self.data["todos"].pop(todo.task)
            self.Manager.save(self.data)

    def clear(self):
        self.data["todos"] = {}
        self.Manager.save(self.data)

    def repair(self):
        pass

    def update(self, todo: Task, update_due_date: str = None, is_completed: bool = False):
        if update_due_date is not None and is_completed:
            self.data.get("todos").get(todo.task).update({"due_date": update_due_date})
            self.data.get("todos").get(todo.task).update({"is_completed": True})
        elif update_due_date is not None:
            self.data.get("todos").get(todo.task).update({"due_date": update_due_date})
        elif is_completed:
            self.data.get("todos").get(todo.task).update({"is_completed": True})
        else:
            pass
        self.Manager.save(self.data)