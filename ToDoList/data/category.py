import json

class Task:
    def __init__(self, task: str, added_on: str = None, due_date: str = None, is_completed: bool = False, priority: int = 0):
        self.task = task
        self.category_name = self.category()
        self.added_on = added_on
        self.due_date = due_date
        self.is_completed = is_completed
        self.priority = priority
        self.category()

    def set_priority(self, priority: int):
        self.priority = priority

    def set_due_date(self, date: str):
        self.due_date = date

    def category(self):
        class_name = str(self.__class__).replace(">","").split(".")[-1].removesuffix("'")
        self.category_name = class_name

    def __repr__(self):
        return json.dumps({
                "task": self.task,
                "category": str(self.category_name),
                "added on": self.added_on,
                "due date": self.due_date,
                "is completed": self.is_completed,
                "priority": self.priority
        })


class Project(Task):
    def __init__(self, task: str, added_on:str = None, due_date: str = None, is_completed:bool = False, priority: int = 0):
        self.task = task
        self.category_name = self.category()
        self.added_on = added_on
        self.due_date = due_date
        self.is_completed = is_completed
        self.priority = priority
        super().__init__(task, added_on, due_date, is_completed, priority)

class Custom(Task):
    def __init__(self, task: str, added_on: str = None, due_date: str = None, is_completed: bool = False, priority: int = 0):
        self.task = task
        self.category_name = self.category()
        self.added_on = added_on
        self.due_date = due_date
        self.priority = priority
        self.is_completed = is_completed
        super().__init__(task, added_on, due_date, is_completed, priority)

    def set_category_name(self, category_name: str):
        self.category_name = category_name
