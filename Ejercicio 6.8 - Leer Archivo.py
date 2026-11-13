import io
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class LeerArchivo:

    @staticmethod
    def leer(nombre_archivo: str) -> list:
        lineas = []
        archivo = open(nombre_archivo, "rb")  # FileInputStream: flujo de bytes
        try:
            conversor = io.TextIOWrapper(archivo, encoding="utf-8-sig")
            linea = conversor.readline()  # Lectura línea a línea (como readLine de Java)
            while linea != "":  # Al llegar al final del archivo, readline() retorna ""
                lineas.append(linea.rstrip("\r\n"))
                linea = conversor.readline()  # Lee la siguiente línea
        finally:
            archivo.close()  # Cierra el archivo
        return lineas


class AppLeerArchivo:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Ejercicio 6.8 - Leer archivo de texto")
        self.root.geometry("540x430")

        marco_ruta = ttk.Frame(root)
        marco_ruta.pack(fill="x", padx=15, pady=(15, 5))
        ttk.Label(marco_ruta, text="Archivo:").pack(side="left")
        self.ruta = tk.StringVar(value="prueba.txt")
        ttk.Entry(marco_ruta, textvariable=self.ruta).pack(side="left", fill="x", expand=True, padx=6)
        ttk.Button(marco_ruta, text="Examinar...", command=self.examinar).pack(side="left")

        botones = ttk.Frame(root)
        botones.pack(pady=8)
        ttk.Button(botones, text="Leer archivo", command=self.leer).pack(side="left", padx=5)
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(side="left", padx=5)

        marco_texto = ttk.Frame(root)
        marco_texto.pack(fill="both", expand=True, padx=15, pady=5)
        self.txt_contenido = tk.Text(marco_texto, state="disabled", wrap="none",
                                     font=("Consolas", 10))
        barra = ttk.Scrollbar(marco_texto, command=self.txt_contenido.yview)
        self.txt_contenido.config(yscrollcommand=barra.set)
        barra.pack(side="right", fill="y")
        self.txt_contenido.pack(side="left", fill="both", expand=True)

        self.lbl_estado = ttk.Label(root, text="Seleccione un archivo y pulse 'Leer archivo'.")
        self.lbl_estado.pack(anchor="w", padx=15, pady=(0, 10))

    def examinar(self) -> None:
        tipos = [("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        ruta = filedialog.askopenfilename(title="Seleccione un archivo", filetypes=tipos)
        if ruta:
            self.ruta.set(ruta)

    def mostrar(self, lineas: list) -> None:
        self.txt_contenido.config(state="normal")
        self.txt_contenido.delete("1.0", tk.END)
        self.txt_contenido.insert(tk.END, "\n".join(lineas))
        self.txt_contenido.config(state="disabled")

    def leer(self) -> None:
        try:
            lineas = LeerArchivo.leer(self.ruta.get().strip())
        except (OSError, UnicodeDecodeError):  # En caso de que se genere una excepción
            messagebox.showerror("Error de lectura", "No se pudo leer el archivo.")
            self.lbl_estado.config(text="No se pudo leer el archivo.")
            return
        self.mostrar(lineas)
        self.lbl_estado.config(text=f"Archivo leído: {len(lineas)} línea(s).")

    def limpiar(self) -> None:
        self.mostrar([])
        self.lbl_estado.config(text="Seleccione un archivo y pulse 'Leer archivo'.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppLeerArchivo(root)
    root.mainloop()
