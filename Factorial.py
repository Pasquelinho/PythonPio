def factorial(n):
  """Calcula el factorial de un número entero positivo."""
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
  
Numero = int(input("Escribe el numero el cual quieres sacarle el factorial, tiene que ser natural positivo: "))
if Numero < 0:
      print ("Ingrese un numero positivo")
resultado = factorial(Numero)
print("El factorial de", Numero, "es", resultado)
    
       
    














