def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = multiply(subtract(fahrenheit, 32), 5 / 9)
    if celsius < 0:
            raise AssertionError("El resultado es menor que 0 en Celsius")
    return celsius
