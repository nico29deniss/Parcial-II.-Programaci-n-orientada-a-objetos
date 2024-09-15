import tkinter as tk

# Función para agregar elementos a la lista
def agregar_dato():
    dato = entrada.get()
    if dato:
        lista.insert(tk.END, dato)
        entrada.set('')  # Limpiar el campo de entrada
    else:
        tk.messagebox.showwarning("Advertencia", "El campo está vacío")

# Función para limpiar la lista y el campo de texto
def limpiar_datos():
    lista.delete(0, tk.END)  # Limpiar la lista

# Crear ventana principal
app = tk.Tk()
app.title("Gestor de Datos")
app.geometry("400x400")

# Variable para entrada
entrada = tk.StringVar()

# Componentes GUI
tk.Label(app, text="Ingrese el valor:", font=('Arial', 10)).pack(pady=10)
tk.Entry(app, fg='black', bg='white', font=('Arial', 10), textvariable=entrada).pack(pady=10)
tk.Button(app, text="Agregar", font=('Arial', 10), bg='red', fg='white', command=agregar_dato).pack(pady=10)

# Lista para agregar datos
lista = tk.Listbox(app, font=('Arial', 12), width=40, height=20)
lista.pack(pady=10)

# Botón para limpiar la lista
tk.Button(app, text="Limpiar", font=('Arial', 10), bg='blue', fg='white', command=limpiar_datos).pack(pady=10)

# Iniciar el bucle principal
app.mainloop()
