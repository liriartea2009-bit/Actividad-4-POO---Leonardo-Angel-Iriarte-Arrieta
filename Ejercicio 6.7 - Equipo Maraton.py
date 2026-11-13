import tkinter as tk
from tkinter import ttk, messagebox


class CampoInvalidoError(Exception):
    """Se lanza cuando un campo de texto no cumple las condiciones de validación."""


class EquipoCompletoError(Exception):
    """Se lanza al añadir un programador a un equipo que ya está completo."""


class Programador:
    """Modela un integrante del equipo: tiene un nombre y apellidos."""

    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    """Modela un equipo de programadores (máximo tres) que participa en una maratón."""

    CAPACIDAD = 3

    def __init__(self, nombre_equipo: str, universidad: str, lenguaje_programacion: str):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = [None] * self.CAPACIDAD  # Espacio para tres programadores
        self.tamanio_equipo = 0  # El tamaño del equipo inicialmente es cero

    def esta_lleno(self) -> bool:
        return self.tamanio_equipo == len(self.programadores)

    def anadir(self, programador: Programador) -> None:
        if self.esta_lleno():  # Si el equipo está lleno, se genera la excepción
            raise EquipoCompletoError("El equipo está completo. No se pudo agregar programador.")
        self.programadores[self.tamanio_equipo] = programador
        self.tamanio_equipo += 1  # Se incrementa el tamaño del equipo

    @staticmethod
    def validar_campo(campo: str) -> None:
        """Valida que el campo no esté vacío, no tenga dígitos y no supere 20 caracteres."""
        if not campo:
            raise CampoInvalidoError("El campo no puede estar vacío.")
        for caracter in campo:
            if caracter.isdigit():  # Si el caracter es un dígito se genera la excepción
                raise CampoInvalidoError("El nombre no puede tener dígitos.")
        if len(campo) > 20:  # Si la longitud supera los 20 caracteres, se genera la excepción
            raise CampoInvalidoError("La longitud no debe ser superior a 20 caracteres.")


class AppEquipoMaraton:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.equipo = None
        self.root.title("Ejercicio 6.7 - Equipo de maratón de programación")
        self.root.geometry("470x540")
        self.root.resizable(False, False)

        marco_equipo = ttk.LabelFrame(root, text="Datos del equipo")
        marco_equipo.pack(fill="x", padx=15, pady=(15, 8))
        self.campos_equipo = self._crear_campos(
            marco_equipo, ("Nombre del equipo", "Universidad", "Lenguaje"))
        self.btn_crear = ttk.Button(marco_equipo, text="Crear equipo", command=self.crear_equipo)
        self.btn_crear.grid(row=3, column=0, columnspan=2, pady=8)

        marco_integrante = ttk.LabelFrame(root, text="Integrantes (mínimo 2, máximo 3)")
        marco_integrante.pack(fill="x", padx=15, pady=8)
        self.campos_integrante = self._crear_campos(marco_integrante, ("Nombre", "Apellidos"))
        ttk.Button(marco_integrante, text="Añadir integrante",
                   command=self.anadir_integrante).grid(row=2, column=0, columnspan=2, pady=8)

        self.lista = tk.Listbox(root, height=5)
        self.lista.pack(fill="x", padx=15, pady=8)
        self.lbl_estado = ttk.Label(root, text="Cree primero el equipo.")
        self.lbl_estado.pack()
        ttk.Button(root, text="Nuevo equipo", command=self.nuevo_equipo).pack(pady=12)

    @staticmethod
    def _crear_campos(marco, etiquetas) -> dict:
        campos = {}
        for fila, etiqueta in enumerate(etiquetas):
            ttk.Label(marco, text=f"{etiqueta}:", width=18).grid(row=fila, column=0, padx=8)
            entrada = ttk.Entry(marco, width=30)
            entrada.grid(row=fila, column=1, padx=8, pady=4)
            campos[etiqueta] = entrada
        return campos

    def crear_equipo(self) -> None:
        datos = [entrada.get().strip() for entrada in self.campos_equipo.values()]
        if not all(datos):
            messagebox.showwarning("Campos incompletos", "Complete todos los datos del equipo.")
            return
        self.equipo = EquipoMaratonProgramacion(*datos)
        self.btn_crear.config(state="disabled")
        self._actualizar_estado()

    def anadir_integrante(self) -> None:
        if self.equipo is None:
            messagebox.showwarning("Equipo no creado", "Primero debe crear el equipo.")
            return
        nombre = self.campos_integrante["Nombre"].get().strip()
        apellidos = self.campos_integrante["Apellidos"].get().strip()
        try:
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            self.equipo.anadir(Programador(nombre, apellidos))
        except CampoInvalidoError as error:
            messagebox.showerror("Campo no válido", str(error))
            return
        except EquipoCompletoError as error:
            messagebox.showinfo("Equipo completo", str(error))
            return
        self.lista.insert(tk.END, f"{nombre} {apellidos}")
        for entrada in self.campos_integrante.values():
            entrada.delete(0, tk.END)
        self._actualizar_estado()

    def nuevo_equipo(self) -> None:
        self.equipo = None
        entradas = list(self.campos_equipo.values()) + list(self.campos_integrante.values())
        for entrada in entradas:
            entrada.delete(0, tk.END)
        self.lista.delete(0, tk.END)
        self.btn_crear.config(state="normal")
        self.lbl_estado.config(text="Cree primero el equipo.")

    def _actualizar_estado(self) -> None:
        cantidad = self.equipo.tamanio_equipo
        if self.equipo.esta_lleno():
            estado = "equipo completo"
        elif cantidad >= 2:
            estado = "equipo válido (puede añadir uno más)"
        else:
            estado = "faltan integrantes (mínimo 2)"
        self.lbl_estado.config(
            text=f"{self.equipo.nombre_equipo} - Integrantes: {cantidad}/3 - {estado}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppEquipoMaraton(root)
    root.mainloop()
