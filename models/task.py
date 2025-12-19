# -*- coding: utf-8 -*-
from datetime import datetime

class Task:
    """
    Represents a single task in the to-do list.
    """

    def __init__(self, title, priority, task_id=None, created_at=None):
        self.id = task_id
        self.title = title
        self.priority = priority
        self.created_at = created_at

    def __str__(self):
        return f"{self.title} ({self.priority})"
