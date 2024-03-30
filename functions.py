def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

#def convert_fahrenheit_to_celsius(fahrenheit):
#    return multiply(subtract(fahrenheit, 32), 5 / 9) # <-- Fix this in step 7

def convert_fahrenheit_to_celsius(fahrenheit):
 if fahrenheit < -459.67:
    raise ValueError("El valor de Fahrenheit no puede ser menor que -459.67")
    return multiply(subtract(fahrenheit, 32), 5 / 9)