import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os

class LeerArchivoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Lector de Archivos - Ejercicio 6.8")
        master.geometry("600x500")

        # Frame para la entrada de archivo
        frame_archivo = tk.Frame(master, padx=10, pady=10)
        frame_archivo.pack(fill=tk.X)

        tk.Label(frame_archivo, text="Nombre del archivo:").pack(side=tk.LEFT)
        
        # Usar la ruta relativa correcta
        default_file_path = os.path.join("ejercicios", "ejercicio 6.8", "prueba.txt")
        self.ruta_archivo_var = tk.StringVar(value=default_file_path)
        
        self.entry_archivo = tk.Entry(frame_archivo, textvariable=self.ruta_archivo_var, width=40)
        self.entry_archivo.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.btn_browse = tk.Button(frame_archivo, text="...", command=self.seleccionar_archivo)
        self.btn_browse.pack(side=tk.LEFT)

        # Frame para los botones de acción
        frame_acciones = tk.Frame(master, padx=10, pady=5)
        frame_acciones.pack(fill=tk.X)

        self.btn_leer = tk.Button(frame_acciones, text="Leer Archivo", command=self.leer_archivo)
        self.btn_leer.pack(side=tk.LEFT, padx=5)

        self.btn_mayusculas = tk.Button(frame_acciones, text="Convertir a Mayúsculas", command=self.convertir_a_mayusculas)
        self.btn_mayusculas.pack(side=tk.LEFT, padx=5)

        # Área de texto para mostrar el contenido
        self.texto_contenido = scrolledtext.ScrolledText(master, wrap=tk.WORD, state=tk.DISABLED)
        self.texto_contenido.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        
        # Etiqueta de estado
        self.status_var = tk.StringVar()
        self.status_label = tk.Label(master, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def seleccionar_archivo(self):
        """Abre un diálogo para seleccionar un archivo y actualiza el campo de entrada."""
        ruta = filedialog.askopenfilename(
            initialdir=os.path.dirname(self.ruta_archivo_var.get()), # Directorio inicial
            title="Seleccionar archivo de texto",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        if ruta:
            # Convertir a ruta relativa si está dentro del proyecto
            try:
                rel_path = os.path.relpath(ruta, start=os.getcwd())
                self.ruta_archivo_var.set(rel_path)
            except ValueError:
                # Si está en una unidad diferente, usar la ruta absoluta
                self.ruta_archivo_var.set(ruta)

    def leer_archivo(self):
        """Lee el contenido del archivo especificado y lo muestra en el área de texto."""
        ruta_archivo = self.ruta_archivo_var.get()
        self.texto_contenido.config(state=tk.NORMAL)
        self.texto_contenido.delete(1.0, tk.END)
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                self.texto_contenido.insert(tk.END, contenido)
            self.status_var.set(f"Archivo '{os.path.basename(ruta_archivo)}' leído correctamente.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"El archivo '{ruta_archivo}' no fue encontrado.")
            self.status_var.set(f"Error: El archivo '{ruta_archivo}' no existe.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al leer el archivo: {e}")
            self.status_var.set(f"Error al leer el archivo.")
        finally:
            self.texto_contenido.config(state=tk.DISABLED)

    def convertir_a_mayusculas(self):
        """Convierte el texto actual en el área de texto a mayúsculas."""
        contenido_actual = self.texto_contenido.get(1.0, tk.END)
        if contenido_actual.strip():
            self.texto_contenido.config(state=tk.NORMAL)
            self.texto_contenido.delete(1.0, tk.END)
            self.texto_contenido.insert(tk.END, contenido_actual.upper())
            self.texto_contenido.config(state=tk.DISABLED)
            self.status_var.set("Texto convertido a mayúsculas.")
        else:
            self.status_var.set("No hay texto para convertir.")