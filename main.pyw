from datetime import datetime, timedelta
from tkinter import *

task = 0
global tasks
tasks = []

class Task:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def create(name, time): # Create a new task
    task = Task(name, time)
    taskname = task.name
    starttime = datetime.now()
    endtime = starttime + timedelta(minutes = task.time)
    endtime = endtime.time().strftime("%H:%M")
    T.delete("1.0","end")
    tasks.append(f"[{taskname}], Deadline: {endtime}\n")
    for task in tasks:
        T.insert('end', task)

def enter():
    name = ""
    time = 0
    name = name_var.get()
    time = time_var.get()
    create(name, time)

def done(): # This function marks the current tasks as done
    global tasks
    T.delete("1.0","end")
    T.insert('end', "You have no tasks at the moment")
    taskentry.delete(0, 'end')
    timeentry.delete(0, 'end')
    tasks = []

# Main window
root = Tk()
root.geometry("450x600")
root.title("Personal Task Manager")
root['bg'] = 'khaki'

name_var = StringVar()
time_var = IntVar()

# Widgets
tasklabel = Label(root, text = "Enter new task:")
tasklabel.grid(row = 0, column = 0, padx = 20, pady = 10)

taskentry = Entry(root, textvariable = name_var)
taskentry.grid(row = 1, column = 0, padx = 20)

timelabel = Label(root, text = "Enter time to be alloted (minutes):")
timelabel.grid(row = 0, column = 1, padx = 20)

timeentry = Entry(root, textvariable = time_var)
timeentry.grid(row = 1, column = 1)

btn_ok = Button(root, text = "Enter", bg = 'lightblue', command = enter)
btn_ok.grid(row = 1, column = 2)

btn_done = Button(root, text = "Done", bg = 'lightblue', command = done)
btn_done.grid(row = 2, column = 2)

T = Text(root, height = 30, width = 45)
T.grid(row = 2, column = 0, columnspan = 2, pady = 20)
T.insert('end', "You have no tasks at the moment")

root.mainloop()
