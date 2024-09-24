def factorial(n):
  """Calcula el factorial de un número entero positivo."""
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Solicitar al usuario ingresar un número
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero < 0:
  print("El número debe ser positivo.") 

else:
  resultado = factorial(numero)
  print("El factorial de", numero, "es", resultado)