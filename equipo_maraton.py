from typing import List

from .programador import Programador
from .validaciones import validar_contrasena


class EquipoMaratonProgramacion:


    def __init__(self, nombre_equipo: str, universidad: str, lenguaje_programacion: str, contrasena: str | None = None, confirmacion: str | None = None):
        if nombre_equipo is None or nombre_equipo.strip() == "":
            raise ValueError("El nombre del equipo es obligatorio")
        if universidad is None or universidad.strip() == "":
            raise ValueError("La universidad es obligatoria")
        if lenguaje_programacion is None or lenguaje_programacion.strip() == "":
            raise ValueError("El lenguaje de programación es obligatorio")

        self._nombre_equipo = nombre_equipo.strip()
        self._universidad = universidad.strip()
        self._lenguaje_programacion = lenguaje_programacion.strip()
        self._programadores: List[Programador] = []
        self._capacidad = 3
        self._contrasena: str | None = None
        # Si se provee contraseña, se valida y se almacena
        if contrasena is not None or confirmacion is not None:
            validar_contrasena(contrasena or "", confirmacion or "")
            self._contrasena = contrasena

    @property
    def capacidad(self) -> int:
        return self._capacidad

    @property
    def tamano_equipo(self) -> int:
        return len(self._programadores)

    @property
    def nombre_equipo(self) -> str:
        return self._nombre_equipo

    @property
    def universidad(self) -> str:
        return self._universidad

    @property
    def lenguaje_programacion(self) -> str:
        return self._lenguaje_programacion

    @property
    def contrasena(self) -> str | None:
        return self._contrasena

    def equipo_completo(self) -> bool:
        return self.tamano_equipo >= self.capacidad

    def agregar_programador(self, nombre: str, apellidos: str):
        if self.equipo_completo():
            raise ValueError("El equipo está lleno (máximo 3 programadores)")
        nuevo = Programador(nombre, apellidos)
        self._programadores.append(nuevo)

    def resumen_equipo(self) -> str:
        if self.tamano_equipo < 2:
            raise ValueError("El equipo debe tener mínimo 2 programadores")
        lineas = [
            f"Equipo: {self._nombre_equipo}",
            f"Universidad: {self._universidad}",
            f"Lenguaje: {self._lenguaje_programacion}",
            f"Programadores ({self.tamano_equipo}/{self.capacidad}):",
        ]
        for p in self._programadores:
            lineas.append(f" - {p.nombre} {p.apellidos}")
        return "\n".join(lineas)