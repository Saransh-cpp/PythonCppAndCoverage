from build import calc


def multiply(a, b, lang):
    if lang.lower() == "python":
        return a * b
    elif lang.lower() == "cpp":
        return calc.multiply(a, b)

    raise ValueError("lang can only be python or cpp")


def divide(a, b, lang):
    if b == 0:
     raise ValueError("denominator cannot be zero")

    if lang.lower() == "python":
        return a / b
    elif lang.lower() == "cpp":
        return calc.divide(a, b)

    raise ValueError("lang can only be python or cpp")


def add(a, b, lang):
    if lang.lower() == "python":
        return a + b
    elif lang.lower() == "cpp":
        return calc.add(a, b)

    raise ValueError("lang can only be python or cpp")


def subtract(a, b, lang):
    if lang.lower() == "python":
        return a - b
    elif lang.lower() == "cpp":
        return calc.subtract(a, b)

    raise ValueError("lang can only be python or cpp")
