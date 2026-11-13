import tkinter as tk
from tkinter import ttk


class PruebaExcepciones:

    def ejecutar(self) -> list:
        salida = []

        # Primer bloque try
        try:
            salida.append("Ingresando al primer try")
            cociente = 10000 / 0 
            salida.append("Después de la división") 
        except ZeroDivisionError:  
            salida.append("División por cero")
        finally:
          
            salida.append("Ingresando al primer finally")

 
        try:
            salida.append("Ingresando al segundo try")
            objeto = None
        
            objeto.upper()  # Se lanza una excepción
            salida.append("Imprimiendo objeto")  
        except ZeroDivisionError:  
            salida.append("División por cero")
        except Exception: 
            salida.append("Ocurrió una excepción")
        finally:
            salida.append("Ingresando al segundo finally")

        return salida


class AppPruebaExcepciones:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.prueba = PruebaExcepciones()
        self.root.title("Ejercicio 6.4 - Excepciones")
        self.root.geometry("460x360")
        self.root.resizable(False, False)

        ttk.Label(root, text="Resultado de ejecutar PruebaExcepciones",
                  font=("Arial", 12, "bold")).pack(pady=(15, 8))

        self.txt_salida = tk.Text(root, width=50, height=12, state="disabled",
                                  font=("Consolas", 10))
        self.txt_salida.pack(padx=15)

        botones = ttk.Frame(root)
        botones.pack(pady=12)
        ttk.Button(botones, text="Ejecutar", command=self.ejecutar).pack(side="left", padx=5)
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(side="left", padx=5)

    def mostrar(self, lineas: list) -> None:
        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", tk.END)
        self.txt_salida.insert(tk.END, "\n".join(lineas))
        self.txt_salida.config(state="disabled")

    def ejecutar(self) -> None:
        self.mostrar(self.prueba.ejecutar())

    def limpiar(self) -> None:
        self.mostrar([])


if __name__ == "__main__":
    root = tk.Tk()
    app = AppPruebaExcepciones(root)
    root.mainloop()
