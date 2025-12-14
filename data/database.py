# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime


class ToDoDatabase:
    """
    Data access layer.
    Handles all SQLite database operations.
    Uses a single database connection.
    """

    def __init__(self, db_name="todo.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        """Create the tasks table if it does not already exist."""
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                priority TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def add_task(self, title, priority):
        """Insert a new task into the database."""
        cursor = self.connection.cursor()
        created_at = datetime.now().isoformat()

        cursor.execute("""
            INSERT INTO tasks (title, priority, created_at)
            VALUES (?, ?, ?)
        """, (title, priority, created_at))

        self.connection.commit()

    def delete_task(self, task_id):
        """Delete a task from the database by id."""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.connection.commit()

    def get_all_tasks(self):
        """Return all tasks stored in the database."""
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT  id, title, priority, created_at
            FROM tasks
            ORDER BY created_at ASC
        """)
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()


