import tkinter as tk
from tkinter import messagebox

from .equipo_maraton import EquipoMaratonProgramacion
from .validaciones import validar_contrasena


class VentanaEquipo(tk.Tk):
    """Interfaz gráfica con Tkinter equivalente a la versión Java Swing."""

    def __init__(self):
        super().__init__()
        self.title("Equipo Maratón de Programación")
        self.geometry("720x520")

        # Modelo
        self.equipo: EquipoMaratonProgramacion | None = None

        # Secciones
        self._crear_panel_equipo()
        self._crear_panel_programadores()
        self._crear_panel_salida()

        self._actualizar_estado("Sin equipo creado")
        self._habilitar_programadores(False)

    # Panel de equipo
    def _crear_panel_equipo(self):
        marco = tk.LabelFrame(self, text="Datos del equipo")
        marco.pack(fill=tk.X, padx=10, pady=8)

        tk.Label(marco, text="Nombre del equipo:").grid(row=0, column=0, sticky="w", padx=6, pady=4)
        tk.Label(marco, text="Universidad:").grid(row=1, column=0, sticky="w", padx=6, pady=4)
        tk.Label(marco, text="Lenguaje de programación:").grid(row=2, column=0, sticky="w", padx=6, pady=4)
        tk.Label(marco, text="Contraseña:").grid(row=3, column=0, sticky="w", padx=6, pady=4)
        tk.Label(marco, text="Confirmación:").grid(row=4, column=0, sticky="w", padx=6, pady=4)

        self.tf_nombre_equipo = tk.Entry(marco, width=30)
        self.tf_universidad = tk.Entry(marco, width=30)
        self.tf_lenguaje = tk.Entry(marco, width=30)
        self.tf_pwd = tk.Entry(marco, width=30, show="*")
        self.tf_pwd_confirm = tk.Entry(marco, width=30, show="*")
        self.tf_nombre_equipo.grid(row=0, column=1, padx=6, pady=4)
        self.tf_universidad.grid(row=1, column=1, padx=6, pady=4)
        self.tf_lenguaje.grid(row=2, column=1, padx=6, pady=4)
        self.tf_pwd.grid(row=3, column=1, padx=6, pady=4)
        self.tf_pwd_confirm.grid(row=4, column=1, padx=6, pady=4)

        self.btn_crear_equipo = tk.Button(marco, text="Crear equipo", command=self._accion_crear_equipo)
        self.btn_crear_equipo.grid(row=5, column=0, columnspan=2, padx=6, pady=6, sticky="ew")

    # Panel de programadores
    def _crear_panel_programadores(self):
        marco = tk.LabelFrame(self, text="Agregar programadores (máximo 3)")
        marco.pack(fill=tk.X, padx=10, pady=8)

        tk.Label(marco, text="Nombre:").grid(row=0, column=0, sticky="w", padx=6, pady=4)
        tk.Label(marco, text="Apellidos:").grid(row=1, column=0, sticky="w", padx=6, pady=4)
        self.tf_nombre_prog = tk.Entry(marco, width=26)
        self.tf_apellidos_prog = tk.Entry(marco, width=26)
        self.tf_nombre_prog.grid(row=0, column=1, padx=6, pady=4)
        self.tf_apellidos_prog.grid(row=1, column=1, padx=6, pady=4)

        self.btn_agregar = tk.Button(marco, text="Agregar programador", command=self._accion_agregar_programador)
        self.btn_mostrar = tk.Button(marco, text="Mostrar equipo", command=self._accion_mostrar_equipo)
        self.btn_agregar.grid(row=2, column=0, padx=6, pady=6, sticky="ew")
        self.btn_mostrar.grid(row=2, column=1, padx=6, pady=6, sticky="ew")

        self.lbl_estado = tk.Label(marco, anchor="w")
        self.lbl_estado.grid(row=3, column=0, columnspan=2, sticky="ew", padx=6)

    # Panel de salida
    def _crear_panel_salida(self):
        marco = tk.Frame(self)
        marco.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
        self.ta_salida = tk.Text(marco, height=12)
        self.ta_salida.pack(fill=tk.BOTH, expand=True)

    # Acciones
    def _accion_crear_equipo(self):
        try:
            # Validación de contraseña según requisitos del PDF
            validar_contrasena(self.tf_pwd.get(), self.tf_pwd_confirm.get())
            self.equipo = EquipoMaratonProgramacion(
                self.tf_nombre_equipo.get(),
                self.tf_universidad.get(),
                self.tf_lenguaje.get(),
                self.tf_pwd.get(),
                self.tf_pwd_confirm.get(),
            )
            self._actualizar_estado(f"Equipo creado. Capacidad: {self.equipo.capacidad}")
            self._habilitar_programadores(True)
            self.btn_crear_equipo.configure(state=tk.DISABLED)
            self.tf_nombre_equipo.configure(state=tk.DISABLED)
            self.tf_universidad.configure(state=tk.DISABLED)
            self.tf_lenguaje.configure(state=tk.DISABLED)
            self.tf_pwd.configure(state=tk.DISABLED)
            self.tf_pwd_confirm.configure(state=tk.DISABLED)
        except ValueError as ex:
            messagebox.showerror("Validación", str(ex))

    def _accion_agregar_programador(self):
        if not self.equipo:
            messagebox.showerror("Validación", "Primero cree el equipo")
            return
        try:
            self.equipo.agregar_programador(self.tf_nombre_prog.get(), self.tf_apellidos_prog.get())
            self._actualizar_estado(f"Programadores: {self.equipo.tamano_equipo}/{self.equipo.capacidad}")
            self.ta_salida.insert(tk.END, f"Programador agregado: {self.tf_nombre_prog.get().strip()} {self.tf_apellidos_prog.get().strip()}\n")
            self.tf_nombre_prog.delete(0, tk.END)
            self.tf_apellidos_prog.delete(0, tk.END)
            if self.equipo.equipo_completo():
                self._habilitar_programadores(False)
                self.ta_salida.insert(tk.END, "\nEquipo completo. Puede mostrar el resumen.\n")
        except ValueError as ex:
            messagebox.showerror("Validación", str(ex))

    def _accion_mostrar_equipo(self):
        if not self.equipo:
            messagebox.showerror("Validación", "Primero cree el equipo")
            return
        try:
            self.ta_salida.insert(tk.END, "\n" + self.equipo.resumen_equipo() + "\n")
        except ValueError as ex:
            messagebox.showerror("Validación", str(ex))

    # Utilidades
    def _habilitar_programadores(self, habilitar: bool):
        state = tk.NORMAL if habilitar else tk.DISABLED
        self.tf_nombre_prog.configure(state=state)
        self.tf_apellidos_prog.configure(state=state)
        self.btn_agregar.configure(state=state)

    def _actualizar_estado(self, msg: str):
        self.lbl_estado.configure(text=msg)