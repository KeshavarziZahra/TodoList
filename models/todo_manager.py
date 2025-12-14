# -*- coding: utf-8 -*-
from models.task import Task
from data.database import ToDoDatabase

class ToDoManager:
    """
    Business logic layer.
    Handles task creation, deletion, and retrieval.
    """

    def __init__(self):
        self.db = ToDoDatabase()

    def add_task(self, task: Task):
        """Create a new task and store it in the database."""
        self.db.add_task(task.title, task.priority)

    def delete_task(self, task_id):
        """Delete a task by its id."""
        self.db.delete_task(task_id)

    def get_all_tasks(self):
        """
        Retrieve all tasks from the database
        and convert them into Task objects.
        """
        rows = self.db.get_all_tasks()
        
        print(rows)
        
        tasks = []

        for row in rows:
            task_id, title, priority, created_at = row
            task = Task(
                title=title,
                priority=priority,
                task_id=task_id,
                created_at=created_at
            )
            tasks.append(task)

        return tasks


