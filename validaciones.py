import re


def validar_contrasena(contrasena: str, confirmacion: str) -> None:
    """Valida una contraseña conforme a los requisitos del PDF.

    Requisitos:
    - Mínimo 8 caracteres.
    - Sin espacios en blanco.
    - Al menos una letra, una mayúscula, un número y un carácter especial.
    - Debe coincidir con la confirmación.
    Lanza ValueError con mensajes descriptivos al fallar.
    """
    if contrasena is None or confirmacion is None:
        raise ValueError("La contraseña y confirmación son obligatorias")

    pwd = contrasena
    if len(pwd) < 8:
        raise ValueError("La contraseña debe tener mínimo 8 caracteres")
    if re.search(r"\s", pwd):
        raise ValueError("La contraseña no debe contener espacios en blanco")
    if not re.search(r"[A-Za-z]", pwd):
        raise ValueError("La contraseña debe incluir al menos una letra")
    if not re.search(r"[A-Z]", pwd):
        raise ValueError("La contraseña debe incluir al menos una mayúscula")
    if not re.search(r"\d", pwd):
        raise ValueError("La contraseña debe incluir al menos un número")
    if not re.search(r"[^A-Za-z0-9]", pwd):
        raise ValueError("La contraseña debe incluir al menos un carácter especial")
    if contrasena != confirmacion:
        raise ValueError("Las contraseñas no son iguales")