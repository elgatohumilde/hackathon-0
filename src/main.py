def calculate(e):

    if not e.strip():
        raise ValueError("La expresión está vacía o contiene solo espacios.")

    valid_chars = "0123456789.+-*/() "
    if any(char not in valid_chars for char in e):
        raise ValueError("La expresión contiene caracteres no válidos.")
