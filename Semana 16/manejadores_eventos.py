import tkinter as tk  # Importa la librería Tkinter para crear la interfaz gráfica
from tkinter import messagebox, simpledialog  # Importa diálogos de mensaje y entrada


class TaskManager:
    def __init__(self, master):
        self.master = master  # Guarda la referencia de la ventana principal
        self.master.title("Gestor de Tareas")  # Establece el título de la ventana

        # Variables
        self.tasks = []  # Inicializa una lista vacía para las tareas
        self.selected_task_index = None  # Inicializa el índice de la tarea seleccionada

        # UI Components
        self.task_entry = tk.Entry(master, width=50)  # Crea un campo de entrada para tareas
        self.task_entry.pack(pady=10)  # Agrega el campo de entrada a la ventana con un espaciado

        # Botón para añadir tareas
        self.add_button = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)  # Agrega el botón a la ventana

        # Botón para marcar tareas como completadas
        self.complete_button = tk.Button(master, text="Marcar Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)  # Agrega el botón a la ventana

        # Botón para eliminar tareas
        self.delete_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)  # Agrega el botón a la ventana

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(master, width=50, height=10)  # Crea una lista para mostrar las tareas
        self.task_listbox.pack(pady=10)  # Agrega el listbox a la ventana
        self.task_listbox.bind('<<ListboxSelect>>', self.on_task_select)  # Vincula un evento de selección

        # Atajos de teclado
        self.master.bind('<Return>', lambda event: self.add_task())  # Atajo para añadir tarea
        self.master.bind('<c>', lambda event: self.complete_task())  # Atajo para completar tarea
        self.master.bind('<Delete>', lambda event: self.delete_task())  # Atajo para eliminar tarea
        self.master.bind('<Escape>', lambda event: self.master.quit())  # Atajo para cerrar la aplicación

    def add_task(self):
        task = self.task_entry.get()  # Obtiene el texto del campo de entrada
        if task:  # Verifica que no esté vacío
            self.tasks.append(task)  # Añade la tarea a la lista de tareas
            self.update_task_list()  # Actualiza la lista mostrada
            self.task_entry.delete(0, tk.END)  # Limpia el campo de entrada

    def complete_task(self):
        if self.selected_task_index is not None:  # Verifica que hay una tarea seleccionada
            self.tasks[self.selected_task_index] += " (Completada)"  # Marca la tarea como completada
            self.update_task_list()  # Actualiza la lista mostrada
            self.selected_task_index = None  # Resetea la selección

    def delete_task(self):
        if self.selected_task_index is not None:  # Verifica que hay una tarea seleccionada
            self.tasks.pop(self.selected_task_index)  # Elimina la tarea de la lista
            self.update_task_list()  # Actualiza la lista mostrada
            self.selected_task_index = None  # Resetea la selección

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)  # Limpia el listbox
        for task in self.tasks:  # Itera sobre las tareas
            self.task_listbox.insert(tk.END, task)  # Agrega cada tarea al listbox

    def on_task_select(self, event):
        try:
            self.selected_task_index = self.task_listbox.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        except IndexError:
            self.selected_task_index = None  # Resetea la selección si no hay ninguna tarea seleccionada


if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = TaskManager(root)  # Crea una instancia de la clase TaskManager
    root.mainloop()  # Inicia el bucle de eventos de la aplicación
