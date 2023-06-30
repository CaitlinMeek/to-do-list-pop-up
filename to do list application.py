

#Todo List Application: Develop a simple command-line or graphical interface application
#that allows users to create, manage, and track their to-do lists.

#idea for basic code

#need GUI


#when button is pressed to add item to to-do list, should be able to input
#input should be displayed and added to the list on the interface
#add=input("Add item:")
#have section where all add can be displayed
#print(add)


import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

def delete_item():
    selected_indices = listbox.curselection()
    if selected_indices:
        for index in reversed(selected_indices):
            listbox.delete(index)

def show_options():
    index = listbox.curselection()
    if index:
        item = listbox.get(index)
        options = ['Important', 'Set Time', 'Work', 'Personal']
        selected_options = []
        for option in options:
            choice = messagebox.askyesno("Select Option", f"Select '{option}' for '{item}'?")
            if choice:
                selected_options.append(option)
        if selected_options:
            print(f"{item}: {', '.join(selected_options)}")

def clear_selection():
    listbox.selection_clear(0, tk.END)

root = tk.Tk()
root.title("To Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 12))
entry.pack(side=tk.LEFT, padx=10)

button = tk.Button(frame, text="Add Item", command=add_item)
button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, font=("Helvetica", 12), width=50, selectmode=tk.SINGLE)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Item", command=delete_item)
delete_button.pack(side=tk.RIGHT)

options_button = tk.Button(root, text="Options", command=show_options)
options_button.pack(side=tk.RIGHT, padx=5)

unselect_button = tk.Button(root, text="Unselect", command=clear_selection)
unselect_button.pack(side=tk.RIGHT)

root.mainloop()

