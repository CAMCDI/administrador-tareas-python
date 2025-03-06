import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Tareas")
        self.root.geometry("600x400")
        
        self.tasks = []
        
        self.style = tb.Style("superhero")
        
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.task_entry = ttk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        
        self.add_button = ttk.Button(self.frame, text="Agregar Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)
        
        self.task_list = ttk.Treeview(self.frame, columns=("Tarea", "Estado"), show='headings')
        self.task_list.heading("Tarea", text="Tarea")
        self.task_list.heading("Estado", text="Estado")
        self.task_list.column("Tarea", width=300)
        self.task_list.column("Estado", width=100)
        self.task_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        self.complete_button = ttk.Button(self.frame, text="Completar", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.delete_button = ttk.Button(self.frame, text="Eliminar", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append((task, "Pendiente"))
            self.task_list.insert("", tk.END, values=(task, "Pendiente"))
            self.task_entry.delete(0, tk.END)
    
    def complete_task(self):
        selected_item = self.task_list.selection()
        if selected_item:
            item_values = self.task_list.item(selected_item, "values")
            self.task_list.item(selected_item, values=(item_values[0], "Completada"))
    
    def delete_task(self):
        selected_item = self.task_list.selection()
        if selected_item:
            self.task_list.delete(selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
