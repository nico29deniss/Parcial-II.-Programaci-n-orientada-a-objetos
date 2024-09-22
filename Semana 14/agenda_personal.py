import tkinter as tk
from tkinter import messagebox, Menu, scrolledtext

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Menú
        self.menu_bar = Menu(root)
        menu_archivo = Menu(self.menu_bar, tearoff=0)
        menu_archivo.add_command(label="Abrir", command=self.menu_action)
        menu_archivo.add_command(label="Guardar", command=self.menu_action)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=root.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
        root.config(menu=self.menu_bar)

        # Etiqueta
        tk.Label(root, text="Agenda Personal").pack(pady=10)

        # Campo de texto
        self.desc_entry = tk.Entry(root)
        self.desc_entry.pack(pady=5)

        # Botón para agregar evento
        self.add_button = tk.Button(root, text="Agregar Evento", command=self.add_event)
        self.add_button.pack(pady=5)

        # Casilla de verificación
        self.var_check = tk.IntVar()
        self.check_box = tk.Checkbutton(root, text="Opción de Recordatorio", variable=self.var_check)
        self.check_box.pack(pady=5)

        # Lista desplegable
        self.opciones = ["Importante", "Normal", "Bajo"]
        self.variable_seleccionada = tk.StringVar(root)
        self.variable_seleccionada.set(self.opciones[0])
        self.dropdown = tk.OptionMenu(root, self.variable_seleccionada, *self.opciones)
        self.dropdown.pack(pady=5)

        # Botones de radio
        self.var_radio = tk.StringVar()
        self.var_radio.set(self.opciones[0])  # Inicializa con la primera opción
        tk.Radiobutton(root, text="Importante", variable=self.var_radio, value="Importante").pack(anchor=tk.W)
        tk.Radiobutton(root, text="Normal", variable=self.var_radio, value="Normal").pack(anchor=tk.W)
        tk.Radiobutton(root, text="Bajo", variable=self.var_radio, value="Bajo").pack(anchor=tk.W)

        # Área de texto (Text Widget)
        self.area_texto = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.area_texto.pack(pady=10)

    def add_event(self):
        descripcion = self.desc_entry.get()
        prioridad = self.variable_seleccionada.get()
        recordatorio = "Sí" if self.var_check.get() else "No"
        if not descripcion:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una descripción.")
            return

        self.area_texto.insert(tk.END, f"Evento: {descripcion}, Prioridad: {prioridad}, Recordatorio: {recordatorio}\n")
        self.desc_entry.delete(0, tk.END)

    def menu_action(self):
        messagebox.showinfo("Menú", "Opción del menú seleccionada")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
