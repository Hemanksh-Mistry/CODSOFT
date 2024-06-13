# To-Do List (GUI)

# Importing the required libraries
from tkinter import *
from tkinter import messagebox

# Creating the main window
root = Tk()
root.title("To-Do List")
root.geometry("400x450")
root.resizable(width=False, height=False)

# Function to add a task
def add_task():
        task = entry.get()
        if task:
                task = "[ ] " + task
                listbox.insert(END, task)
                entry.delete(0, END)
        else:
                messagebox.showwarning("Warning", "Please enter a task!")

# Function to delete a task
def delete_task():
        try:
                task_index = listbox.curselection()[0]
                listbox.delete(task_index)
        except:
                messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to mark a task as completed
def mark_completed():
        try:
                task_index = listbox.curselection()[0]
                task = listbox.get(task_index)
                if task.startswith("[ ]"):
                        task = task.replace("[ ]", "[X]")
                listbox.delete(task_index)
                listbox.insert(task_index, task)
        except:
                messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Function to mark a task as important
def mark_important():
        try:
                task_index = listbox.curselection()[0]
                task = listbox.get(task_index)
                if task.startswith("[ ]"):
                        task = task.replace("[ ]", "[!]")
                elif task.startswith("[X]"):
                        task = task.replace("[X]", "[!]")
                listbox.delete(task_index)
                listbox.insert(task_index, task)
        except:
                messagebox.showwarning("Warning", "Please select a task to mark as important!")

# Entry widget to enter a task
entry = Entry(root, width = 30)
entry.pack(pady = 20)

# Button to add a task
add_button = Button(root, text = "Add Task", command = add_task)
add_button.pack(pady = 10)

# Listbox to display tasks
listbox = Listbox(root, width = 50, height = 10)
listbox.pack(pady = 20)

# Displaying heading in the listbox (important, status, task)
listbox.insert(END, "Important | Status | Task")
listbox.insert(END, "-" * 50)

# Scrollbar for the listbox
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

# Button to delete a task
delete_button = Button(root, text = "Delete Task", command = delete_task)
delete_button.pack(pady = 10)

# Button to mark a task as completed
completed_button = Button(root, text = "Mark Completed", command = mark_completed)
completed_button.pack(pady = 10)

# Button to mark a task as important
important_button = Button(root, text = "Mark Important", command = mark_important)
important_button.pack(pady = 10)

root.mainloop()