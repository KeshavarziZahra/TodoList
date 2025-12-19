# -*- coding: utf-8 -*-

import tkinter as tk
from gui.app_gui import ToDoGUI
from models.todo_manager import ToDoManager


def main():
    root = tk.Tk()
    toDoManager = ToDoManager()
    app = ToDoGUI(root, toDoManager)
    root.mainloop()


if __name__ == "__main__":
    main()