import tkinter as tk
from tkinter import ttk, messagebox


class Vendedor:

    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None

    def verificar_edad(self, edad: int) -> None:
        
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        self.edad = edad

    def imprimir(self) -> str:
        return (f"Nombre del vendedor = {self.nombre}\n"
                f"Apellidos del vendedor = {self.apellidos}\n"
                f"Edad del vendedor = {self.edad}")


class AppVendedor:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Ejercicio 6.5 - Vendedor")
        self.root.geometry("420x330")
        self.root.resizable(False, False)

        ttk.Label(root, text="Datos del vendedor", font=("Arial", 12, "bold")).pack(pady=(15, 8))

        formulario = ttk.Frame(root)
        formulario.pack(padx=20, fill="x")
        self.campos = {}
        for fila, etiqueta in enumerate(("Nombre", "Apellidos", "Edad")):
            ttk.Label(formulario, text=f"{etiqueta}:", width=10).grid(row=fila, column=0, sticky="w")
            entrada = ttk.Entry(formulario, width=32)
            entrada.grid(row=fila, column=1, pady=4)
            self.campos[etiqueta] = entrada

        botones = ttk.Frame(root)
        botones.pack(pady=12)
        ttk.Button(botones, text="Registrar vendedor", command=self.registrar).pack(side="left", padx=5)
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(side="left", padx=5)

        ttk.Label(root, text="Resultado:", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
        self.lbl_resultado = ttk.Label(root, text="-", justify="left")
        self.lbl_resultado.pack(anchor="w", padx=20, pady=4)

    def registrar(self) -> None:
        nombre = self.campos["Nombre"].get().strip()
        apellidos = self.campos["Apellidos"].get().strip()
        if not nombre or not apellidos:
            messagebox.showwarning("Campos incompletos", "Ingrese el nombre y los apellidos.")
            return
        try:
            edad = int(self.campos["Edad"].get())
        except ValueError:  # Equivale a la InputMismatchException del Scanner
            messagebox.showerror("Dato no numérico", "La edad debe ser un número entero.")
            return

        vendedor = Vendedor(nombre, apellidos)
        try:
            vendedor.verificar_edad(edad)
        except ValueError as error:  # Excepción de argumento ilegal
            messagebox.showerror("Edad no válida", str(error))
            self.lbl_resultado.config(text="No se pudo registrar el vendedor.")
            return
        self.lbl_resultado.config(text=vendedor.imprimir())

    def limpiar(self) -> None:
        for entrada in self.campos.values():
            entrada.delete(0, tk.END)
        self.lbl_resultado.config(text="-")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppVendedor(root)
    root.mainloop()
