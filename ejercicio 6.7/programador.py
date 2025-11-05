class Programador:
    """Clase Programador con validaciones de nombre y apellidos.

    Reglas del PDF:
    - Campos obligatorios (no vacíos)
    - Solo texto (sin dígitos)
    - Longitud máxima 20 caracteres
    """

    def __init__(self, nombre: str, apellidos: str):
        Programador.validar_texto(nombre, "Nombre")
        Programador.validar_texto(apellidos, "Apellidos")
        self._nombre = nombre.strip()
        self._apellidos = apellidos.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def apellidos(self) -> str:
        return self._apellidos

    @staticmethod
    def validar_texto(valor: str, etiqueta: str):
        if valor is None or valor.strip() == "":
            raise ValueError(f"{etiqueta} es obligatorio")
        v = valor.strip()
        if len(v) > 20:
            raise ValueError(f"{etiqueta} no puede superar 20 caracteres")
        for c in v:
            if c.isdigit():
                raise ValueError(f"{etiqueta} debe contener solo texto (sin números)")