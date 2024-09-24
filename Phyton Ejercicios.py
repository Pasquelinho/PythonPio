def contador_ascendente():
  """Solicita al usuario un número entero positivo e imprime los números desde 1 hasta ese número."""

  while True:  # Bucle para asegurar una entrada válida
    try:
      numero = int(input("Ingresa un número entero positivo: "))
      if numero > 0:
        break  # Sal del bucle si la entrada es válida
      else:
        print("El número debe ser positivo. Inténtalo de nuevo.")
    except ValueError:
      print("Entrada inválida. Debes ingresar un número entero.")

  # Imprime los números desde 1 hasta el número ingresado
  for i in range(1, numero + 1):
    print(i)

# Llama a la función para ejecutar el programa
contador_ascendente()