import math
import tkinter as tk
from tkinter import ttk


class CalculosNumericos:

    @staticmethod
    def calcular_logaritmo_neperiano(valor: str) -> str:
        try:
            numero = float(str(valor).strip().replace(",", "."))  # ValueError si no es numérico
            if numero <= 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            return f"Resultado = {math.log(numero)}"
        except ArithmeticError:
            return "El valor debe ser un número positivo para calcular el logaritmo"
        except ValueError:  # Equivale a la InputMismatchException de Java
            return "El valor debe ser numérico para calcular el logaritmo"

    @staticmethod
    def calcular_raiz_cuadrada(valor: str) -> str:
        try:
            numero = float(str(valor).strip().replace(",", "."))  # ValueError si no es numérico
            if numero < 0:
                # Si el valor es negativo, se genera una excepción aritmética
                raise ArithmeticError("El valor debe ser un número positivo")
            return f"Resultado = {math.sqrt(numero)}"
        except ArithmeticError:
            return "El valor debe ser un número positivo para calcular la raíz cuadrada"
        except ValueError:  # Equivale a la InputMismatchException de Java
            return "El valor debe ser numérico para calcular la raíz cuadrada"


class AppCalculosNumericos:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Ejercicio 6.6 - Cálculos numéricos")
        self.root.geometry("560x270")
        self.root.resizable(False, False)

        ttk.Label(root, text="Valor numérico:", font=("Arial", 12, "bold")).pack(pady=(18, 6))
        self.entrada = ttk.Entry(root, width=28, justify="center")
        self.entrada.pack()
        self.entrada.bind("<Return>", lambda evento: self.calcular())

        botones = ttk.Frame(root)
        botones.pack(pady=14)
        ttk.Button(botones, text="Calcular", command=self.calcular).pack(side="left", padx=5)
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(side="left", padx=5)

        self.lbl_logaritmo = ttk.Label(root, text="Logaritmo neperiano: -", wraplength=520)
        self.lbl_logaritmo.pack(anchor="w", padx=20, pady=4)
        self.lbl_raiz = ttk.Label(root, text="Raíz cuadrada: -", wraplength=520)
        self.lbl_raiz.pack(anchor="w", padx=20, pady=4)

    def calcular(self) -> None:
        valor = self.entrada.get()
        resultado_log = CalculosNumericos.calcular_logaritmo_neperiano(valor)
        resultado_raiz = CalculosNumericos.calcular_raiz_cuadrada(valor)
        self.lbl_logaritmo.config(text="Logaritmo neperiano: " + resultado_log)
        self.lbl_raiz.config(text="Raíz cuadrada: " + resultado_raiz)

    def limpiar(self) -> None:
        self.entrada.delete(0, tk.END)
        self.lbl_logaritmo.config(text="Logaritmo neperiano: -")
        self.lbl_raiz.config(text="Raíz cuadrada: -")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppCalculosNumericos(root)
    root.mainloop()
