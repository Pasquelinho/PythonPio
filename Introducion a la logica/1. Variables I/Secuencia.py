def fibonacci(n):
  """Calcula los n primeros números de la secuencia de Fibonacci."""
  if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
  elif n == 1:
    return [0]
  else:
    secuencia = [0, 1]
    while len(secuencia) < n:
      siguiente = secuencia[-1] + secuencia[-2]
      secuencia.append(siguiente)
    return secuencia

# Solicitar el número de términos
n = int(input("Ingrese la cantidad de términos de la secuencia de Fibonacci: "))

# Obtener y mostrar la secuencia
resultado = fibonacci(n)
print("Los primeros", n, "términos de la secuencia de Fibonacci son:", resultado)