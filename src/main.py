def calculate(e):

    if not e.strip():
        raise ValueError("La expresión está vacía o contiene solo espacios.")

    valid_chars = "0123456789.+-*/() "
    if any(char not in valid_chars for char in e):
        raise ValueError("La expresión contiene caracteres no válidos.")

    def evaluate_expression(e):
        while "*" in e or "/" in e:
            for i, op in enumerate(e):
                if op == "*":
                    if i - 1 < 0 or i + 1 >= len(e):
                        raise SyntaxError("Sintaxis inválida en la expresión.")
                    left = float(e[i - 1])
                    right = float(e[i + 1])
                    res = left * right
                    e = e[:i - 1] + [str(round(res, 10))] + e[i + 2:]
                    break

                if op == "/":
                    if i - 1 < 0 or i + 1 >= len(e):
                        raise SyntaxError("Sintaxis inválida en la expresión.")
                    left = float(e[i - 1])
                    right = float(e[i + 1])
                    if right == 0:
                        raise ZeroDivisionError("División por cero.")
                    res = left / right
                    e = e[:i - 1] + [str(round(res, 10))] + e[i + 2:]
                    break

        while "+" in e or "-" in e:
            for i, op in enumerate(e):
                if op == "+":  # SUMA: JOAQUIN
                    if i - 1 < 0 or i + 1 >= len(e):
                        raise SyntaxError("Sintaxis inválida en la expresión.")
                    left = float(e[i - 1])
                    right = float(e[i + 1])
                    res = left + right
                    e = e[:i - 1] + [str(round(res, 10))] + e[i + 2:]
                    break

        result = float(e[0])
        return int(result) if result.is_integer() else result
